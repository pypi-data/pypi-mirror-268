# Aeroterra Data Science

A python library with basic functions to ahieve your geospatial data science projects using the arcgis environment.


# Packages

The Library counts with different packages across its extension

## Layers

Created to handle arcgis layers, their information and metadata.

 - layers
	 - get_layer
	 - clone_layer
	 - create_layer
	 - add_to_layer
	 - update_layer
	 - empty_layer
	 - create_empty_gdf
	 - read_full_layer
	 - read_layer_gdf
 - fields
	 - add_field
	 - delete_field
	 - get_fields
	 - get_fields
	 - get_objectid_field
 - properties
	 - get_symbology
	 - get_layer_crs
	 - get_layer_extent

## Geometry

Created to handle geometries, in arcgis and shapely formats.
 - change_crs
	 - change_crs
 - geometry
     - get_arcgis_geometry
     - get_geo_json
