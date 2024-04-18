import pytest
from aquacalc.all_formulas import  swamee_jain
from aquacalc.all_simple import area, velocity, reynolds_number
import math 

def test_area():
    """
    Test that the area function returns the correct calculation.
    """
    # Test with a diameter of 1000mm (1m), expecting area = π * (0.5^2)
    assert math.isclose(area(1000), math.pi * 0.5**2, rel_tol=1e-4)

def test_velocity():
    """
    Test that the velocity function returns the correct calculation.
    """
    # Test with a flow of 1000L/s and diameter of 1000mm (1m)
    # Expected velocity = flow / area / 1000 = 1000 / (π * (0.5^2)) / 1000
    expected_velocity = 1000 / (math.pi * 0.5**2) / 1000
    assert math.isclose( velocity(1000, 1000), expected_velocity, rel_tol=1e-4)

def test_reynolds_number():
    # Test with known values
    flow = 110.25  # L/s
    diameter = 350  # mm
    viscosity = 1.3 * 10**-6  # m^2/s
    expected_result = 306160.6538867


    assert pytest.approx(reynolds_number(flow, diameter, viscosity), 0.0001) == expected_result

    # Test with default viscosity
    expected_result_default_viscosity = 306160.6538867
    assert pytest.approx(reynolds_number(flow, diameter), 0.0001) == expected_result_default_viscosity

def test_swamee_jain():
    # Test with known values
    flow = 100  # L/s
    diameter = 200  # mm
    ruhet = 0.5 # mm to m
    viscosity = 1.3 * 10**-6  # m^2/s
    expected_result = 0.019
    assert pytest.approx(swamee_jain(flow, diameter, ruhet, viscosity), 0.001) == expected_result

    # Test with default viscosity
    expected_result_default_viscosity = 0.019
    assert pytest.approx(swamee_jain(flow, diameter, ruhet), 0.001) == expected_result_default_viscosity




