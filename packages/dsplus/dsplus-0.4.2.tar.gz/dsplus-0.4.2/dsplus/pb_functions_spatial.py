#region Libraries

#%%
import copy

from enum import Enum

import pandas as pd
import numpy as np

import geopandas as gpd
from shapely import geometry
from osgeo import gdal
import rasterio
import rasterstats as rs

import plotly.express as px

from .pb_functions_general import *
from .pb_functions_pandas import *

#endregion -----------------------------------------------------------------------------------------
#region Variables

#%%
class Options_epsg(Enum):
    wgs84 = 4326
    nad83_LA_north = 3451
    nad83_LA_south = 3452

#%%
class Options_px_basemap(Enum):
    carto_positron = 'carto-positron'
    carto_darkmatter = 'carto-darkmatter'
    satellite = 'mapbox-satellite'
    none = 'white-bg'
    open_street_map = 'open-street-map'
    satellite_esri = 'satellite_esri'
    satellite_usda = 'satellite_usda'
    satellite_national_map = 'satellite_national_map'

#%%
class Options_px_tiles(Enum):
    satellite_esri = 'https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
    satellite_usda = 'https://gis.apfo.usda.gov/arcgis/rest/services/NAIP/USDA_CONUS_PRIME/ImageServer/tile/{z}/{y}/{x}'
    satellite_national_map = 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}'

#endregion -----------------------------------------------------------------------------------------
#region Functions: Dataframe and sp Conversion

#%%
def sp_points_from_df_xy(df_xy: pd.DataFrame, column_x = 'x', column_y = 'y', crs = None) -> gpd.GeoDataFrame:
    '''Create points geodataframe.

    Args:
        df_xy (DataFrame): Dataframe with x and y columns.
        column_x (str): Name of column with x values. Defaults to 'x'.
        column_y (str): Name of column with y values. Defaults to 'y'.
        crs (any): CRS that can be assiged to gdf. Defaults to None.

    Returns:
        gpd.GeoDataFrame: Points geodataframe with all columns from df_xy and no crs.

    Examples:
        >>> sp_points = sp_points_from_df_xy(df)
        >>> sp_points = sp_points_from_df_xy(df, column_x='longitude', column_y='latitude', crs=4326)
    '''

    sp_points = gpd.GeoDataFrame(df_xy,
                                 geometry=gpd.points_from_xy(df_xy[column_x], df_xy[column_y]))

    if crs is not None:
        sp_points.crs = crs

    return (sp_points)

#%%
def sp_lines_from_df_xy(df_xy: pd.DataFrame, column_x = 'x', column_y = 'y', column_group: str = None, keep_columns = False, crs = None) -> gpd.GeoDataFrame:
    '''Create polylines geodataframe.

    Args:
        df_xy (DataFrame): Dataframe with x and y columns.
        column_x (str): Name of column with x values. Defaults to 'x'.
        column_y (str): Name of column with y values. Defaults to 'y'.
        column_group (str, optional): Column name to use as group. Defaults to None. If None, all points become one single polyline.
        keep_columns (bool): Whether to keep all columns from 'df_xy'. Defaults to False.
        crs (any): CRS that can be assiged to gdf. Defaults to None.

    Returns:
        gpd.GeoDataFrame: Polyline geodataframe without columns from df_xy and with no crs.

    Examples:
        >>> sp_lines = sp_lines_from_df_xy(df, column_group='group')
        >>> sp_lines = sp_lines_from_df_xy(df, column_group='group', keep_columns=True, column_x='longitude', column_y='latitude', crs=4326)
    '''
    sp_points = gpd.GeoDataFrame(df_xy,
                                 geometry=gpd.points_from_xy(df_xy[column_x], df_xy[column_y]))
    temp_group_column = copy.copy(column_group)
    if column_group is None:
        column_group = 'temp___group'
        sp_points = sp_points.assign(**{column_group: 1})
    sp_lines = \
        (sp_points
            .groupby(column_group)['geometry']
            .apply(lambda _: geometry.LineString(list(_)))
            .reset_index()
        )
    if temp_group_column is None:
        sp_lines = sp_lines.drop(column_group, axis=1)
    if keep_columns:
        if column_group is None:
            sp_lines = sp_lines.pipe(pd_concat_cols, df_xy.iloc[[0]], cols_drop = [column_x, column_y])
        else:
            df_xy = df_xy.groupby('index_info').head(1).reset_index(drop=True)
            sp_lines = sp_lines.merge(df_xy, how='left', on=column_group).drop([column_x, column_y], axis=1)

    if crs is not None:
        sp_lines.crs = crs

    return (sp_lines)

#%%
def sp_polygons_from_df_xy(df_xy: pd.DataFrame, column_x = 'x', column_y = 'y', column_group: str = None, keep_columns = False, crs = None) -> gpd.GeoDataFrame:
    '''Create polygons geodataframe.

    Args:
        df_xy (DataFrame): Dataframe with x and y columns.
        column_x (str): Name of column with x values. Defaults to 'x'.
        column_y (str): Name of column with y values. Defaults to 'y'.
        column_group (str, optional): Column name to use as group. Defaults to None. If None, all points become one single polygon. Starting and ending coordinates are joined by a closing line.
        keep_columns (bool): Whether to keep all columns from 'df_xy'. Defaults to False.
        crs (any): CRS that can be assiged to gdf. Defaults to None.

    Returns:
        gpd.GeoDataFrame: Polyline geodataframe without columns from df_xy and with no crs.

    Examples:
        >>> sp_polygons = sp_polygons_from_df_xy(df, column_group='group')
        >>> sp_polygons = sp_polygons_from_df_xy(df, column_group='group', keep_columns=True, column_x='longitude', column_y='latitude', crs=4326)
    '''
    sp_points = gpd.GeoDataFrame(df_xy,
                                 geometry=gpd.points_from_xy(df_xy[column_x], df_xy[column_y]))
    temp_group_column = copy.copy(column_group)
    if column_group is None:
        column_group = 'temp___group'
        sp_points = sp_points.assign(**{column_group: 1})
    sp_polygons = \
        (sp_points
            .groupby(column_group)['geometry']
            .apply(lambda _: geometry.Polygon(list(_)))
            .reset_index()
        )
    if temp_group_column is None:
        sp_polygons = sp_polygons.drop(column_group, axis=1)
    if keep_columns:
        if column_group is None:
            sp_polygons = sp_polygons.pipe(pd_concat_cols, df_xy.iloc[[0]], cols_drop = [column_x, column_y])
        else:
            df_xy = df_xy.groupby('index_info').head(1).reset_index(drop=True)
            sp_polygons = sp_polygons.merge(df_xy, how='left', on=column_group).drop([column_x, column_y], axis=1)

    if crs is not None:
        sp_polygons.crs = crs

    return (sp_polygons)

#%%
def sp_to_df_xy(sp: gpd.GeoDataFrame, explode:bool = True, cols_to_keep:str|list|np.ndarray|pd.Series = None, cols_keep_all:bool = False):
    '''Convert geodataframe to dataframe of x and y values.

    Args:
        sp (GeoDataFrame): Geodataframe.
        explode (bool, optional): Whether to explode geometry. Defaults to True
        cols_to_keep (str | list | np.ndarray | pd.Series, optional): Vector of columns to keep from 'sp'. Defaults to None.
        cols_keep_all (bool, optional): Whether to keep all columns from 'sp'. Defaults to False.

    Returns:
        pd.DataFrame: Dataframe with columns: 'id_geom' indicating individual geometry parts, 'id_sp' indicating index of 'sp', 'id_part' indicating individual geometry parts for each index of 'sp', 'x' indicating x-coordinates, and 'y' indicating y-coordinates. Other columns from 'sp' may be included.

    Notes:
        - 'id_geom' is f'{id_sp}__{id_part}' and is unique.
        - If all geometry are singlepart, each entry in 'id' will be unique, and 'id_part' will all be 0.
        - For a multipart geometry, 'id_sp' will be the same, and 'id_part' will be unique.
        - If 'cols_keep_all' is True, 'cols_to_keep' is ignored.

    Examples:
        >>> sp_to_df_xy(sp_points)
        >>> sp_to_df_xy(sp_lines)
        >>> sp_to_df_xy(sp_polygons)
        >>> sp_to_df_xy(sp_points, cols_to_keep='City')
        >>> sp_to_df_xy(sp_points, cols_to_keep=['City', 'Country'])
        >>> sp_to_df_xy(sp_points, cols_keep_all=True)
    '''
    # df_xy = \
    #     (sp
    #         .explode(index_parts=True)
    #         .get_coordinates()
    #         .reset_index()
    #         .rename(columns={'level_0': 'index',
    #                         'level_1': 'index_part'})
    #         .assign(id_geom=lambda _: str_concat(_['index'], '__', _['index_part']))
    #         .pipe(pd_select_simple, 'id_geom')
    #     )
    cols_to_keep_extra = None
    if explode:
        sp = sp_explode(sp)
        cols_to_keep_extra = ['id_geom', 'id_sp', 'id_part']
        cols_to_keep = set_union(cols_to_keep, cols_to_keep_extra)
    df_xy = \
        (sp
            .get_coordinates()
            .reset_index()
        )

    if cols_keep_all:
        cols_to_keep = sp.drop(columns='geometry').columns
    if cols_to_keep is not None:
        cols_to_keep = pd_to_series(cols_to_keep)

        df_xy = df_xy.merge(sp[cols_to_keep].reset_index(), on='index')

    if cols_to_keep_extra is not None:
        df_xy = df_xy.pipe(pd_select_simple, ['index', *cols_to_keep_extra])
    return df_xy

#endregion -----------------------------------------------------------------------------------------
#region Functions: Chainage

#%%
def sp_get_chainage(sp_line: gpd.GeoDataFrame, sp_points: gpd.GeoDataFrame, return_series=True):
    '''Get chainage of points on a polyline.

    Args:
        sp_line (GeoDataFrame): Polyline geodataframe.
        sp_points (GeoDataFrame): Points geodataframe.
        return_series (bool, optional): Return series (if True) or list (if False). Defaults to True.

    Returns:
        pd.Series | List of float: Series or list of chainages. Same unit as geodataframe.
    '''
    chainage = [sp_line.geometry.iloc[0].project(sp_point) for sp_point in sp_points.geometry]
    # chainage = [sp_line.geometry.project(sp_point).iloc[0] for sp_point in sp_points.geometry]
    if return_series:
        return (pd.Series(chainage))
    else:
        return (chainage)

#%%
def sp_get_chainage_from_df_xy(df_xy: pd.DataFrame):
    '''Get chainage from dataframe.

    Args:
        df_xy (DataFrame): Dataframe with 'x' and 'y' columns.

    Returns:
        pd.DataFrame: dataframe with two appended columns: 'dist' (distance from previous point) and 'chainage' (chainage from first point).
    '''
    df_chainage = \
        (df_xy
            .assign(diff_x = lambda _: _['x'].diff().fillna(0))
            .assign(diff_y = lambda _: _['y'].diff().fillna(0))
            .assign(dist = lambda _: np.sqrt(_['diff_x']**2 + _['diff_y']**2))
            .assign(chainage = lambda _: _['dist'].cumsum())
            .drop(['diff_x', 'diff_y'], axis=1)
        )

    return (df_chainage)

#endregion -----------------------------------------------------------------------------------------
#region Functions: Zonal Stats

#%%
def sp_zonal_stats_points(sp_points: gpd.GeoDataFrame, files_raster: str|list|np.ndarray|pd.Series, col_names: str|list|np.ndarray|pd.Series = None, id_cols: str|list|np.ndarray|pd.Series = None) -> pd.Series|pd.DataFrame:
    '''Get raster values at points.

    Args:
        sp_points (GeoDataFrame): Geodataframe of points.
        files_raster (str | list | np.ndarray | pd.Series of str): Vector of raster file(s).
        col_names (str | list | np.ndarray | pd.Series): Vector of column names. Should be same length as 'files_raster'. Defaults to None.
        id_cols (str | list | np.ndarray | pd.Series): Vector of columns from 'sp_poly' to append to results. Only useful when 'files_raster' is not str. Defaults to None.

    Returns:
        pd.Series | pd.DataFrame: The raster values at points.

    Notes:
        - If 'files_raster' is a string, a series of raster values is returned in same order 'sp_points'.
        - If 'files_raster' is a vector, a dataframe of raster values is returned. The rows indicate the features in 'sp_points' in order. The columns indicate the 'files_raster' in order.

    Examples:
        >>> sp_zonal_stats_points(sp_points, files_rasters[0])
        >>> sp_zonal_stats_points(sp_points, files_rasters, id_cols='name', col_names=os_basename(files_raster, keep_extension=False))
    '''
    df_xy = sp_points.geometry.get_coordinates()
    coords = [(x,y) for x, y in zip(df_xy.x, df_xy.y)]

    if isinstance(files_raster, str):
        with rasterio.open(files_raster) as f:
            temp_values = [val[0] for val in f.sample(coords)]
        temp_values = pd.Series(temp_values)

        return (temp_values)
    else:
        df_values = []
        for file_raster in files_raster:
            with rasterio.open(file_raster) as f:
                df_values.append([val[0] for val in f.sample(coords)])
        df_values = pd.DataFrame(df_values).T

        if col_names is not None:
            df_values = df_values.pipe(pd_set_colnames, col_names)

        if id_cols is not None:
            id_cols = pd_to_series(id_cols)
            df_values = df_values.pipe(pd_concat_cols, sp_points.loc[:, id_cols]).pipe(pd_select_simple, id_cols.tolist())

        return (df_values)

#%%
def sp_zonal_stats_line(sp_lines: gpd.GeoDataFrame, files_raster: str|list|np.ndarray|pd.Series, spacing: float, id_cols: str|list|np.ndarray|pd.Series = None, files_raster_mapped: str|list|np.ndarray|pd.Series = None, filename_colname = 'file', smoothen_span: float = None) -> pd.DataFrame:
    '''Get raster values at lines. Values are sampled at start and end point and points in-between separated by provided 'spacing'.

    Args:
        sp_lines (GeoDataFrame): Geodataframe of lines.
        files_raster (str | list | np.ndarray | pd.Series): Vector of raster file(s).
        spacing (float): Spacing along line to sample raster values at.
        id_cols (str | list | np.ndarray | pd.Series): Vector of columns from 'sp_lines' to append to results. Defaults to None.
        files_raster_mapped (str | list | np.ndarray | pd.Series): Vector of proxies for 'files_raster'. Should be same length as 'files_raster'. Only comes into play when 'files_raster' is not None. Defaults to None.
        filename_colname (str): Name of column that indicates the corresponding raster file. Only comes into play when 'files_raster' is not None. Defaults to 'file'.
        smoothen_span (float, optional): Proportion of number of points for local weighted smoothing. Defaults to None. No smoothing is done if set to None.

    Returns:
        pd.DataFrame: The raster values at each sampled point.

    Examples:
        >>> sp_zonal_stats_line(sp_roads, files_raster[0], spacing=500)
        >>> sp_zonal_stats_line(sp_roads, [files_raster[0]], spacing=500)
        >>> sp_zonal_stats_line(sp_roads, files_raster, spacing=500)
        >>> sp_zonal_stats_line(sp_roads,
                                files_raster,
                                spacing=500,
                                id_cols='FULLNAME',
                                files_raster_mapped=os_basename(files_raster))
    '''
    files_raster_is_str = True if isinstance(files_raster, str) else False

    files_raster = pd_to_series(files_raster)
    if files_raster_mapped is None:
        files_raster_mapped = pd_to_series(files_raster)

    df_profile = pd.DataFrame()
    for i in np.arange(0, sp_lines.shape[0]):
        sp_line = sp_lines.iloc[[i]]
        sp_points = sp_get_points_along_line(sp_line, spacing = spacing)

        for j, file_raster in enumerate(files_raster):
            sp_points = sp_points.assign(elev = sp_zonal_stats_points(sp_points, file_raster))

            temp_df_profile = sp_points.pipe(pd_drop, 'geometry')

            if smoothen_span is not None:
                # window_length = int(np.round(temp_df_profile.shape[0]*smoothen_span))
                # temp_df_profile = temp_df_profile.assign(elev_sm = lambda _: savgol_filter(_['elev'], window_length, 2))
                temp_df_profile = temp_df_profile.assign(elev_sm = lambda _: smoothen_line(_['elev'], window_count=smoothen_span))

            if not files_raster_is_str:
                temp_df_profile = temp_df_profile.assign(**{filename_colname: files_raster_mapped[j]})

            if id_cols is not None:
                id_cols = pd_to_series(id_cols)

                temp_df = sp_line[id_cols].reset_index(drop=True)
                temp_df = temp_df.loc[temp_df.index.repeat(temp_df_profile.shape[0])]

                temp_df_profile = temp_df_profile.pipe(pd_concat_cols, temp_df)

            df_profile = df_profile.pipe(pd_concat_rows, temp_df_profile)

    if files_raster_is_str:
        df_profile = df_profile.pipe(pd_select_simple, id_cols)
    else:
        df_profile = df_profile.pipe(pd_select_simple, filename_colname).pipe(pd_select_simple, id_cols)

    return (df_profile)


#%%
def sp_zonal_stats_poly(sp_poly: gpd.GeoDataFrame, files_raster: str|list|np.ndarray|pd.Series, stats: str|list=['min', 'max', 'mean', 'sum', 'median', 'majority'], id_cols: str|list|np.ndarray|pd.Series = None, files_raster_mapped: str|list|np.ndarray|pd.Series = None, filename_colname = 'file') -> pd.Series|pd.DataFrame|dict:
    '''Get raster value summaries at polygons.

    Args:
        sp_poly (GeoDataFrame): Geodataframe of polygons.
        files_raster (str | list | np.ndarray | pd.Series): Vector of raster file(s)
        stats (str | list of str): Stat to use. Defaults to ['min', 'max', 'mean', 'sum', 'median', 'majority']. Acceptable values for the list are: 'sum', 'std', 'median', 'majority', 'minority', 'unique', 'range', 'nodata', 'percentile'. Percentile statistic can be used by specifying 'percentile_<q>' where <q> can be a floating point number between 0 and 100.
        id_cols (str | list | np.ndarray | pd.Series): Vector of columns from 'sp_poly' to append to results. Doesn't come into play if both 'files_raster' and 'stats' are str. Defaults to None.
        files_raster_mapped (str | list | np.ndarray | pd.Series): Vector of proxies for 'files_raster'. Should be same length as 'files_raster'. Defaults to None.
        filename_colname (str): Name of column that indicates the corresponding raster file. Only comes into play when 'files_raster' and 'stats' are both not str. Defalts to 'file'.

    Returns:
        pd.Series | pd.DataFrame | dict: The summary of raster values by specified statistics at each polygon.

    Notes:
        - If 'files_raster' is a string and 'stats' is a string, a series of raster values is returned in same order 'sp_poly'.
        - If 'files_raster' is a vector and 'stats' is a string, a dataframe of raster values is returned. The rows indicate the 'sp_poly' in order. The columns indicate the 'files_raster' in order.
        - If 'files_raster' is a string and 'stats' is a vector, a dataframe of raster values is returned. The rows indicate the 'sp_poly' in order. The columns indicate the 'stats' in order. 'files_raster_mapped' is used as column names if not None.
        - If 'files_raster' is a vector and 'stats' is a vector, a dataframe of raster values is returned. Each item is a dictionary corresponding to the raster value for each file in order. The rows indicate 'sp_poly' in order. The columns indicate the 'stats' in order. An additional column, 'filename_colname' indicates the corresponding raster file. 'files_raster_mapped' used instead of filenames if it's not None.

    Examples:
        >>> sp_zonal_stats_poly(sp_poly,
                                files_rasters[0],
                                stats = 'sum')
        >>> sp_zonal_stats_poly(sp_poly,
                                files_rasters[0],
                                stats = ['sum'],
                                id_cols = 'name')
        >>> sp_zonal_stats_poly(sp_poly,
                                files_rasters[0],
                                stats = ['sum', 'mean'],
                                id_cols = 'name',
                                files_raster_mapped=os_basename(files_raster, keep_extension=False))
        >>> sp_zonal_stats_poly(sp_poly,
                                files_rasters,
                                stats = 'mean',
                                id_cols = 'name',
                                files_raster_mapped=os_basename(files_raster, keep_extension=False))
        >>> sp_zonal_stats_poly(sp_poly,
                                files_rasters,
                                stats = ['mean'],
                                id_cols = 'name',
                                filename_colname='type',
                                files_raster_mapped=os_basename(files_raster, keep_extension=False))
        >>> sp_zonal_stats_poly(sp_poly,
                                files_rasters,
                                stats = ['sum', 'mean'],
                                id_cols = 'name',
                                filename_colname='type',
                                files_raster_mapped=os_basename(files_raster, keep_extension=False))
    '''
    if isinstance(files_raster, str):
        if isinstance(stats, str):
            v_values = rs.zonal_stats(sp_poly, files_raster, stats=[stats])
            v_values = pd.DataFrame(v_values).iloc[:, 0]

            return (v_values)
        else:
            df_values = rs.zonal_stats(sp_poly, files_raster, stats=stats)
            df_values = pd.DataFrame(df_values)

            if id_cols is not None:
                id_cols = pd_to_series(id_cols)
                df_values = df_values.pipe(pd_concat_cols, sp_poly.loc[:, id_cols]).pipe(pd_select_simple, id_cols.tolist())

            return (df_values)
    else:
        if files_raster_mapped is not None:
            files_raster_mapped = pd_to_series(files_raster_mapped)
        if isinstance(stats, str):
            df_values = []
            for file_raster in files_raster:
                temp_values = rs.zonal_stats(sp_poly, file_raster, stats=[stats])
                temp_values = pd.DataFrame(temp_values).iloc[:, 0]
                df_values.append(temp_values.to_list())
            df_values = pd.DataFrame(df_values).T

            if files_raster_mapped is not None:
                df_values = df_values.pipe(pd_set_colnames, files_raster_mapped)

            if id_cols is not None:
                id_cols = pd_to_series(id_cols)
                df_values = df_values.pipe(pd_concat_cols, sp_poly.loc[:, id_cols]).pipe(pd_select_simple, id_cols.tolist())

            return (df_values)
        else:
            df_values = pd.DataFrame()
            for i, file_raster in enumerate(files_raster):
                if files_raster_mapped is not None:
                    file_raster_mapped = files_raster_mapped.iloc[i]
                else:
                    file_raster_mapped = file_raster
                temp_df_values = rs.zonal_stats(sp_poly, file_raster, stats=stats)
                temp_df_values = pd.DataFrame(temp_df_values).assign(**{filename_colname: file_raster_mapped})

                if id_cols is not None:
                    id_cols = pd_to_series(id_cols)
                    temp_df_values = temp_df_values.pipe(pd_concat_cols, sp_poly.loc[:, id_cols]).pipe(pd_select_simple, id_cols.tolist())

                df_values = df_values.pipe(pd_concat_rows, temp_df_values)

            return (df_values)

#endregion -----------------------------------------------------------------------------------------
#region Functions: Plotly

#TODO Documentation

#%%
def px_sp_create_map(sp = None, center_lon=-95.7129, center_lat=37.0902, zoom=2.5, **kwargs):
    if sp is not None:
        if sp.crs.to_epsg() != Options_epsg.wgs84.value:
            sp = sp.to_crs(Options_epsg.wgs84.value)

        temp_centroid = gpd.GeoDataFrame(geometry=sp.centroid)
        center_lon = temp_centroid.geometry.x.mean()
        center_lat = temp_centroid.geometry.y.mean()
        # temp_bounds = sp.bounds
        # temp_del_x = temp_bounds['maxx'].max() - temp_bounds['minx'].min()
        # temp_del_y = temp_bounds['maxy'].max() - temp_bounds['miny'].min()
        # zoom_x = 360/temp_del_x
        # zoom_y = 180/temp_del_y
    fig = px.choropleth_mapbox(center=dict(lon=center_lon,
                                           lat=center_lat),
                               zoom=zoom,
                               **kwargs)
    return fig

#%%
def px_add_trace_data(fig_original, *figs):
    # TODO not working (only takes first fig)
    for fig in figs:
        for i in range(len(fig.data)):
            fig_original.add_trace(fig.data[i])
        return fig_original

#%%
def px_sp_basemap(fig, basemap):
    if pd.Series(dir(Options_px_tiles)).str.contains(basemap).any():
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": "traces",
                    "sourcetype": "raster",
                    # "sourceattribution": "United States Geological Survey",
                    "source": [Options_px_tiles[basemap].value],
                }
            ],
        )
    else:
        fig.update_layout(mapbox_style=basemap)

#%%
def px_sp_points(sp_points,
                 color_value = None,
                 size_value = None,
                 symbol_value = None,
                 legend_name = None,
                 hover_skip = False,
                 update_crs = True,
                 **kwargs):
    if update_crs:
        if sp_points.crs.to_epsg() != Options_epsg.wgs84.value:
            sp_points = sp_points.to_crs(Options_epsg.wgs84.value)
    fig = px.scatter_mapbox(sp_points,
                            lon=sp_points.geometry.x,
                            lat=sp_points.geometry.y,
                            **kwargs)
    if color_value is not None:
        fig = fig\
            .update_traces(marker=dict(color=color_value))
    if size_value is not None:
        fig = fig\
            .update_traces(marker=dict(size=size_value))
    if symbol_value is not None:
        fig = fig\
            .update_traces(marker=dict(symbol=symbol_value))
    if legend_name is not None:
        if ('color' not in kwargs) and ('size' not in kwargs):
            fig = fig\
                .update_traces(name=legend_name,
                               showlegend=True)
        else:
            fig = fig\
                .update_traces(legendgroup=legend_name,
                               legendgrouptitle_text=legend_name,
                               showlegend=True)
    if hover_skip:
        fig = fig\
            .update_traces(hoverinfo='skip',
                           hovertemplate=None)
    return fig

#%%
def px_sp_polylines(sp_lines,
                    color_value = None,
                    width_value = None,
                    dash_value = None,
                    legend_name = None,
                    hover_skip = False,
                    update_crs = True,
                    **kwargs):
    if update_crs:
        if sp_lines.crs.to_epsg() != Options_epsg.wgs84.value:
            sp_lines = sp_lines.to_crs(Options_epsg.wgs84.value)
    df_lines_xy = sp_to_df_xy(sp_lines, cols_keep_all=True)
    fig = px.line_mapbox(df_lines_xy,
                         lon=df_lines_xy['x'],
                         lat=df_lines_xy['y'],
                         line_group=df_lines_xy['id_geom'],
                         **kwargs)
    if color_value is not None:
        fig = fig\
            .update_traces(line=dict(color=color_value))
    if width_value is not None:
        fig = fig\
            .update_traces(line=dict(width=width_value))
    if dash_value is not None:
        fig = fig\
            .update_traces(line=dict(dash=dash_value))
    if legend_name is not None:
        if 'color' not in kwargs:
            fig = fig\
                .update_traces(name=legend_name,
                               legendgroup=legend_name,
                               showlegend=True)
        else:
            fig = fig\
                .update_traces(legendgroup=legend_name,
                               legendgrouptitle_text=legend_name,
                               showlegend=True)
    if 'color' not in kwargs:
        for i in range(len(fig.data)):
            if i == 0:
                fig.data[i].showlegend = True
            else:
                fig.data[i].showlegend = False
    if hover_skip:
        fig = fig\
            .update_traces(hoverinfo='skip',
                           hovertemplate=None)
    return fig

#%%
def px_sp_polygons(sp_polygons,
                   color_value = None,
                   line_color = None,
                   line_width = None,
                   line_dash = None,
                   legend_name = None,
                   hover_skip = False,
                   update_crs = True,
                   **kwargs):
    if update_crs:
        if sp_polygons.crs.to_epsg() != Options_epsg.wgs84.value:
            sp_polygons = sp_polygons.to_crs(Options_epsg.wgs84.value)
    if color_value is not None:
        kwargs['color_discrete_sequence'] = [color_value, color_value]
    fig = px.choropleth_mapbox(sp_polygons,
                               locations=sp_polygons.index,
                               geojson=sp_polygons.geometry,
                               **kwargs)
    if line_color is not None:
        fig = fig\
            .update_traces(marker=dict(line=dict(color=line_color)))
    if line_width is not None:
        fig = fig\
            .update_traces(marker=dict(line=dict(width=line_width)))
    if line_dash is not None:
        fig = fig\
            .update_traces(marker=dict(line=dict(dash=line_dash)))
    if legend_name is not None:
        if 'color' not in kwargs:
            fig = fig\
                .update_traces(name=legend_name,
                               legendgroup=legend_name,
                               showlegend=True)
        else:
            fig = fig\
                .update_traces(legendgroup=legend_name,
                               legendgrouptitle_text=legend_name,
                               showlegend=True)
    if hover_skip:
        fig = fig\
            .update_traces(hoverinfo='skip',
                           hovertemplate=None)
    return fig

#%%
def px_sp_polygon_borders(sp_polygons,
                          line_color = None,
                          line_width = None,
                          line_dash = None,
                          legend_name = None,
                          hover_skip = True,
                          update_crs = True,
                          **kwargs):
    if update_crs:
        if sp_polygons.crs.to_epsg() != Options_epsg.wgs84.value:
            sp_polygons = sp_polygons.to_crs(Options_epsg.wgs84.value)
    df_polygons_xy = sp_to_df_xy(sp_polygons, cols_keep_all=True)
    fig = px.line_mapbox(df_polygons_xy,
                         lon=df_polygons_xy['x'],
                         lat=df_polygons_xy['y'],
                         line_group=df_polygons_xy['id_geom'])
    if line_color is not None:
        fig = fig\
            .update_traces(line=dict(color=line_color))
    if line_width is not None:
        fig = fig\
            .update_traces(line=dict(width=line_width))
    if line_dash is not None:
        fig = fig\
            .update_traces(line=dict(dash=line_dash))
    if legend_name is not None:
        if 'color' not in kwargs:
            fig = fig\
                .update_traces(name=legend_name,
                               legendgroup=legend_name,
                               showlegend=True)
        else:
            fig = fig\
                .update_traces(legendgroup=legend_name,
                               legendgrouptitle_text=legend_name,
                               showlegend=True)
    if 'color' not in kwargs:
        for i in range(len(fig.data)):
            if i == 0:
                fig.data[i].showlegend = True
            else:
                fig.data[i].showlegend = False
    if hover_skip:
        fig = fig\
            .update_traces(hoverinfo='skip',
                           hovertemplate=None)
    return fig

#endregion -----------------------------------------------------------------------------------------
#region Functions: Others

#%%
def sp_explode(sp: gpd.GeoDataFrame):
    '''Explodes geodataframe.

    Args:
        sp (GeoDataFrame): Geodataframe.

    Returns:
        pd.DataFrame: Exploded geodataframe with additional columns: 'id_geom' indicating individual geometry parts, 'id_sp' indicating index of 'sp', and 'id_part' indicating individual geometry parts for each index of 'sp'.

    Notes:
        - 'id_geom' is f'{id_sp}__{id_part}' and is unique.
        - If all geometry are singlepart, each entry in 'id' will be unique, and 'id_part' will all be 0.
        - For a multipart geometry, 'id_sp' will be the same, and 'id_part' will be unique.

    Examples:
        >>> sp_explode(sp_points)
    '''
    sp_exploded = \
        (sp
            .explode(index_parts=True)
            .reset_index()
            .rename(columns={'level_0': 'id_sp',
                            'level_1': 'id_part'})
            .assign(id_geom=lambda _: str_concat(_['id_sp'], '__', _['id_part']))
            .pipe(pd_select_simple, 'id_geom')
        )

    return sp_exploded

#%%
def sp_get_points_along_line(sp_line: gpd.GeoDataFrame, v_distances_normalized: list|np.ndarray|pd.Series=None, count: int=None, spacing: float=None, spacing_normalized: float=None, include_ends=True) -> gpd.GeoDataFrame:
    '''Generate points along polyline.

    Args:
        sp_line (GeoDataFrame): Geodataframe with single polyline feature.
        v_distances (list | np.ndarray | pd.Series of float, optional): Vector of normalized distances ([0, 1]). Defaults to None. 0 means start of line and 1 means end.
        count (int, optional): Number of points to generate. Defaults to None.
        spacing (float, optional): Spacing between each point in absolute units. Defaults to None.
        spacing_normalized (float, optional): Spacing between each point in relative units ([0, 1]). Defaults to None.
        include_ends (bool, optional): Indicates where points at the ends (start and end) need to be included. Defaults to True. Overridden when 'v_distances_normalized' is used.

    Returns:
        gpd.GeoDataFrame: Geodataframe of points. The geodataframe has two columns: 'chainage_normalized' and 'chainage', listing normalized chainages and absolute chainages for each point.

    Notes:
        - Only one of 'v_distances_normalized', 'spacing', 'spacing_normalized', and 'count' should be defined.
        - Priority order: 'v_distances_normalized' > 'spacing' > 'spacing_normalized' > 'count'.
        - 'include_ends' is overridden if 'v_distances_normalized' is used. Include 0 and 1 in 'v_distances_normalized' if ends are to be included.
        - 'include_ends = True' results in 'count' and not ('count' + 2) points if 'count' is used.
        - 'spacing' and 'spacing_normlized' start spacing form the starting point, so the spacing at the end might be smaller than specified.

    Examples:
        >>> sp_get_points_along_line(temp_sp_line, v_distances_normalized=[0,0.1,0.5,0.75,1])
        >>> sp_get_points_along_line(temp_sp_line, count=10, include_ends=False)
        >>> sp_get_points_along_line(temp_sp_line, spacing_normalized=0.3)
        >>> sp_get_points_along_line(temp_sp_line, spacing=1, include_ends=True)
    '''
    temp_length = sp_line.length
    if v_distances_normalized is None:
        if count is not None:
            if include_ends:
                v_distances_normalized = np.linspace(0,1,count)
            else:
                v_distances_normalized = np.linspace(0,1,count+2)
                v_distances_normalized = v_distances_normalized[1:len(v_distances_normalized)-1]
        if spacing is not None:
            spacing_normalized = spacing/temp_length.iloc[0]
        if spacing_normalized is not None:
            if include_ends:
                v_distances_normalized = np.append(np.arange(0,1,spacing_normalized), 1)
            else:
                v_distances_normalized = np.arange(spacing_normalized,1,spacing_normalized)
    v_distances_normalized = np.array(v_distances_normalized)
    sp_points = gpd.GeoDataFrame.from_features(gpd.GeoSeries([sp_line.geometry.iloc[0].interpolate(distance, normalized=True) for distance in v_distances_normalized]))
    sp_points = sp_points.eval('chainage_normalized = @v_distances_normalized').assign(chainage = lambda _: _['chainage_normalized']*temp_length.iloc[0])

    return (sp_points)

#%%
def sp_offset_line_poly(sp: gpd.GeoDataFrame, distance: float, join_style='mitre'):
    '''Offset polyline or polygon.

    Args:
        sp (GeoDataFrame): Polyline or polygon geodataframe with single feature.
        distance (numeric): Distance to offset by. Same unit as gdf. Positive means offset left. Direction is determined by following the direction of the given geometric points.
        join_style (str, optional): Join style for corners between line segments. Acceptable values are 'round' (rounded corner), 'mitre' (sharp corner), and 'bevel' (bevelled corner). Defaults to 'mitre'.

    Returns:
        gpd.GeoDataFrame: Polyline or polygon geodataframe with offsetted feature.
    '''
    return (gpd.GeoDataFrame.from_features(gpd.GeoSeries([sp.geometry.iloc[0].offset_curve(distance, join_style=join_style)])))

#endregion -----------------------------------------------------------------------------------------
#region Archive

#%%
# options_epsg = dict(wgs84 = 4326, nad83_LA_north = 3451, nad83_LA_south = 3452)
# class Options_epsg:
#     wgs84 = 4326
#     nad83_LA_north = 3451
#     nad83_LA_south = 3452

# #%%
# def zonal_stats_poly_multiple(sp_poly: gpd.GeoDataFrame, file_raster: str=None, files_raster: list|np.ndarray|pd.Series=None, stats=['min', 'max', 'mean', 'sum', 'median', 'majority']):
#     '''Get raster value summaries at polygons.

#     Args:
#         sp_poly (GeoDataFrame): Geodataframe of polygons.
#         file_raster (str, optional): Raster file. Defaults to None.
#         stats (list of str): Stat to use. Defaults to ['min', 'max', 'mean', 'sum', 'median', 'majority']. Acceptable values for the list are: 'sum', 'std', 'median', 'majority', 'minority', 'unique', 'range', 'nodata', 'percentile'. Percentile statistic can be used by specifying 'percentile_<q>' where <q> can be a floating point number between 0 and 100.

#     Returns:
#         pd.DataFrame: The summary of raster values by specified statistics at each polygon.

#     Notes:
#         - Only one of file_raster or files_raster need to be specified.
#         - The columns indicate the 'stats' in order. The rows indicate the 'sp_poly' in order.

#     Examples:
#         >>> zonal_stats_poly(sp_points, files_raster_tif[0], stats = 'median')
#         >>> zonal_stats_poly(sp_points, files_raster_tif[0], stats = ['sum', 'mean']).assign(id = sp_points['id'])
#     '''
#     if files_raster is None:
#         df_values = rs.zonal_stats(sp_poly, file_raster, stats=stats)
#         df_values = pd.DataFrame(df_values)

#         return (df_values)
#     else:
#         d_values = dict()
#         for file_raster in files_raster:
#             df_values = rs.zonal_stats(sp_poly, file_raster, stats=stats)
#             df_values = pd.DataFrame(df_values)

#             d_values[file_raster] = df_values

#         return (d_values)

# #%%
# def zonal_stats_poly_single(sp_poly: gpd.GeoDataFrame, file_raster: str=None, files_raster: list|np.ndarray|pd.Series=None, stats='sum'):
#     '''Get raster value summary at polygons.

#     Args:
#         sp_poly (GeoDataFrame): Geodataframe of polygons.
#         file_raster (str, optional): Raster file. Defaults to None.
#         files_raster (list | np.ndarray | pd.Series of str, optional): Vector of raster files. Defaults to None.
#         stats (str): Stat to use. Defaults to 'sum'. Acceptable values are: 'sum', 'std', 'median', 'majority', 'minority', 'unique', 'range', 'nodata', 'percentile'. Percentile statistic can be used by specifying 'percentile_<q>' where <q> can be a floating point number between 0 and 100.

#     Returns:
#         pd.Series | pd.DataFrame: The summary of raster values by specified statistics at each polygon.

#     Notes:
#         - Only one of file_raster or files_raster need to be specified.
#         - If 'file_raster' is used, a series of raster values is returned in same order 'sp_poly'.
#         - If 'files_raster' is used, a dataframe of raster values is returned. The columns indicate the 'sp_poly' in order. The row indicate the 'files_raster' in order.

#     Examples:
#         >>> zonal_stats_poly_single(sp_points, files_raster_tif[0], stats = 'median')
#         >>> zonal_stats_poly_single(sp_points, files_raster=files_raster_tif, stats = 'median').set_axis(sp_points['id'], axis = 1).assign(file = os.path.basename(files_raster_tif)
#     '''
#     if files_raster is None:
#         temp_values = rs.zonal_stats(sp_poly, file_raster, stats=[stats])
#         temp_values = pd.DataFrame(temp_values).iloc[:, 0]

#         return (temp_values)

#     else:
#         df_values = []
#         for file_raster in files_raster:
#             temp_values = rs.zonal_stats(sp_poly, file_raster, stats=[stats])
#             temp_values = pd.DataFrame(temp_values).iloc[:, 0]
#             df_values.append(temp_values.to_list())
#         df_values = pd.DataFrame(df_values)

#         return (df_values)

# #%%
# def zonal_stats_points(sp_points: gpd.GeoDataFrame, file_raster: str=None, files_raster: list|np.ndarray|pd.Series=None) -> pd.Series|pd.DataFrame:
#     '''Get raster values at points.

#     Args:
#         sp_points (GeoDataFrame): Geodataframe of points.
#         file_raster (str, optional): Raster file. Defaults to None.
#         files_raster (list | np.ndarray | pd.Series of str, optional): Vector of raster files. Defaults to None.

#     Returns:
#         pd.Series | pd.DataFrame: The raster values at points.

#     Notes:
#         - Only one of file_raster or files_raster need to be specified.
#         - If 'file_raster' is used, a series of raster values is returned in same order 'sp_points'.
#         - If 'files_raster' is used, a dataframe of raster values is returned. The columns indicate the 'sp_points' in order. The row indicate the 'files_raster' in order.

#     Examples:
#         >>> zonal_stats_points(sp_points, files_raster_tif[0])
#         >>> zonal_stats_points(sp_points, files_raster=files_raster_tif).set_axis(sp_points['id'], axis = 1).assign(file = os.path.basename(files_raster_tif))
#     '''
#     df_xy = sp_points.geometry.get_coordinates()
#     coords = [(x,y) for x, y in zip(df_xy.x, df_xy.y)]

#     if files_raster is None:
#         with rasterio.open(file_raster) as f:
#             temp_values = [val[0] for val in f.sample(coords)]
#         temp_values = pd.Series(temp_values)

#         return (temp_values)
#     else:
#         df_values = []
#         for file_raster in files_raster:
#             with rasterio.open(file_raster) as f:
#                 df_values.append([val[0] for val in f.sample(coords)])
#         df_values = pd.DataFrame(df_values)

#         return (df_values)

#endregion -----------------------------------------------------------------------------------------
