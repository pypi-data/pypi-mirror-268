from shapely.geometry import Polygon

from .constants import ESRI_DATA_TYPES
from .common import get_layer


def get_fields_aux(layer):
    """
    Returns a list of the fields of a layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be read
    
    Returns a list of tuples of type (name, alias, field type)
    """
    fields = layer.properties.fields
    condensed_fields = []

    for field in fields:
        name = field.name
        alias = field.alias
        field_type = ESRI_DATA_TYPES.get(field.type, field.type)
        condensed_fields.append((name, alias, field_type))

    return condensed_fields


def get_fields(gis, layer_id):
    """
    Returns a list of the fields of a layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
    
    Returns a list of tuples of type (name, alias, field type)
    """
    layer = get_layer(gis, layer_id)
    
    return get_fields_aux(layer)


def get_objectid_field_aux(layer):
    """
    Returns the name of the field that works as the objectID field
    
    Parameters:
        - layer: Layer Item of the structure looking to be read
    """
    fields = get_fields_aux(layer)
    
    for field in fields:
        if field[2] == "ObjectID":
            return field[0]
    
    raise Exception(f"Couldn't Find ObjectID Field Between Given Fields [{fields}]")


def get_objectid_field(gis, layer_id):
    """
    Returns the name of the field that works as the objectID field
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
    """
    layer = get_layer(gis, layer_id)
    
    return get_objectid_field_aux(layer)


def get_symbology_aux(layer):
    """
    Returns the symbology data of a given layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be read
    """
    return layer.properties.drawingInfo


def get_symbology(gis, layer_id):
    """
    Returns the symbology data of a given layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
    """
    layer = get_layer(gis, layer_id)
    
    return get_symbology_aux(layer)


def get_layer_crs_aux(layer):
    """
    Returns the spatial reference of a given layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be read
    """
    extent = layer.properties["extent"]

    spatial_reference = extent["spatialReference"]

    crs = spatial_reference["latestWkid"]

    return crs


def get_layer_crs(gis, layer_id):
    """
    Returns the spatial reference of a given layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
    """
    layer = get_layer(gis, layer_id)
    
    return get_layer_crs_aux(layer)


def get_layer_extent_aux(layer):
    """
    Returns the extent of a given layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be read
    """
    extent = layer.properties["extent"]

    min_x = extent["xmin"]
    max_x = extent["xmax"]
    min_y = extent["ymin"]
    max_y = extent["ymax"]

    polygon = Polygon([(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)])

    return polygon


def get_layer_extent(gis, layer_id):
    """
    Returns the extent of a given layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be read
    """
    layer = get_layer(gis, layer_id)
    
    return get_layer_extent_aux(layer)