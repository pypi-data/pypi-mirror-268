from .common import get_layer
from .constants import ESRI_DATA_TYPES, PYTHON_DATA_TYPES

from .properties import get_fields_aux, get_fields, get_objectid_field

def create_field_dict(name, alias, data_type):
    """
    Given a name, alias and data_type it creates the dictionary of items needed
    for it to be a valid ESRIField Dictionary
    
    Parameters:
        - name: Name of the field looking to be created
        - alias: Alias of the field looking to be created
        - data_type: String representing the data type of the field
            looking to be created
    """
    field = {"nullable": True, "defaultValue": None, "editable": True, "domain": None}
    
    esri_type = PYTHON_DATA_TYPES.get(data_type)
    if esri_type is None and data_type not in ESRI_DATA_TYPES:
        raise Exception(f"{data_type} Is Not A Valid Data Type For ESRI")
    elif esri_type is None:
        esri_type = data_type
    
    field["modelName"] = name
    field["name"] = name
    field["alias"] = alias
    field["type"] = esri_type
    
    if esri_type == "esriFieldTypeString":
        field["length"] = 256
    
    return field


def field_present_layer(layer, field_name):
    """
    Checks if field_name is present in layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be read
        - field_name: Name of the field wanting to check if present.
    
    Returns a bool
    """
    fields = get_fields_aux(layer)
    for field in fields:
        if field[0] == field_name:
            return True
    
    return False


def add_field(gis, layer_id, name, data_type, alias=None):
    """
    Adds a field to the layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be modified
        - name: Name of the field looking to be created
        - data_type: String representing the data type of the field
            looking to be created
        - alias (Optional): Alias of the field looking to be created. If None,
            it'll be the same as name
    """    
    if alias is None:
        alias = name
    layer = get_layer(gis, layer_id)
    
    if field_present_layer(layer, name):
        raise Exception(f"Field {name} Already Exists")
    
    new_field = create_field_dict(name, alias, data_type)

    update_dict = {"fields": [new_field]}
    
    return layer.manager.add_to_definition(update_dict)


def delete_field(gis, layer_id, name):
    """
    Deletes a field from the layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be modified
        - name: Name of the field looking to be removed
    """    
    layer = get_layer(gis, layer_id)
    
    if not field_present_layer(layer, name):
        raise Exception(f"Field {name} Doesn't Exist")

    update_dict = {"fields": [{"name": name}]}
    
    return layer.manager.delete_from_definition(update_dict)