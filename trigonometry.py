#!/usr/bin/env python3

import math
from clear import clear
from time import sleep

lol, lol1, lol2, lol3, lol4, lol5 = "a", "b", "c", "@", "B", "Y"

#to prevent hard coding
nl = "\n"
cs = ": "

#formula for Cosine Theorem
def bruh(o, q, p, k):
	try:
		x = float(input(o + cs))
		y = float(input(q + cs))
		a = float(input(p + cs))
		
		print(nl + f"{k} = √({o}² + {q}² - 2 × {o} × {q} × cos({p}°))")
		
		print(nl + f"  = √({x}² + {y}² - 2 × {x} × {y} × cos({a}°))")
		sleep(0.5)
		print(nl + "  = √(" + str(x*x) + " + " + str(y*y) + f" - 2 × {x} × {y} × cos({a}°))")				
		sleep(0.5)
		print(nl + "  = √(" + str(x*x) + " + " + str(y*y) + " - " + str(2*x*y) + f" × cos({a}°))")
		sleep(0.5)
		print(nl + "  = √(" + str(x*x) + " + " + str(y*y) + " - " + str(2*x*y) + " × " + str(math.cos(math.radians(a))) + ")")
		sleep(0.5)
		print(nl + "  = √(" + str(x*x) + " + " + str(y*y) + " - " + str(2*x*y*math.cos(math.radians(a))) + ")")
		sleep(0.5)
		print(nl + "  = √(" + str((x*x+y*y)-(2*x*y*math.cos(math.radians(a)))) + ")")
		sleep(0.5)
		print(nl + k + " = " + str(math.sqrt(x*x+y*y-2*x*y*math.cos(math.radians(a)))))

	except ValueError:
		print("\nMath Error!")
		input("\npress Enter to continue..")
		clear()

#formula for angles using Cosine Theorem
def bruh1(o, q, p, k):
	try:		
		x = float(input(o + cs))
		y = float(input(q + cs))
		z = float(input(p + cs))

		bitch = x*x+y*y-z*z
		bitch1 = 2*x*y
		
		print(nl + f"{k} = cos⁻¹(({o}² + {q}² - {p}²) ÷ ( 2 × {o} × {q}))")

		print(nl + f"  = cos⁻¹(({x}² + {y}² - {z}²) ÷ ( 2 × {x} × {y}))")
		sleep(0.5)
		print(nl + "  = cos⁻¹(({x*x} + {y*y} - {z*z}) ÷ (2 × {x} × {y}))")
		sleep(0.5)		
		print(nl + f"  = cos⁻¹(({x*x+y*y-z*z})÷(2 × {x} × {y}))")
		sleep(0.5)		
		print(f"{nl} = cos⁻¹(({x*x+y*y-z*z} ÷ {2*x*y}))")
		sleep(0.5)
		print(nl + "  = cos⁻¹(" + str(bitch/bitch1) + ")")
		print(nl + k + " = " + str(math.degrees(math.acos(bitch/bitch1))) + "°")
	
	except ValueError:
		print("\nMath Error!")
		input("\npress Enter to continue..")
		clear()

#formula for Sine Theorem
def bruh2(o, q, p, k):
	try:
		x = float(input(o + cs))
		a = float(input(q + cs))
		b = float(input(p + cs))

		print(nl + f"{k} = ({o} × sin({q}°)) ÷ sin({p}°)")
		
		print(nl + f"  = ({x} × sin({a}°)) ÷ sin({b}°)")
		sleep(0.5)
		print(nl + f"  = ({x} × " + str(math.sin(math.radians(a))) + f") ÷ sin({b}°)")
		sleep(0.5)
		print(nl + f"  = ({x} × " + str(math.sin(math.radians(a))) + ") ÷ " + str(math.sin(math.radians(b))))
		sleep(0.5)
		print(nl + "  = (" + str(x*math.sin(math.radians(a))) + ") ÷ " + str(math.sin(math.radians(b))))
		sleep(0.5)
		print(nl + k + " = " + str((x*math.sin(math.radians(a)))/math.sin(math.radians(b))))
	
	except ValueError:
		print("\nMath Error!")
		input("\npress Enter to continue..")
		clear()

#formula for angles using Sine Theorem
def bruh3(o, q, p, k):
	try:
		x = float(input(o + cs))
		y = float(input(q + cs))
		a = float(input(p + cs))
		
		print(nl + f"{k} = sin⁻¹(({o}×sin(({p})))÷({q}))")
		
		print(nl + f"  = sin⁻¹(({x}×sin({a}))÷{y})")
		sleep(0.5)
		print(nl + "  = sin⁻¹((" + str(x) + " × " + str(math.sin(math.radians(a))) +f")) ÷ {y})")
		sleep(0.5)
		print(nl + "  = sin⁻¹(" + str(x*math.sin(math.radians(a))) + f" ÷ {y})")
		sleep(0.5)
		print(nl + "  = sin⁻¹(" + str((x*math.sin(math.radians(a)))/y) + ")")
		sleep(0.5)
		print(nl + k + " = " + str(math.degrees(math.asin(x*math.sin(math.radians(a))/y))) + "°")
	
	except ValueError:
		print("\nMath Error!")
		input("\npress Enter to continue..")
		clear()

def costher():
	formtype = input("get a, b, c, @, B or Y?: ")
	if formtype == "a":
		bruh(lol1, lol2, lol3, lol)
	elif formtype == "b":
		bruh(lol, lol2, lol4, lol1)
	elif formtype == "c":
		bruh(lol, lol1, lol5, lol2)
	elif formtype == "@":
		bruh1(lol1, lol2, lol, lol3)
	elif formtype == "B":
		bruh1(lol2, lol, lol1, lol4)
	elif formtype == "Y":
		bruh1(lol, lol1, lol2, lol5)
	else:
		print(nl + "bruh")
		costher()

def sinther():
	formtype = input("get a, b, c, @, B or Y?: ")
	if formtype == "a":
		bruh2(lol1, lol3, lol4, lol)
	elif formtype == "b":
		bruh2(lol2, lol4, lol5, lol1)
	elif formtype == "c":
		bruh2(lol, lol5, lol3, lol2)
	elif formtype == "@":
		bruh3(lol, lol1 + "/" + lol2, lol4 + "/" + lol5, lol3)
	elif formtype == "B":
		bruh3(lol1, lol + "/" + lol2, lol3 + "/" + lol5, lol4)
	elif formtype == "Y":
		bruh3(lol2, lol + "/" + lol1, lol3 + "/" + lol4, lol5)
	else:
		print(nl + "bruh")
		sinther()