import geopandas as gpd
import pandas as pd

from arcgis.features import GeoAccessor, FeatureSet
from arcgis.geometry.filters import intersects
#TODO: Remove GeoAccessor

from .common import get_layer, ordinal
from .properties import get_layer_crs_aux, get_objectid_field_aux, get_objectid_field_aux, get_fields_aux
from ..geometry.geometry import get_arcgis_geometry


def get_layer_in_list(layers_found, title):
    """
    Find Layer titled as title inside all the layers found
    
    Parameters:
        - layers_found: List of Items to check from
        - title: Title searched
    
    Returns None if not found, the item if found
    """
    for layer in layers_found:
        if layer.title == title:
            return layer
    
    return None


def change_gdf_to_layer_crs(gdf, layer):
    """
    Given a geodataframe it returns a new one with the crs of the given layer
    
    Parameters:
        - gdf: GeoDataFrame to change the crs
        - layer: Layer where to read the crs from
    
    Returns the sucess status of each add.
    """
    layer_crs = get_layer_crs_aux(layer)
    gdf_crs = gdf.crs
    if gdf_crs is None:
        raise Exception("GeoDataFrame Must Have A CRS Assigned")
    elif gdf_crs != layer_crs:
        new_gdf = gdf.to_crs(layer_crs, inplace=True)
    else:
        new_gdf = gdf.copy()
    
    return new_gdf


def clone_layer(og_gis, og_id, new_gis, new_name=None):
    """
    Copy the content from the layer with id og_id in the og_gis into a 
    new layer in the new_gis. The name will be conserved unless given a new one, 
    in case the name is already taken a versioning will be added to it.
    
    Parameters:
        - og_gis: GIS struct from an user that can read the original layer
        - og_id: id of the original layer
        - new_gis: GIS struct from the user that will own the new layer
        - new_name (Optional): Name to be assigned to the new layer, if None the
            original name will be conserved.
    
    Returns the new layer item.
    """
    try:
        old_item = og_gis.content.get(og_id)
        old_layer = old_item.layers[0]
    except:
        raise Exception(f"Couldn't find layer {og_id} For {og_gis}")
    
    layer_content = old_layer.query().sdf
    if len(layer_content) == 0:
        raise Exception("Can't Clone Empty Layer")
    
    title = old_item.title
    if new_name is None:
        new_name = title
    
    og_name = new_name
    names_matching = new_gis.content.search(f"title:{new_name}")
    i = 1
    while get_layer_in_list(names_matching, new_name) is not None:
        ord_i = ordinal(i)
        new_name = f"{og_name} ({ord_i} Copy)"
        names_matching = new_gis.content.search(f"title:{new_name}")
        i += 1
    
    new_layer = layer_content.spatial.to_featurelayer(title=new_name, gis=new_gis)  
    return new_layer


def create_layer(gdf, gis, title=None, folder=None):
    """
    Given a geodataframe it creates a feature layer with its data in a new item
    
    Parameters:
        - gdf: GeoDataFrame to publish
        - gis: GIS struct from the user that will own the new layer
        - title (Optional): Name to be given to the layer
        - folder (Optional): Folder in the portal where to store the layer
    
    Returns the new layer item.
    """
    sdf = GeoAccessor.from_geodataframe(gdf)
    
    layer = sdf.spatial.to_featurelayer(gis=gis, title=title, folder=folder)
    
    return layer


def add_to_layer(gdf, gis, layer_id):
    """
    Given a geodataframe it adds all its features to a layer
    
    Parameters:
        - gdf: GeoDataFrame to publish
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be modified
    
    Returns the sucess status of each add.
    """
    layer = get_layer(gis, layer_id)

    gdf = change_gdf_to_layer_crs(gdf, layer)
        
    sdf = GeoAccessor.from_geodataframe(gdf)
    return layer.edit_features(adds = sdf)


def update_layer(gdf, gis, layer_id, columns=None):
    """
    Given a geodataframe it updates the features asked in columns to a layer
    
    Parameters:
        - gdf: GeoDataFrame to publish
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be modified
        - columns(Optional): strings of the names of the columns to update. If None, all columns will be updated
    
    Returns the sucess status of each add.
    """
    layer = get_layer(gis, layer_id)
    object_id_col = get_objectid_field_aux(layer)

    if columns:
        if object_id_col not in columns:
            columns.append(object_id_col)
        gdf = gdf[columns]
    
    if object_id_col not in gdf.columns:
        raise Exception(f"{object_id_col} Must Be Present In GDF In Order To Know Which Line To Update")

    gdf = change_gdf_to_layer_crs(gdf, layer)
        
    sdf = GeoAccessor.from_geodataframe(gdf)
    feature_set = FeatureSet(sdf)
    return layer.edit_features(updates = feature_set)


def empty_layer(gis, layer_id):
    """
    Empty the data from a layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be emptied
    
    Returns the sucess status of each add.
    """
    layer = get_layer(gis, layer_id)
    
    return layer.manager.truncate()


def create_empty_gdf_aux(layer, crs=None):
    """
    Returns an empty geodataframe with the columns of a given layer
    
    Parameters:
        - layer: Layer Item of the structure looking to be copied
        - crs (Optional): CRS of the GeoDataFrame to be created. If None, 
            the one of the layer will be used
    """
    fields = get_fields_aux(layer)
    fields.append(("SHAPE", "SHAPE", "geometry"))

    columns = [field[0] for field in fields]
    if crs is None:
        crs = get_layer_crs_aux(layer)
    gdf = gpd.GeoDataFrame(columns=columns, geometry='SHAPE', crs=crs)
    for field in fields:
        col = field[1]
        dtype = field[2]
        if col == "SHAPE":
            continue

        try:
            gdf[col] = gdf[col].astype(dtype)
        except:
            continue

    return gdf


def create_empty_gdf(gis, layer_id, crs=None):
    """
    Returns an empty geodataframe with the columns of a given layer
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be emptied
        - crs (Optional): CRS of the GeoDataFrame to be created. If None, 
            the one of the layer will be used
    """
    layer = get_layer(gis, layer_id)
    
    return create_empty_gdf_aux(layer, crs)


def read_full_layer(gis, layer_id, out_crs=None):
    """
    Returns the full data stored in an asked layer.
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be asked
        - out_crs (Optional): Wanted CRS of the returned GeoDataFrame. If not
            loaded, it'll be returned in the one of the layer.

    Returns a GeoDataFrame
    """
    layer = get_layer(gis, layer_id)
    object_id_col = get_objectid_field_aux(layer)

    total_data = None
    if out_crs is None:
        out_crs = get_layer_crs_aux(layer)
    new_data = layer.query(out_sr=out_crs).sdf
    while len(new_data) > 0:
        if total_data is None:
            total_data = new_data.copy()
        else:
            total_data = pd.concat([total_data, new_data])

        last_time = new_data[object_id_col].max()
        new_where = f"{object_id_col} > {last_time}"
        new_data = layer.query(where = new_where, out_sr=out_crs).sdf

    if total_data is None:
        return create_empty_gdf_aux(layer, crs=out_crs)

    total_data = total_data.rename(columns = {"SHAPE": "geometry"})
    return gpd.GeoDataFrame(total_data, geometry="geometry", crs=out_crs)


def read_layer_gdf(gis, layer_id, number=None, query=None, geometry_filter=None, geometry_crs=4326, out_fields=None, out_crs=None):
    """
    Returns the full data stored in an asked layer.
    
    Parameters:
        - gis: GIS struct from the user that owns the layer
        - layer_id: Layer ID of the layer wanting to be asked
        - number (Optional): Layer Number inside the item. If not provided
            it'll be assumed the item should only have 1 layer
        - query (Optional): String representing a SQL query to filter the data to 
            to be read from the layer. If None, all the data will be providen.
        - geometry_filter (Optional): Shapely (Multi)Polygon to filter data geographically.
            If None, all the data will be providen.
        - geometry_crs (Optional): CRS of the given geometry_filer. If missing, 4326 will be assumed.
        - out_fields (Optional): List of fields names to recieve. If None, all will be returned.
        - out_crs (Optional): CRS of the returned gdf. If None, the crs of the layer will be used.


    Returns a GeoDataFrame
    """
    layer = get_layer(gis, layer_id, number)

    geo_filter = None
    if geometry_filter is not None:
        bounds = get_arcgis_geometry(geometry_filter, geometry_crs)
        geo_filter = intersects(bounds)

    if out_crs is None:
        out_crs = get_layer_crs_aux(layer)

    object_id_col = get_objectid_field_aux(layer)
    
    basic_where = query
    if out_fields is None:
       out_fields = "*"

    total_data = None
    new_data = layer.query(where = basic_where, geometry_filter=geo_filter, out_fields=out_fields, out_sr=out_crs).sdf
    while len(new_data) > 0:
        if total_data is None:
            total_data = new_data.copy()
        else:
            total_data = pd.concat([total_data, new_data])

        last_time = new_data[object_id_col].max()
        if query:
            new_where = basic_where + f" AND {object_id_col} > {last_time}"
        else:
            new_where = f"{object_id_col} > {last_time}"
        new_data = layer.query(where = new_where, geometry_filter=geo_filter, out_fields=out_fields, out_sr=out_crs).sdf

    if total_data is None:
        return create_empty_gdf_aux(layer)

    total_data = total_data.rename(columns = {"SHAPE": "geometry"})
    return gpd.GeoDataFrame(total_data, geometry="geometry", crs=out_crs)
