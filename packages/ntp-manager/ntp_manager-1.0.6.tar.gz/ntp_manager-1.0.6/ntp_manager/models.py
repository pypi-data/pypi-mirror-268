# %%
import math
from dataclasses import dataclass
from datetime import datetime
from typing import Literal, TypeVar, overload

import geojson
from numpy import array, multiply, ndarray
from serde import deserialize, field
from shapely.geometry import LineString, Polygon, shape, MultiPolygon


def with_geojson(initer):
    return lambda x: initer(shape(geojson.loads(x)))

LineStringWGJ = with_geojson(LineString)
PolygonWGJ = with_geojson(Polygon)


@deserialize
@dataclass
class NTPLine:
    linetype: int
    closed: bool # 闭合是 region, 开放是 mark
    line: LineString = field(deserializer=LineStringWGJ)

@deserialize
@dataclass
class NTPLabel:
    name: str
    position: tuple[float | int, float | int] | list = field(deserializer=tuple)

@deserialize
@dataclass
class NTPRegion:
    label: NTPLabel
    polygon: Polygon | MultiPolygon = field(deserializer=PolygonWGJ)
    area: float = 0

@deserialize
@dataclass
class NTPRegionWarnings:
    单标无区: list[NTPLabel]

    悬线: list[LineString] = field(deserializer=lambda x: [LineStringWGJ(i) for i in x])
    切线: list[LineString] = field(deserializer=lambda x: [LineStringWGJ(i) for i in x])
    劣线: list[LineString] = field(deserializer=lambda x: [LineStringWGJ(i) for i in x])
    单区多标: list[tuple[Polygon, list[NTPLabel]]] = field(
        deserializer=lambda x: [
            (PolygonWGJ(i[0]), [NTPLabel(*j.values()) for j in i[1]]) 
            for i in x
        ]
    )
    单区无标: list[Polygon] = field(deserializer=lambda x: [PolygonWGJ(i) for i in x])


T_SIZE_SOURCE = Literal['ntp', 'background', 'manual'] | str
T_COLOR_SOURCE = Literal['green', 'red', 'blue', 'yellow']

@deserialize
@dataclass
class Cells : 
    green : ndarray = field(default_factory=lambda: array([]))
    red   : ndarray = field(default_factory=lambda: array([]))
    blue  : ndarray = field(default_factory=lambda: array([]))
    yellow: ndarray = field(default_factory=lambda: array([]))

    colors: tuple[
        T_COLOR_SOURCE, T_COLOR_SOURCE, 
        T_COLOR_SOURCE, T_COLOR_SOURCE
    ] = ('green', 'red', 'blue', 'yellow')

    def __getitem__(self, color: T_COLOR_SOURCE | str) -> ndarray:
        return getattr(self, color)
    
    def __setitem__(self, color: T_COLOR_SOURCE | str, value: ndarray):
        setattr(self, color, value)

    def __iter__(self):
        for color in self.colors:
            yield color, getattr(self, color)

@dataclass
class Gains:
    #            blue   yellow red    green
    gains: tuple[float, float, float, float]


    def __getattr__(self, key: str):
        match key:
            case 'g1' | 'gb' | 'blue':
                return self.gains[0]
            case 'g2' | 'gy' | 'yellow':
                return self.gains[1]
            case 'g3' | 'gr' | 'red':
                return self.gains[2]
            case 'g4' | 'gg' | 'green':
                return self.gains[3]
            case other:
                return self.__dict__[other]

    def __repr__(self):
        return f'<Gains | blue: {self.gb:.4}, yellow: {self.gy:.4}, red: {self.gr:.4}, green: {self.gg:.4}>'

    @property
    def green(self): return self.gains[3]
    @property
    def red(self): return self.gains[2]
    @property
    def blue(self): return self.gains[1]
    @property
    def yellow(self): return self.gains[0]


@deserialize
@dataclass
class SliceMeta:
    '''
    from serde import from_dict
    slice_meta = from_dict(SliceMeta, json.load(open('slice_meta.json'))
    '''
    date: datetime
    ntp_path: str
    bin_size: int
    um_per_pixel: float
    background_path: str
    w: int | float
    h: int | float
    size_source: T_SIZE_SOURCE
    ignore_regions: list[str]
    transpose: bool

    ntp_resolution: float
    '''ntp 文件里写的分辨率，单位是 um/pixel，不因 to_bin_size 而改变'''
    ntp_w: int | float
    '''ntp 文件里写的宽度，单位是 pixel，不因 to_bin_size 而改变'''
    ntp_h: int | float
    '''ntp 文件里写的高度，单位是 pixel，不因 to_bin_size 而改变'''

    warnings: NTPRegionWarnings

    regions: list[NTPRegion]

    raw_labels: list[tuple[str, tuple[float, float]]]
    raw_lines: list[NTPLine]

    cells: Cells = field(default_factory=Cells)
    ntp_version: str = 'none'

    def to_bin_size(self, bin_size: int):
        scale = self.bin_size / bin_size
        new_self = scale_element(self, scale)
        new_self.bin_size = bin_size
        new_self.size_source = f'rebinsize {self.bin_size} -> {bin_size}'
        return new_self


T = TypeVar("T", NTPLine, NTPLabel, NTPRegion, NTPRegionWarnings, Cells, SliceMeta)

# 以下几行是因为 pyright、mypy 无法正确推断递归泛型，期待有一天注释掉这些代码后，二者不报错
# https://github.com/microsoft/pyright/issues/5777
@overload
def scale_element(e: Polygon, s: float) -> Polygon: ...
@overload
def scale_element(e: LineString, s: float) -> LineString: ...
@overload
def scale_element(e: NTPLine, s: float) -> NTPLine: ...
@overload
def scale_element(e: NTPLabel, s: float) -> NTPLabel: ...
@overload
def scale_element(e: NTPRegion, s: float) -> NTPRegion: ...
@overload
def scale_element(e: NTPRegionWarnings, s: float) -> NTPRegionWarnings: ...
@overload
def scale_element(e: Cells, s: float) -> Cells: ...
@overload
def scale_element(e: SliceMeta, s: float) -> SliceMeta: ...
# 以上几行是因为 pyright 无法正确推断递归泛型

def scale_element(e: T, s: float) -> T:
    if isinstance(e, Polygon):
        return Polygon([
            (x * s, y * s) for x, y in e.exterior.coords
        ])
    elif isinstance(e, LineString):
        return LineString([
            (x * s, y * s) for x, y in e.coords
        ])
    elif isinstance(e, NTPLine):
        return NTPLine(
            e.linetype, e.closed, 
            scale_element(e.line, s)
        )
    elif isinstance(e, NTPLabel):
        return NTPLabel(e.name, (e.position[0] * s, e.position[1] * s))
    elif isinstance(e, NTPRegion):
        return NTPRegion(
            scale_element(e.label, s), 
            scale_element(e.polygon, s), 
            e.area * s * s
        )
    elif isinstance(e, NTPRegionWarnings):
        return NTPRegionWarnings(
            e.单标无区,
            e.悬线, e.切线, e.劣线,
            [(Polygon([
                (x * s, y * s) for x, y in p.exterior.coords
            ]), l) for p, l in e.单区多标],
            [Polygon([
                (x * s, y * s) for x, y in p.exterior.coords
            ]) for p in e.单区无标]
        )
    elif isinstance(e, Cells):
        return Cells(
            green=array(e.green * s),
            red=array(e.red * s),
            blue=array(e.blue * s),
            yellow=array(e.yellow * s)
        )
    elif isinstance(e, SliceMeta):
        new_cells = scale_element(e.cells, s)

        return SliceMeta(
            e.date,
            e.ntp_path,
            e.bin_size,
            e.um_per_pixel,
            e.background_path,
            e.w * s,
            e.h * s,
            e.size_source,
            ignore_regions=e.ignore_regions,
            transpose=e.transpose,
            warnings=scale_element(e.warnings, s),
            
            regions=[scale_element(i, s) for i in e.regions],
            raw_labels=[
                (l[0], (l[1][0] * s, l[1][1] * s)) for l in e.raw_labels
            ],
            raw_lines=[scale_element(i, s) for i in e.raw_lines],
            cells=new_cells,
            ntp_version=e.ntp_version,
            ntp_resolution=e.ntp_resolution,
            ntp_w=e.ntp_w, 
            ntp_h=e.ntp_h
        )
    else:
        raise TypeError(f'unsupported type: {type(e)}')
