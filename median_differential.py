#!/usr/bin/env python3

def median_diff():
	function = input("Insert function(x^n == x**n, nx == n*x) f(x) = ")

	f = lambda x : eval(function)
	
	pairs = eval(input("give all pairs needed (seperated by a comma): "))

	if str(pairs).count(",") < 2:
		pairs = [pairs]
		
	for pair in pairs:
		x1 = pair[0]
		x2 = pair[1]
	
		y1 = f(x1)
		y2 = f(x2)
	
		m = (y2-y1)/(x2-x1)
	
		print(f"{pair}\t\t{m}")
