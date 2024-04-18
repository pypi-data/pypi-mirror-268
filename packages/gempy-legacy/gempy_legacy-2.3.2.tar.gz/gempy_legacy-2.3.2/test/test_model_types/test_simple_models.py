import pytest

import numpy as np
import sys, os

sys.path.append("../..")
import gempy_legacy
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

input_path = os.path.dirname(__file__) + '/../input_data'
update_sol = False
test_values = [45, 150, 2500, 67000, 100000]


class TestNoFaults:
    """
    I am testing all block and potential field values so sol is (n_block+n_pot)
    """

    def test_a(self, interpolator):
        """
        2 Horizontal layers with drift 0
        """
        # Importing the data from csv files and settign extent and resolution
        geo_data = gempy_legacy.create_data(extent=[0, 10, 0, 10, -10, 0], resolution=[50, 50, 50],
                                            path_o=input_path + "/GeoModeller/test_a/test_a_Foliations.csv",
                                            path_i=input_path + "/GeoModeller/test_a/test_a_Points.csv")

        geo_data.set_aesara_function(interpolator)

        # Compute model
        sol = gempy_legacy.compute_model(geo_data)

        if update_sol:
            np.save(input_path + '/test_a_sol.npy', sol.lith_block[test_values])

        # Load model
        real_sol = np.load(input_path + '/test_a_sol.npy')

        # Checking that the plots do not rise errors
        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.savefig(os.path.dirname(__file__) + '/../figs/test_a.png', dpi=100)

        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, show_scalar=True)

        # We only compare the block because the absolute pot field I changed it
        np.testing.assert_array_almost_equal(np.round(sol.lith_block[test_values]), real_sol, decimal=0)

    def test_b(self, interpolator):
        """
        Two layers a bit curvy, drift degree 1
        """

        # Importing the data from csv files and settign extent and resolution
        geo_data = gempy_legacy.create_data(extent=[0, 10, 0, 10, -10, 0], resolution=[50, 50, 50],
                                            path_o=input_path + "/GeoModeller/test_b/test_b_Foliations.csv",
                                            path_i=input_path + "/GeoModeller/test_b/test_b_Points.csv")

        geo_data.set_aesara_function(interpolator)

        # Compute model
        sol = gempy_legacy.compute_model(geo_data)

        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.savefig(os.path.dirname(__file__) + '/../figs/test_b.png', dpi=200)

        if update_sol:
            np.save(input_path + '/test_b_sol.npy', sol.lith_block[test_values])

        # Load model
        real_sol = np.load(input_path + '/test_b_sol.npy')

        # Checking that the plots do not rise errors
        gempy_legacy.plot.plot_2d(geo_data, cell_number=25)

        # We only compare the block because the absolute pot field I changed it
        np.testing.assert_array_almost_equal(np.round(sol.lith_block[test_values]), real_sol, decimal=0)

    def test_c(self, interpolator):
        """
        Two layers a bit curvy, drift degree 0
        """

        # Importing the data from csv files and settign extent and resolution
        geo_data = gempy_legacy.create_data(extent=[0, 10, 0, 10, -10, 0], resolution=[50, 50, 50],
                                            path_o=input_path + "/GeoModeller/test_c/test_c_Foliations.csv",
                                            path_i=input_path + "/GeoModeller/test_c/test_c_Points.csv")

        geo_data.set_aesara_function(interpolator)

        # Compute model
        sol = gempy_legacy.compute_model(geo_data)

        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.savefig(os.path.dirname(__file__) + '/../figs/test_c.png', dpi=200)

        if update_sol:
            np.save(input_path + '/test_c_sol.npy', sol.lith_block[test_values])

        # Load model
        real_sol = np.load(input_path + '/test_c_sol.npy')

        # Checking that the plots do not rise errors
        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, show_scalar=True)

        # We only compare the block because the absolute pot field I changed it
        np.testing.assert_array_almost_equal(np.round(sol.lith_block[test_values]), real_sol, decimal=0)


class TestFaults:

    def test_d(self, interpolator):
        """
        Two layers 1 fault
        """

        # Importing the data from csv files and settign extent and resolution
        geo_data = gempy_legacy.create_data(extent=[0, 10, 0, 10, -10, 0], resolution=[50, 50, 50],
                                            path_o=input_path + "/GeoModeller/test_d/test_d_Foliations.csv",
                                            path_i=input_path + "/GeoModeller/test_d/test_d_Points.csv")

        gempy_legacy.map_stack_to_surfaces(geo_data, {'fault1': 'f1', 'series': ('A', 'B')})

        geo_data.set_is_fault('fault1')

        geo_data.set_aesara_function(interpolator)

        # Compute model
        sol = gempy_legacy.compute_model(geo_data)

        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.savefig(os.path.dirname(__file__) + '/../figs/test_d.png', dpi=200)

        if update_sol:
            np.save(input_path + '/test_d_sol.npy', sol.lith_block[test_values])

        # Load model
        real_sol = np.load(input_path + '/test_d_sol.npy')

        # We only compare the block because the absolute pot field I changed it
        np.testing.assert_array_almost_equal(np.round(sol.lith_block[test_values]), real_sol, decimal=0)

    def test_e(self, interpolator):
        """
        Two layers a bit curvy, 1 fault
        """
        # Importing the data from csv files and settign extent and resolution
        geo_data = gempy_legacy.create_data(extent=[0, 10, 0, 10, -10, 0], resolution=[50, 50, 50],
                                            path_o=input_path + "/GeoModeller/test_e/test_e_Foliations.csv",
                                            path_i=input_path + "/GeoModeller/test_e/test_e_Points.csv")

        gempy_legacy.map_stack_to_surfaces(geo_data, {'fault1': 'f1', 'series': ('A', 'B')})
        geo_data.set_is_fault('fault1')

        geo_data.set_aesara_function(interpolator)

        # Compute model
        sol = gempy_legacy.compute_model(geo_data)

        if update_sol:
            np.save(input_path + '/test_e_sol.npy', sol.lith_block[test_values])

        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.savefig(os.path.dirname(__file__) + '/../figs/test_e.png', dpi=200)

        # Load model
        real_sol = np.load(input_path + '/test_e_sol.npy')

        # We only compare the block because the absolute pot field I changed it
        np.testing.assert_array_almost_equal(np.round(sol.lith_block[test_values]), real_sol, decimal=0)

    def test_f_sort_surfaces(self, interpolator):
        """
        Two layers a bit curvy, 1 fault. Checked with geomodeller
        """

        # Importing the data from csv files and settign extent and resolution
        geo_data = gempy_legacy.create_data(extent=[0, 2000, 0, 2000, -2000, 0], resolution=[50, 50, 50],
                                            path_o=input_path + "/GeoModeller/test_f/test_f_Foliations.csv",
                                            path_i=input_path + "/GeoModeller/test_f/test_f_Points.csv")

        gempy_legacy.map_stack_to_surfaces(geo_data, {'fault1': 'MainFault',
                                               'series'       : ('Reservoir',
                                                          'Seal',
                                                          'SecondaryReservoir',
                                                          'NonReservoirDeep'
                                                          ),
                                                      },
                                           )

        geo_data.set_aesara_function(interpolator)
        geo_data.set_is_fault('fault1')

        # Compute model
        sol = gempy_legacy.compute_model(geo_data, sort_surfaces=True)

        if update_sol:
            np.save(input_path + '/test_f_sol.npy', sol.lith_block[test_values])

        real_sol = np.load(input_path + '/test_f_sol.npy')
        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.show()
        plt.savefig(os.path.dirname(__file__) + '/../figs/test_f.png', dpi=200)

        gempy_legacy.compute_model(geo_data)
        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.show()

        gempy_legacy.compute_model(geo_data)
        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.show()

        # We only compare the block because the absolute pot field I changed it
        np.testing.assert_array_almost_equal(np.round(sol.lith_block[test_values]), real_sol, decimal=0)

        ver, sim = gempy_legacy.get_surfaces(geo_data)
        print(ver, sim)

    def test_compute_model_multiple_ranges(self, interpolator):

        # Importing the data from csv files and settign extent and resolution
        geo_data = gempy_legacy.create_data(extent=[0, 2000, 0, 2000, -2000, 0], resolution=[50, 50, 50],
                                            path_o=input_path + "/GeoModeller/test_f/test_f_Foliations.csv",
                                            path_i=input_path + "/GeoModeller/test_f/test_f_Points.csv")

        gempy_legacy.map_stack_to_surfaces(geo_data, {'fault1': 'MainFault',
                                               'series'       : ('Reservoir',
                                                          'Seal',
                                                          'SecondaryReservoir',
                                                          'NonReservoirDeep'
                                                          ),
                                                      },
                                           )

        geo_data.set_aesara_function(interpolator)
        geo_data.set_is_fault('fault1')
        geo_data.modify_kriging_parameters('range', [3000, 3500, 0])
        geo_data._additional_data.kriging_data.set_default_c_o()
        # Compute model
        sol = gempy_legacy.compute_model(geo_data, sort_surfaces=True)
        gempy_legacy.plot.plot_2d(geo_data, cell_number=25, direction='y', show_data=True)
        plt.show()


def test_simple_model_gempy_engine():
    import numpy
    numpy.set_printoptions(precision=3, linewidth=200)

    g = gempy_legacy.create_data("test_engine", extent=[-4, 4, -4, 4, -4, 4], resolution=[4, 1, 4])
    sp = np.array([[-3, 0, 0],
                   [0, 0, 0],
                   [2, 0, 0.5],
                   [2.5, 0, 1.2],
                   [3, 0, 2],
                   [1, 0, .2],
                   [2.8, 0, 1.5]])

    g.set_default_surfaces()

    for i in sp:
        g.add_surface_points(*i, surface="surface1")

    g.add_orientations(-3, 0, 2, pole_vector=(0, 0, 1), surface="surface1")
    g.add_orientations(2, 0, 3, pole_vector=(-.2, 0, .8), surface="surface1")

    g.modify_orientations([0, 1], smooth=0.000000000001)
    g.modify_surface_points(g._surface_points.df.index, smooth=0.0000000001)

    gempy_legacy.set_interpolator(g, verbose=[
        "n_surface_op_float_sigmoid",
        "scalar_field_iter",
        "compare",
        "sigma"
    ])

    g.modify_kriging_parameters("range", 50)
    # g.modify_kriging_parameters("$C_o$", 5 ** 2 / 14 / 3)
    g.modify_kriging_parameters("drift equations", [0])

    import aesara
    dtype = "float32"

    g._interpolator.aesara_graph.i_reescale.set_value(np.cast[dtype](1.))
    g._interpolator.aesara_graph.gi_reescale.set_value(np.cast[dtype](1.))

    gempy_legacy.compute_model(g)

    print(g.additional_data)
    print(g.solutions.scalar_field_matrix)

    gempy_legacy.plot_2d(g)
    print(g.grid.values)

    print(g.solutions.weights_vector)
