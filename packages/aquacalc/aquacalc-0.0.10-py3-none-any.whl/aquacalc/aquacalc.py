def calculate_tank_volume(length, width, height):
    """Calculates the volume of a rectangular tank.

    Args:
        length (float): Length of the tank.
        width (float): Width of the tank.
        height (float): Height of the tank.

    Returns:
        float: The volume of the tank.
    """
    volume = length * width * height
    return volume

def how_many():
    a= int(input('How many times '))
    
    print('\n'.join('Fuck off' for _ in range(a)))
    

