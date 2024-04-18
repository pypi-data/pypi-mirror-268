from fxpmath import Fxp
from math import isclose
from fixedpoint_config import DTYPE
def test_multiplication():
    # Fxp as operands
    x1 = Fxp(0.5, signed=False, dtype=DTYPE)
    x2 = Fxp(0.7, signed=False, dtype=DTYPE)

    # Define the type of the new variable first
    y = Fxp(None, signed=False, dtype=DTYPE)
    # Set the value of the new variable with equal
    y.equal(x1*x2)

    assert (y.dtype == x1.dtype and y.dtype == x2.dtype)

def test_addition():
    x1 = Fxp(0.2, signed=False, dtype=DTYPE)
    x2 = Fxp(0.3, signed=False, dtype=DTYPE)
    y = Fxp(None, signed=False, dtype=DTYPE)
    y.equal(x1 + x2)

    assert (y.dtype == x1.dtype and y.dtype == x2.dtype)
    assert isclose(0.5, y, rel_tol=0.05)

def test_overflow():
    x1 = Fxp(0.8, signed=False, dtype=DTYPE)
    print(x1.info(verbose=True))
    x2 = Fxp(0.5, signed=False, dtype=DTYPE)
    y = Fxp(None, signed=False, dtype=DTYPE)
    y.equal(x1 + x2)

    assert (y.dtype == x1.dtype and y.dtype == x2.dtype)
    assert isclose(1, y, rel_tol=0.05)

def test_underflow():
    x1 = Fxp(0.8, signed=False, dtype=DTYPE)
    x2 = Fxp(0.5, signed=False, dtype=DTYPE)
    y = Fxp(None, signed=False, dtype=DTYPE)
    y.equal(x2 - x1)

    assert (y.dtype == x1.dtype and y.dtype == x2.dtype)
    assert isclose(0, y, rel_tol=0.05)
