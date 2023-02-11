#!/usr/bin/env python3
"""Exemplo de funções"""

"""
f(x) = 5 * (x / 2)
"""

def f(x):
  	return 5 * (x / 2)

def double(x):
  	return x * 2
  
print(f(10))
print(double(f(10)) == 50 )

###

def print_in_upper(text):
  	print(text.upper())

print_in_upper("ayrton")

####

def heron(a, b, c):
  """Calcula a área de um triângulo"""
  perimeter = a + b + c
  s = perimeter / 2
  area = s * (s - a) * (s - b) * (s - c)
  return area ** 0.5 # math.sqrt(area)

area_triangulo = heron(3, 4, 5)
print(area_triangulo)