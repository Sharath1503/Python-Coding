# Module example 

def calCircum(radius: float) -> float:
    """
    Calculate the circumference of a circle given its radius.
    """
    return 2 * (22/7) * radius

def calAreaofCircle(radius=None, diameter=None):
    '''
    returns area of circle based on radius or diameter
    '''
    pi =22/7
    if radius is not None:
        return pi * radius ** 2
    elif diameter is not None:
        return pi * (diameter/2) ** 2