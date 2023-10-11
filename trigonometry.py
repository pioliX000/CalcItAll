import math
from clear import clear
from time import sleep

lol, lol1, lol2, lol3, lol4, lol5 = "a", "b", "c", "@", "B", "Y"

# To prevent hard coding
nl = "\n"
cs = ": "

# Formula for Cosine Theorem
def bruh(o, q, p, k):
    try:
        x = float(input(o + cs))
        y = float(input(q + cs))
        a = float(input(p + cs)

        print(f"{nl}{k} = √({o}² + {q}² - 2 × {o} × {q} × cos({a}°))")

        print(f"{nl}  = √({x}² + {y}² - 2 × {x} × {y} × cos({a}°))")
        sleep(0.5)
        print(f"{nl}  = √({x*x} + {y*y} - 2 × {x} × {y} × cos({a}°))")                
        sleep(0.5)
        print(f"{nl}  = √({x*x} + {y*y} - {2*x*y} × cos({a}°))")
        sleep(0.5)
        print(f"{nl}  = √({x*x} + {y*y} - {2*x*y*math.cos(math.radians(a))})")
        sleep(0.5)
        print(f"{nl}  = √({(x*x+y*y)-(2*x*y*math.cos(math.radians(a))})")
        sleep(0.5)
        print(f"{nl}{k} = {math.sqrt(x*x+y*y-2*x*y*math.cos(math.radians(a)))}")

    except ValueError:
        print("\nMath Error!")
        input("\nPress Enter to continue..")
        clear()

# Formula for angles using Cosine Theorem
def bruh1(o, q, p, k):
    try:        
        x = float(input(o + cs))
        y = float(input(q + cs))
        z = float(input(p + cs))

        bitch = x*x+y*y-z*z
        bitch1 = 2*x*y

        print(f"{nl}{k} = cos⁻¹(({o}² + {q}² - {p}²) ÷ ( 2 × {o} × {q}))")

        print(f"{nl}  = cos⁻¹(({x*x} + {y*y} - {z*z}) ÷ (2 × {x} × {y}))")
        sleep(0.5)
        print(f"{nl}  = cos⁻¹(({x*x+y*y-z*z})÷(2 × {x} × {y}))")
        sleep(0.5)        
        print(f"{nl}  = cos⁻¹(({x*x+y*y-z*z} ÷ {2*x*y}))")
        sleep(0.5)
        print(f"{nl}  = cos⁻¹({bitch/bitch1})")
        print(f"{nl}{k} = {math.degrees(math.acos(bitch/bitch1))}°")

    except ValueError:
        print("\nMath Error!")
        input("\nPress Enter to continue..")
        clear()

# Formula for Sine Theorem
def bruh2(o, q, p, k):
    try:
        x = float(input(o + cs))
        a = float(input(q + cs))
        b = float(input(p + cs))

        print(f"{nl}{k} = ({o} × sin({q}°)) ÷ sin({p}°)")

        print(f"{nl}  = ({x} × sin({a}°)) ÷ sin({b}°)")
        sleep(0.5)
        print(f"{nl}  = ({x} × {math.sin(math.radians(a))}) ÷ sin({b}°)")
        sleep(0.5)
        print(f"{nl}  = ({x} × {math.sin(math.radians(a))}) ÷ {math.sin(math.radians(b)}")
        sleep(0.5)
        print(f"{nl}  = ({x*math.sin(math.radians(a))}) ÷ {math.sin(math.radians(b)}")
        sleep(0.5)
        print(f"{nl}{k} = {(x*math.sin(math.radians(a))/math.sin(math.radians(b))}")

    except ValueError:
        print("\nMath Error!")
        input("\nPress Enter to continue..")
        clear()

# Formula for angles using Sine Theorem
def bruh3(o, q, p, k):
    try:
        x = float(input(o + cs))
        y = float(input(q + cs))
        a = float(input(p + cs)

        print(f"{nl}{k} = sin⁻¹(({o}×sin(({p})))÷({q}))")

        print(f"{nl}  = sin⁻¹(({x}×sin({a}))÷{y})")
        sleep(0.5)
        print(f"{nl}  = sin⁻¹(({x} × {math.sin(math.radians(a))})) ÷ {y})")
        sleep(0.5)
        print(f"{nl}  = sin⁻¹({x*math.sin(math.radians(a))} ÷ {y})")
        sleep(0.5)
        print(f"{nl}  = sin⁻¹({(x*math.sin(math.radians(a))/y})")
        sleep(0.5)
        print(f"{nl}{k} = {math.degrees(math.asin(x*math.sin(math.radians(a))/y))}°")

    except ValueError:
        print("\nMath Error!")
        input("\nPress Enter to continue..")
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
        print(f"{nl}bruh")
        costher()

def sinther():
    formtype = input("get a, b, c, @, B or Y?: ")
    if formtype == "a":
        bruh2(lol1, lol3, lol4, lol)
    elif formtype == "b":
        bruh2(lol2, lol4, lol5, lol1)
    elif formtype == "c":
        bruh2(lol, lol5,
