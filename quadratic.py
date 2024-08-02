import math
from clear import clear

def Vertex():
    try:
        print("y = ax² + bx + c")
    
        a = float(input("\na: "))
        b = float(input("b: "))
        c = float(input("c: "))
    
        #vertex form
        bdiva = round(b/a, 2)
        cdiva = round(c/a, 2)
        bdiv2 = round(bdiva/2, 2)
        twoa = a*2
    
        sign1 = "+"
        sign2 = "+"
    
        #check for sign of numbers and assign them to properly display the function
        if b < 0:
                sign1 = "-"
    
        if c < 0:
                sign2 = "-"
        #
    
        #print equation
        print(f"\ny = {a}x² {sign1} {math.fabs(b)}x {sign2} {c}")
        #
    
        #check once again
        if bdiva < 0:
                sign1 = "-"
        else:
                sign1 = "+"
    
        if cdiva < 0:
                sign2 = "-"
        else:
                sign2 = "+"
        #
    
        #factor out a
        print(f"y = {a}[x² {sign1} {math.fabs(bdiva)}x {sign2} {math.fabs(cdiva)}]")
        #
    
        #add quadratic addition
        print(f"y = {a}[x² {sign1} {math.fabs(bdiva)}x + {math.fabs(bdiv2)}² + (-({math.fabs(bdiv2)}²) {sign2} {math.fabs(cdiva)})]")
        #
    
        #square (b/a)/2
        print(f"y = {a}[x² {sign1} {math.fabs(bdiva)}x + {math.fabs(bdiv2)}² + (-{round(bdiv2**2, 2)} {sign2} {math.fabs(cdiva)})]")
        #
    
        #check again
        if -math.fabs(bdiv2)**2 + cdiva < 0:
                sign2 = "-"
        else:
                sign2 = "+"
        #
    
        #calculate new c
        newc = round(-math.fabs(bdiv2)**2 + cdiva, 2)
    
        print(f"y = {a}[(x² {sign1} {math.fabs(bdiva)}x + {math.fabs(bdiv2)}²) {sign2} {math.fabs(newc)}]")
    
        #create binomial equation
        print(f"y = {a}[(x {sign1} {math.fabs(bdiv2)})² {sign2} {math.fabs(newc)}]")
        #
    
        #check again
        if newc * a < 0:
                sign2 = "-"
        else:
                sign2 = "+"
        #
    
        #factor in a
        print(f"y = {a}(x {sign1} {math.fabs(bdiv2)})² {sign2} {round(math.fabs(newc * a), 2)}")
        #
    
        #print out point
        print(f"\n   S ( {-bdiv2} | {round(newc * a, 2)} ) \n")
        #
        #
        
         #quadratic formula
        print("\nx₁ = (-b + √(b² - 4ac))/2a")
        print("x₂ = (-b - √(b² - 4ac))/2a")
    
        print(f"\nx₁ = ({-b} + √({b}² - 4*{a}*{c}))/2*{a}")
        print(f"x₂ = ({-b} - √({b}² - 4*{a}*{c}))/2*{a}")
    
        print(f"\nx₁ = ({-b} + √({b**2 - round(4*a*c, 2)}))/{twoa}")
        print(f"x₂ = ({-b} - √({b**2 - round(4*a*c, 2)}))/{twoa}")
    
        try:
            #check if root is solvable
            sqrt = round(math.sqrt(b**2 - 4*a*c), 2)
            #
    
            print(f"\nx₁ = ({-b} + {sqrt})/{twoa}")
            print(f"x₂ = ({-b} - {sqrt})/{twoa}")
    
            print(f"\nx₁ = {round(-b + sqrt, 2)}/{twoa}")
            print(f"x₂ = {round(-b - sqrt, 2)}/{twoa}")
            
            print(f"\nx₁ = {round((-b + sqrt)/twoa, 2)}")
            print(f"x₂ = {round((-b - sqrt)/twoa, 2)}")
        
        except ValueError:
            #print out it's not solvable
            print("Not solvable!")
            #
        #
    except ValueError:
        print("\nMath Error!")
        input("\npress Enter to continue..")
        clear()
        
#reverse vertex form
def revVertex():
    print("y = ax² + bx + c")
    try:
        x = float(input("\nx: "))
        y = float(input("y: "))
        a = float(input("a: "))
        
        sign1 = "+"
        sign2 = "+"
         
        x *= -1
        ydiva = round(y/a, 2)
        
        if x < 0:
               sign1 = "-"
    
        if ydiva < 0:
               sign2 = "-"
        
        print(f"\ny = {a}[(x {sign1} {math.fabs(x)})² {sign2} {math.fabs(ydiva)}]")
      
        print(f"y = {a}[x² {sign1} {math.fabs(2*x)}x + {x**2} {sign2} {math.fabs(ydiva)}]")
        
        if x**2 + ydiva < 0:
            sign2 = "-"
        else:
            sign2 = "+"
            
        print(f"y = {a}[x² {sign1} {math.fabs(2*x)}x {sign2} {math.fabs(x**2 + ydiva)}]")
        
        if 2*x*a < 0:
            sign1 = "-"
        else:
            sign1 = "+"
            
        if (x**2 + ydiva)*a < 0:
            sign2 = "-"
        else:
            sign2 = "+"
            
        print(f"y = {a}x² {sign1} {math.fabs(2*x*a)}x {sign2} {round(math.fabs((x**2 + ydiva)*a), 2)}")
    
    except ValueError:
        print("\nMath Error!")
        input("\npress Enter to continue..")
        clear()
        
def quadratics():
    form_type = input("rev vertex(rv) or vertex(v): ")
    
    if form_type == "rv":
        revVertex()
    elif form_type == "v":
        Vertex()