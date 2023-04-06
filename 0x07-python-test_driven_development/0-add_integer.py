!#/usr/bin/python3

def add_integer(a, b=98):
    
    # Check that both inputs are integers or floats
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast both inputs to integers if they are floats

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    # Compute the addition of a and b
    
    return a + b
