"""
Main script for visualizing a 3D voxel structure.
Plot the following features:
    - the different domain composing the voxel structure
    - the connected components of the voxel structure
    - the deviation between the original geometry and the voxel structure

Three different mode are available for the plots:
    - windowed mode: with the Qt Framework
    - notebook mode: with Jupyter notebook
    - silent mode: nothing is shown and the program exit

The plots are generated with PyVista.
The plots can be saved as PNG images.
"""

__author__ = "Thomas Guillod"
__copyright__ = "Thomas Guillod - Dartmouth College"
__license__ = "Mozilla Public License Version 2.0"

from pypeec.lib_visualization import data_viewer
from pypeec.lib_visualization import data_voxel
from pypeec.lib_visualization import manage_pyvista
from pypeec.lib_visualization import manage_plotgui
from pypeec.lib_check import check_data_visualization
from pypeec.lib_check import check_data_options
from pypeec import log

# get a logger
LOGGER = log.get_logger("VIEWER")


def _get_grid_voxel(data_geom):
    """
    Convert the complete voxel geometry into a PyVista uniform grid.
    Convert the non-empty voxel geometry into a PyVista unstructured grid.
    Add the domain tags to the grid.
    """

    # extract the data
    n = data_geom["n"]
    d = data_geom["d"]
    c = data_geom["c"]
    domain_def = data_geom["domain_def"]
    connection_def = data_geom["connection_def"]
    pts_cloud = data_geom["pts_cloud"]
    reference = data_geom["reference"]

    # get voxel indices
    idx = data_viewer.get_voxel(domain_def)

    # convert the voxel geometry into PyVista grids
    grid = data_voxel.get_grid(n, d, c)
    voxel = data_voxel.get_voxel(grid, idx)
    point = data_voxel.get_point(pts_cloud)
    reference = data_voxel.get_reference(reference, voxel)

    # add the domain tag to the geometry
    voxel = data_viewer.set_data(voxel, idx, domain_def, connection_def)

    return grid, voxel, point, reference


def _get_plot(tag, data_viewer, grid, voxel, point, reference, gui_obj):
    """
    Make a plot with the voxel structure and the domains.
    """

    # extract the data
    framework = data_viewer["framework"]
    title = data_viewer["title"]
    layout = data_viewer["layout"]
    data_window = data_viewer["data_window"]
    data_plot = data_viewer["data_plot"]
    data_options = data_viewer["data_options"]

    # check framework
    if framework != "pyvista":
        raise ValueError("invalid plot framework")

    # get the plotter (with the Qt framework)
    pl = gui_obj.open_pyvista(tag, title, data_window)

    # make the plot
    manage_pyvista.get_plot_viewer(pl, grid, voxel, point, reference, layout, data_plot, data_options)


def run(
        data_voxel, data_viewer,
        tag_plot=None, plot_mode="qt", folder=".", name=None,
):
    """
    Main script for visualizing a 3D voxel structure.
    Handle invalid data with exceptions.
    """

    # check the voxel data
    LOGGER.info("check the voxel data")
    data_geom = check_data_options.check_data_voxel(data_voxel)

    # check the input data
    LOGGER.info("check the input data")
    check_data_visualization.check_data_viewer(data_viewer)
    check_data_options.check_plot_options(plot_mode, folder, name)
    check_data_options.check_tag_list(data_viewer, tag_plot)

    # find the plots
    if tag_plot is not None:
        data_viewer = {key: data_viewer[key] for key in tag_plot}

    # create the Qt app (should be at the beginning)
    LOGGER.info("init the plot manager")
    gui_obj = manage_plotgui.PlotGui(plot_mode, folder, name)

    # handle the data
    LOGGER.info("parse data")
    (grid, voxel, point, reference) = _get_grid_voxel(data_geom)

    # make the plots
    with log.BlockTimer(LOGGER, "generate plots"):
        for i, (tag_plot, data_viewer_tmp) in enumerate(data_viewer.items()):
            LOGGER.info("plotting %d / %d / %s" % (i+1, len(data_viewer), tag_plot))
            _get_plot(tag_plot, data_viewer_tmp, grid, voxel, point, reference, gui_obj)

    # enter the event loop (should be at the end, blocking call)
    gui_obj.show()
