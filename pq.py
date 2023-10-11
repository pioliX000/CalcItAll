#!/usr/bin/env python3

import math
from clear import clear
from time import sleep

def pq():
    # Printing example to know what p and q are
    print("0 = x² + px + q\n")

    # Getting variables
    try:
        p = float(input("p: "))
        q = float(input("q: "))

        def pqmeth(x, y):
            print(f"\nx{x} = -({p} / 2) {y} √(({p} / 2)² - ({q}))")
            sleep(0.5)
            print(f"\n   = -({p/2}) {y} √({(p/2)**2 - q})")
            sleep(0.5)
            print(f"\n   = -({p/2}) {y} {math.sqrt((p/2)**2 - q)}")
            sleep(0.5)
            if y == "-":
                result = -(p/2) - math.sqrt((p/2)**2 - q)
            elif y == "+":
                result = -(p/2) + math.sqrt((p/2)**2 - q)
            print(f"\n   = {result}")
            sleep(0.5)

        pqmeth("₁", "+")
        pqmeth("₂", "-")

    except ValueError:
        print("\nMath Error!")
        input("\nPress Enter to continue...")
        clear()
