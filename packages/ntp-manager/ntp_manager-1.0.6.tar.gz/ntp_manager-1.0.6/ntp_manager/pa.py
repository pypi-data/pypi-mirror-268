import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Literal, overload

import fire
import numpy as np
import orjson
from imagesize import get as get_image_size
from shapely.geometry import LineString, MultiLineString, Point, Polygon
from shapely.geometry.collection import GeometryCollection
from shapely.ops import polygonize_full, unary_union

from ntp_manager.local_nhp_utils.ntp_file_reader import NTPFileReader
from ntp_manager.models import (NTPLabel, NTPLine, NTPRegion,
                                NTPRegionWarnings, SliceMeta, T_SIZE_SOURCE)
from ntp_manager.utils import geojson_default

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#                                保存到ntp同级  不保存    保存到指定位置
T_EXPORT_POSITION_POLICY = Literal['default', 'none'] | Path

def prepare_ntp(
    ntp_path: Path, /, *, 
    um_per_pixel: float = 0.65,
    bin_size: int = 1, 
    background_path: str | None = None, 
    w: int=0, h: int=0,
    transpose: bool = False,
) -> tuple[NTPFileReader, int, int, T_SIZE_SOURCE]:
    """准备好 ntp 

    Args:
        ntp_path (Path): _description_
        um_per_pixel (float, optional): 这里是最原始数据的分辨率，若意图影响最终大小，不要改这一条，通常来说时空组写 0.5，光学写 0.65/0.875/0.325. defaults to 0.65.
        bin_size (int, optional): 如果指定，应该与 w、h 同等次. Defaults to 1.
        background_path (str | None, optional): _description_. Defaults to None.
        w (int, optional): 如果指定，应该与 binsize 同等次. Defaults to 0.
        h (int, optional): 如果指定，应该与 binsize 同等次. Defaults to 0.
        transpose (bool, optional): 是否给 <T167 的转置. Defaults to False.

    Returns:
        tuple[NTPFileReader, int, int, T_SIZE_SOURCE]: _description_
    """    
    assert ntp_path.exists(), f'ntp_path {ntp_path} not exists'

    size_source: T_SIZE_SOURCE = 'ntp'

    if background_path:
        assert Path(background_path).exists(), f'background_path {background_path} not exists'
        w, h = [int(x) for x in get_image_size(background_path)]
        size_source = f'background from {background_path}'


    if w and h:
        image_center = np.array([w, h]) / 2
        ntp = NTPFileReader(
            ntp_path, resolution=um_per_pixel, 
            default_bin=bin_size,
            default_image_center=image_center,
            transpose=transpose,
        )
        size_source = size_source if not background_path else 'manual'
    else:
        ntp = NTPFileReader(
            ntp_path, resolution=um_per_pixel, 
            default_bin=bin_size,
            transpose=transpose,
        )
        ntp.default_image_center = (ntp.default_image_center / bin_size).astype(int)

        w, h = (ntp.default_image_center * 2).astype(int).tolist()
        size_source = 'ntp'

    return ntp, w, h, size_source

def prepare_export_path(export_position_policy: T_EXPORT_POSITION_POLICY, ntp_path: Path) -> Path | None:
    match export_position_policy:
        case 'default':
            export_base_path = ntp_path.parent
        case 'none':
            export_base_path = None    
        case _:
            export_base_path = Path(export_position_policy)

    return export_base_path

def fetch_ntp_lines(region_marks: dict[str, list[tuple[int, np.ndarray]]]):
    res: list[NTPLine] = []

    for t in ['region', 'mark']:
        closed = t == 'region'
        for current_type, current_data in region_marks[t]:
            points = current_data.tolist()
            if len(points) < 2:
                logger.warning(f'线段 {current_type} 点数小于2，跳过。{points=}')
                continue
            if closed:
                points.append(points[0])
            line = NTPLine(linetype=current_type, line=LineString(points), closed=closed)
            res.append(line)
    return res

def filter_ntp_lines(ntp_lines: list[NTPLine], ignore_regions: list[str]) -> list[LineString]:
    res = []
    for line in ntp_lines:
        current_type_str = f'{"region" if line.closed else "mark"}{line.linetype}'
        if current_type_str not in ignore_regions:
            res.append(line.line)

    return res


def lines_to_region(
    lines: list[LineString], 
    labels: list[tuple[str, tuple[float, float]]]
) -> tuple[list[NTPRegion], NTPRegionWarnings]:
    all_line_string = unary_union(MultiLineString(lines))
    polygons, cuts, dangles, invalids = polygonize_full(all_line_string)
    polygons: GeometryCollection

    label_to_id = defaultdict(set)
    id_to_label = defaultdict(set)

    regions: list[NTPRegion] = []
    ntp_warnings = NTPRegionWarnings(
        单区多标=[], 单区无标=[], 单标无区=[], 
        悬线=[], 切线=[], 劣线=[]
    )

    for label, position in labels:
        point = Point(position)
        for i, polygon in enumerate(polygons.geoms):
            polygon: Polygon
            if polygon.contains(point):
                label_to_id[(label, position)].add(i)
                id_to_label[i].add((label, position))
                regions.append(NTPRegion(
                    NTPLabel(name=label, position=position), 
                    polygon=polygon,
                    area=polygon.area,
                ))

    for label, position in labels:
        if len(label_to_id[(label, position)]) == 0:
            ntp_warnings.单标无区.append(NTPLabel(name=label, position=position))
    for i, polygon in enumerate(polygons.geoms):
        current_label = id_to_label[i]
        if len(current_label) == 0:
            ntp_warnings.单区无标.append(polygon)
        elif len(current_label) > 1:
            ntp_warnings.单区多标.append((
                polygon, 
                [NTPLabel(name=label, position=position) for label, position in current_label]
            ))

    ntp_warnings.悬线 = dangles.geoms
    ntp_warnings.切线 = cuts.geoms
    ntp_warnings.劣线 = invalids.geoms
    return regions, ntp_warnings



@overload
def main(
    ntp_path: str | Path, 
    /, *, 
    um_per_pixel: float = 0.65,
    bin_size: int = 1, 
    verbose: bool = False, ignore_regions: list[str] = ['region3','region4','mark4'],
    # region3 是是血管，region4 是检查，mark4是 layer4 但是在时空芯片里应该全都选
    background_path: str = '', 
    export_position_policy: T_EXPORT_POSITION_POLICY = 'default',
    w: int=0, h: int=0, 
    return_bytes: bool = False, 
    transpose: bool = False,
) -> SliceMeta: ...

@overload
def main(
    ntp_path: str | Path, 
    /, *, 
    um_per_pixel: float = 0.65,
    bin_size: int = 1, 
    verbose: bool = False, ignore_regions: list[str] = ['region3','region4','mark4'],
    # region3 是是血管，region4 是检查，mark4是 layer4 但是在时空芯片里应该全都选
    background_path: str = '', 
    export_position_policy: T_EXPORT_POSITION_POLICY = 'default',
    w: int=0, h: int=0, 
    return_bytes: bool = True, 
    transpose: bool = False,
) -> bytes: ...



def main(
    ntp_path: str | Path, 
    /, *, 
    um_per_pixel: float = 0.65,
    bin_size: int = 1, 
    verbose: bool = False, ignore_regions: list[str] = ['region3','region4','mark4'],
    # region3 是是血管，region4 是检查，mark4是 layer4 但是在时空芯片里应该全都选
    background_path: str = '', 
    export_position_policy: T_EXPORT_POSITION_POLICY = 'default',
    w: int=0, h: int=0, 
    return_bytes: bool = False, 
    transpose: bool = False,
):
    """_summary_

    Args:
        ntp_path (str | Path): _description_
        
        um_per_pixel (float, optional): 这里是最原始数据的分辨率，若意图影响最终大小，不要改这一条，通常来说时空组写 0.5，光学写 0.65/0.875/0.325. defaults to 0.65.
        
        bin_size (int, optional): 如果指定，应该与 w、h 同等次. Defaults to 1.
        
        verbose (bool, optional): _description_. Defaults to False.
        ignore_regions (list[str], optional): _description_. Defaults to ['region3','region4','mark4'].
        
        background_path (str, optional): _description_. Defaults to ''.
        
        export_position_policy (T_EXPORT_POSITION_POLICY, optional): _description_. Defaults to 'default'.
        
        w (int, optional): 如果指定，应该与 binsize 同等次. Defaults to 0.
        
        h (int, optional): 如果指定，应该与 binsize 同等次. Defaults to 0.
        
        return_bytes (bool, optional): _description_. Defaults to False.
        transpose (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    if verbose:
        logger.setLevel(logging.DEBUG)

    ntp_path = Path(ntp_path)
    ntp, w, h, size_source = prepare_ntp(
        ntp_path, um_per_pixel=um_per_pixel, bin_size=bin_size, 
        background_path=background_path, w=w, h=h, 
        transpose=transpose,
    )
    export_base_path = prepare_export_path(export_position_policy, ntp_path)

    raw_ntp_lines = fetch_ntp_lines(ntp.read_ntp_region_mark())
    ntp_lines = filter_ntp_lines(raw_ntp_lines, ignore_regions)
    raw_labels = ntp.read_labels()
    regions, warnings = lines_to_region(ntp_lines, raw_labels)

    cells = ntp.read_cells()

    res = SliceMeta(
        date=datetime.now(), 
        ntp_path=str(ntp_path),
        bin_size=bin_size,
        um_per_pixel=um_per_pixel,
        background_path=background_path,
        w=w, h=h,
        ignore_regions=ignore_regions,
        warnings=warnings,
        regions=regions,
        raw_labels=raw_labels,
        raw_lines=raw_ntp_lines,
        ntp_version=ntp.ntp_version,
        transpose=transpose,
        size_source=size_source,
        cells=cells,

        ntp_w=ntp.ntp_wh[0],
        ntp_h=ntp.ntp_wh[1],
        ntp_resolution=ntp.ntp_resolution,
    )
    if export_base_path is not None:
        (export_base_path / f'{ntp_path.stem}.json').write_bytes(
            orjson.dumps(res, default=geojson_default, option=orjson.OPT_INDENT_2 | orjson.OPT_SERIALIZE_NUMPY)
        )
    if __name__ != '__main__':
        if return_bytes:
            return orjson.dumps(res, default=geojson_default, option=orjson.OPT_SERIALIZE_NUMPY)
        else:
            return res


if __name__ == '__main__':
    fire.Fire(main)
