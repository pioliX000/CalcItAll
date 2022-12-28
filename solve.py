from sympy.parsing.sympy_parser import parse_expr
from sympy import *

variable_count = input("how many variables: ")

if variable_count == "1":
	x = symbols('x')
elif variable_count == "2":
	x = symbols('x')
	y = symbols('y')
elif variable_count == "3":
	x = symbols('x')
	y = symbols('y')
	z = symbols('z')
elif variable_count == "4":
	x = symbols('x')
	y = symbols('y')
	z = symbols('z')
	p = symbols('p')

eq1 = parse_expr(input("eq1: "))
eq2 = parse_expr(input("eq2: "))

print("\n" + str(eq1) + " = " + str(eq2) + "\n")

eq = Eq(eq1, eq2)

print(solve(eq))