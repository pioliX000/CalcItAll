import math

def is_whole(n):
    return n % 1 == 0

def calc_lineareq():
    try:
        calc_type = input("orth or norm: ")

        print("f1 y = mx + b")
        print("P1 ( x | y )\n")

        x = float(input("x: "))
        y = float(input("y: "))

        m1 = float(input("\nm1: "))

        if calc_type == "orth":
            m2 = round(-1/m1, 2)
            if is_whole(m2):
                m2 = int(m2)
            print(f"\nm2 = -1/m1 = {m2}")
        elif calc_type == "norm":
            m2 = m1
            if is_whole(m2):
                m2 = int(m2)

        b = round(y - m2 * x, 2)
        if is_whole(b):
            b = int(b)

        print("\nf2 y = mx + b")

        print(f"\nf2 {y} = {m2}*{x} + b")
        print(f"f2 {y} = {round(m2*x, 2)} + b")

        if m2 * x < 0:
            print(f"f2 {y} = {round(m2*x, 2)} + b | +{round(m2*x*-1, 2)}")
            print(f"f2 {round(y + (m2*x*-1), 2)} = b")
        elif m2 * x > 0:
            print(f"f2 {y} = {m2*x} + b | {round(m2*x*-1, 2)}")
            print(f"f2 {b} = b")

        if b < 0:
            print(f"\n\ny = {m2}x - {b*-1}")
        elif b > 0:
            print(f"\ny = {m2}x + {b}")

    except ValueError:
        print("\nMath Error!")
        input("\nPress Enter to continue...")
        clear()

def points():
    kek = input("parab(p) or linear(l): ")
    if kek == "l":
        try:
            print("y = mx + b")

            m = float(input("\nm: "))
            b = float(input("b: "))

            f = int(input("\nfrom: "))
            t = int(input("to: "))

            for x in range(f, t + 1):
                print(f"\nx={x} | y={m*x+b}")

        except ValueError:
            print("\nMath Error!")
            input("\nPress Enter to continue...")
            clear()

    elif kek == "p":
        try:
            print("\ny = ax² + bx + c")

            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))

            f = int(input("\nfrom: "))
            t = int(input("to: "))

            bdiva = round(b/a, 2)
            cdiva = round(c/a, 2)
            bdiv2 = round(bdiva/2, 2)

            newc = round(-math.fabs(bdiv2)**2 + cdiva, 2)

            for x in range(f, t + 1):
                y = a*x**2 + b*x + c
                print(f"\nx = {x} | y = {y}")
            print(f"\n   S ( {-bdiv2} | {round(newc * a, 2)} ) \n")

        except ValueError:
            print("\nMath Error!")
            input("\nPress Enter to continue...")
            clear()

def linear_solve():
    form_type = input("points(p) or calc new linear equation(ln): ")

    if form_type == "p":
        points()
    elif form_type == "ln":
        calc_lineareq()
