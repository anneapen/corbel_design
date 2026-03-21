
#Determining bearing capacity of concrete
def bearing_capacity(fck:float):
    """
    Calculates the bearing capacity of the concrete
    """
    cap=0.4*fck
    return round(cap,2)