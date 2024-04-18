import math
import numpy as np


def area(diameter):
    """Calculates the area of a circlular pipe.

    Args:
        diameter (float): The diameter of the pipe in mm .

    Returns:
        float: The area of the circularpipe  in m^2.
    """

    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")
    if diameter <= 0:
        raise ValueError("Diameter cannot be zero or negative")
    return math.pi * (diameter / 1000 / 2) ** 2


def velocity(flow, diameter):
    """
    Calculates the average velocity of fluid in a circular pipe with formula flow / Area.

    Parameters:
    Q (float): The volumetric flow rate of the fluid in L/s.
    Diameter (float): The diameter of the pipe in mm.

    Returns:
    float: The average velocity of the fluid in m/s.
    """
    if not isinstance(flow, (int, float)):
        raise TypeError("Flow must be a number (int or a float)")
    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")

    return (flow / area(diameter)) / 1000


def flow(velocity, diameter, liter=True):
    """
    Calculate the flow rate of a fluid through a pipe with the formula velocity * area.

    Parameters:
    velocity (float or int): The velocity of the fluid in the pipe.
    diameter (float or int): The diameter of the pipe.
    liter (bool, optional): Whether to return the flow rate in liters per second.
                            Defaults to True.
                            liter = False returns the flow rate in cubic meters per second.

    Returns:
    float or int: The flow rate of the fluid through the pipe.

    Raises:
    TypeError: If velocity or diameter is not a number (int or float).
    """

    if not isinstance(velocity, (int, float)):
        raise TypeError("Velocity must be a number (int or a float)")
    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")
    if liter:
        return (velocity * area(diameter)) * 1000
    else:
        return velocity * area(diameter)





def reynolds_number(velocity, diameter, viscosity=1.31 * 10**-6):
    """
    Calculates the Reynolds number for flow in a circular pipe.

    Parameters:
    Q (float): The flow rate of the fluid in L/s.
    Diameter (float): The diameter of the pipe in mm.
    viscosity (float): The viscosity of the fluid in m^2/s. Default is 1.3 * 10**-6.

    Returns:
    float: The Reynolds number.
    """
    if not isinstance(velocity, (int, float)):
        raise TypeError("Velocity(v) must be a number (int or a float)")
    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")
    if not isinstance(viscosity, (int, float)):
        raise TypeError("Viscosity must be a number (int or a float)")

   

    return (velocity * diameter / 1000) / viscosity

