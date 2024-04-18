import math
import numpy as np
from scipy.optimize import brentq

from aquacalc.all_simple import area , velocity , flow , reynolds_number 

def swamee_jain(diameter, ruhet, reynolds_number):
    """
    Calculates the friction factor using the Swamee-Jain equation.

    Parameters:
    - diameter (float): The diameter of the pipe (in mm).
    - ruhet (float): The roughness height of the pipe (in mm).
    - reynolds_number (float): The Reynolds number calculated using the flow rate, diameter, and viscosity.

    Returns:
    - friction_factor (float): The friction factor calculated using the Swamee-Jain equation.

    Formula:
    The Swamee-Jain equation is given by:
    f = 0.25 / (math.log10((ruhet / (3.7 * diameter)) + (5.74 / reynolds_number**0.9))) ** 2

    Note:
    - This equation is used to estimate the friction factor in fully developed turbulent flow in pipes.
    if the flow is laminar, the friction factor is calculated using the Poiseuille's equation.

    - The equation assumes that the flow is turbulent and the pipe is smooth.
    """
    if not isinstance(reynolds_number, (int, float)):
        raise TypeError("Reynolds number must be a number (int or a float)")
    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")
    if not isinstance(ruhet, (int, float)):
        raise TypeError("Roughness height (ruhet) must be a number (int or a float)")
 
   
    if reynolds_number < 4000: 
        return 64 / re
    else:
        return 0.25 / (math.log10((ruhet / (3.7 * diameter)) + (5.74 / reynolds_number**0.9)) ** 2)

    
 
    

def darcy_weisbach(frictions_factor, length, diameter, velocity):
    """
    Calculates the Darcy-Weisbach friction factor for fluid flow in a pipe.

    Parameters:
    frictions_factor (float): The friction factor of the pipe.
    length (float): The length of the pipe (in meters).
    diameter (float): The diameter of the pipe (in millimeters).
    velocity (float): The velocity of the fluid flow (in meters per second).

    Returns:
    float: The Darcy-Weisbach friction factor.

    Formula:
    The Darcy-Weisbach friction factor is calculated using the following formula:
    frictions_factor * length * velocity ** 2 / (2 * diameter / 1000 * 9.81)
    """
    return (
        frictions_factor * length * velocity ** 2 / (2 * diameter / 1000 * 9.81)
    )



def colebrook_white(diameter, roughness, reynolds_number):

    """Calculates the friction factor for pipe flow using the Colebrook-White equation.

    Parameters:
    - diameter (float): The inner diameter of the pipe (in meters).
    - roughness (float): The absolute roughness of the pipe's inner surface (in meters).
    - reynolds_number (float): The Reynolds number of the flow, which is a dimensionless quantity.

    Returns:
    - friction_factor (float): The friction factor calculated using the Colebrook-White equation.

    Formula:
    The Colebrook-White equation is an implicit equation given by:
    1/sqrt(f) = -2 * log10((roughness/(3.7*diameter)) + (2.51/(reynolds_number*sqrt(f))))

   

    Note:
    - This function uses the Brent's method to solve the implicit Colebrook-White equation.
    - The function assumes that the flow is fully turbulent.
    - The Brent's method requires initial bracketing values, which are provided within a typical range for turbulent flow.
    - The viscosity parameter is not required because the Reynolds number is used directly.

    Exceptions:
    - ValueError: If the Brent's method fails to find a solution within the provided bracketing values, an error is raised.

    Example usage:
    friction_factor = colebrook_white(diameter=0.1, roughness=1e-5, reynolds_number=10000)
    """
   
  
    
    # Function to find root
    def f_zero(f):
        return   1.0 / math.sqrt(f) + 2.0 * math.log10(
            roughness / (3.7 * diameter) + 2.51 / (reynolds_number * math.sqrt(f))
        )
        
        

    # Initial bracketing values for f
    f_l = 0.008  # A reasonable lower bound for turbulent flow
    f_u = 0.08  # A reasonable upper bound for turbulent flow

    # Use Brent's method to find the root
    try:
        # Use Brent's method to find the root
        f = brentq(f_zero, f_l, f_u)
    except ValueError as e:
        raise ValueError("The Brent method failed to find a root: " + str(e))

    return f

def frictions_factor(diameter, ruhet, reynolds_number, method="swamee_jain"):
    """Calculate the friction factor for fluid flow in a pipe.

    Args:
        diameter (float): The diameter of the pipe in mm .
        ruhet (float): The roughness height of the pipe in mm .
        reynolds_number (float): The Reynolds number of the flow.
        method (str, optional): The method to use for calculating the friction factor.
            Defaults to "swamee_jain".
            other methods are "colebrook_white"

    Returns:
        float: The friction factor.

    Raises:
        ValueError: If an invalid method is specified.

    Examples:
        >>> frictions_factor(100, 0.1, 10000)
        0.025

    """
    match method:
        case "swamee_jain":
            return swamee_jain(diameter, ruhet, reynolds_number)
        case "colebrook_white":
            return colebrook_white(diameter, ruhet, reynolds_number)
        case _:
            raise ValueError("Invalid method specified.")
        

