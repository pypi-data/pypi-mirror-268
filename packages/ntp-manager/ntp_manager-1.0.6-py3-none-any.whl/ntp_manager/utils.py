from functools import partial

import geojson
import orjson
from serde import from_dict as from_dict
from shapely.geometry.base import BaseGeometry, GeometrySequence


def geojson_default(obj):
    if isinstance(obj, BaseGeometry):
        return geojson.dumps(obj)
    if isinstance(obj, GeometrySequence):
        return [i for i in obj]
    raise TypeError

geo_dump = partial(
    orjson.dumps, default=geojson_default, 
    option=orjson.OPT_SERIALIZE_NUMPY
)
