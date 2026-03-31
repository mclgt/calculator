import math

def sin(x):
    """Calcola il seno di x."""
    return math.sin(math.radians(x))

def cos(x):
    """Calcola il coseno di x."""
    return math.cos(math.radians(x))

def tan(x):
    """Calcola la tangente di x."""
    return math.tan(math.radians(x))

def logarithm10(x):
    """Calcola il logaritmo in base 10 di x."""
    if x <= 0:
        raise ValueError("Input must be greater than 0.")
    return math.log10(x)

def natural_logarithm(x): 
    """Calcola il logaritmo naturale di x."""
    if x <= 0:
        raise ValueError("Input must be greater than 0.")
    return math.log(x)

def power(base, exponent):
    """Calcola base elevato alla potenza di exponent."""
    return math.pow(base, exponent)

def square_root(x):
    """Calcola la radice quadrata di x."""
    if x < 0:
        raise ValueError("Input must be non-negative.")
    return math.sqrt(x)

