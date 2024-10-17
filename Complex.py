from math import sqrt 

class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __subtract__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)
    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __div__(self, other):
        a, b, p, q = self.real, self.imag, other.real, other.imag 
        r = p**2 + q**2
        return Complex((a*p+b*q)/r, (b*p-a*q)/r)
    
    def __conj__(self):
        return Complex(self.real, -1 * self.imag)