#!/usr/bin/env python3

import math
from clear import clear
from time import sleep

def pq():
	#printing example to know what p and q are
	print("0 = x² + px + q\n")

	#getting variables
	try:
		p = float(input("p: "))
		q = float(input("q: "))
	
		def pqmeth(x, y):
			print("\nx" + x + f" = -({p} / 2) {y} √(({p} / 2)²-({q}))")
			sleep(0.5)
			print("\n   = -(" + str(p/2) + f") {y} √((" + str(p/2) + f")² - ({q}))")
			sleep(0.5)
			print("\n   = -(" + str(p/2) + f")  {y}  √(" + str((p/2)*(p/2)) + " + " + str(-(q)) + ")")
			sleep(0.5)
			print(f"\n   = -(" + str(p/2) + f")  {y}  √(" + str((p/2)*(p/2)-(q)) + ")")
			sleep(0.5)		
			print(f"\n   = -(" + str(p/2) + f")  {y}  " + str(math.sqrt(((p/2)**2)-(q))))
			sleep(0.5)		
			if y == "-":
				print("\n   = " + str(-(p/2)-math.sqrt(((p/2)**2)-(q))))
				sleep(0.5)
			elif y == "+":
				print("\n   = " + str(-(p/2)+math.sqrt(((p/2)**2)-(q))))
				sleep(0.5)

		pqmeth("₁", "+")
		pqmeth("₂", "-")

	except ValueError:
		print("\nMath Error!")
		input("\npress Enter to continue..")
		clear()