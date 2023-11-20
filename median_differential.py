#!/usr/bin/env python3

def f(x):
	return 2*(x-3)**2

pairs = eval(input("give all pairs needed: "))

for pair in pairs:
	x1 = pair[0]
	x2 = pair[1]

	y1 = f(x1)
	y2 = f(x2)

	m = (y2-y1)/(x2-x1)

	print(f"{pair}\t\t{m}")
