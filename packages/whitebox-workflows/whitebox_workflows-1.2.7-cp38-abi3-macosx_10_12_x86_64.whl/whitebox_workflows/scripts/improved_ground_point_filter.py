from math import ceil
from whitebox_workflows import LicenseType, Lidar, WbEnvironmentBase
from .utils import LicenseError, print_tool_header

def improved_ground_point_filter(
        wbe: WbEnvironmentBase, 
        input: Lidar, 
        block_size = 1.0, # in xy units
        max_building_size = 150.0, # in xy units
        slope_threshold = 15.0,
        elev_threshold = 0.15
    ) -> Lidar:
    if wbe.license_type != LicenseType.WbWPro:
        raise LicenseError()
    
    reset_verbose = wbe.verbose
    if wbe.verbose:
        print_tool_header("improved_ground_point_filter")
        print("\nPerforming operation...")

    wbe.verbose = False # suppress the output from each of the workflow components

    max_building_size = ceil(max_building_size / block_size) # max_building_size expressed in cell

    # print('Finding min z points...')
    grd_pts = wbe.filter_lidar_by_percentile(input, 0.0, 1.0)

    # print('TINing...')
    tin = wbe.lidar_tin_gridding(
        input_lidar=grd_pts,
        interpolation_parameter="z",
        returns_included='all',
        cell_size=block_size, 
        excluded_classes=None
    )

    # print('Finding and removing low-point noise...')
    tin2 = wbe.fill_pits(tin)
    tin = (tin2 - tin).con(f'value > {elev_threshold*2.0}', tin2, tin)

    # print('Removing off-terrain objects....')
    dtm = wbe.remove_off_terrain_objects(tin, filter_size=max_building_size, slope_threshold=slope_threshold)

    grd_pts = wbe.filter_lidar_by_reference_surface(input_lidar=input, ref_surface=dtm, threshold=elev_threshold)
    
    if grd_pts.header.get_num_points() == 0:
        raise Exception("No ground points were detected")

    wbe.verbose = reset_verbose

    return grd_pts