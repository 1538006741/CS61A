from math import pi, sqrt

def area_square(r):
    return r*r

def area_circle(r):
    return r*r*pi

def area_hexagon(r):
    return r*r*3*sqrt(3)/2

"""
we find a question that 
    >>>area_circle(-10)
    314.1592653589793
    we do not want to see this,the r should
    not be negetive.
so now we introdue a function:
    'assert',
    let me show it
    assert 3>2 , 'Math is broken'
    assert 3<2 , 'taht is false'
    so when it is false, print the
    information .

and then we add it into our code
"""
from math import pi, sqrt

def area_square(r):
    assert r>0, 'The length must be positive'
    return r*r

def area_circle(r):
    assert r>0, 'The length must be positive'
    return r*r*pi

def area_hexagon(r):
    assert r>0, 'The length must be positive'
    return r*r*3*sqrt(3)/2

"""
However, it is so so... boring that we
compete  assert r>0, 'The length must be positive'
again and again

so maybe we can define a function so that 
we can make it easy.

Let us do it!
"""

from math import pi, sqrt

def area(r,shape_constant):
    assert r>0, 'The length must be positive'
    return r*r*shape_constant

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    return area(r,3*sqrt(3)/2)