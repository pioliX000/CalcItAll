#!/usr/bin/env python3

from trigonometry import costher, sinther
from pq import pq
from quadratic import quadratics
from clear import clear
from linear_equation import linear_solve
from median_differential import median_diff

clear()

def main_menu():
    try:
        def trigonometry_menu():
            try:
                def perform_trigonometry_operations():
                    choice = input("\nCosine Theorem(ct), Sine Theorem(st) or back?: ")
                    if choice == "ct":
                        clear()
                        costher()
                    elif choice == "st":
                        clear()
                        sinther()
                    elif choice == "back":
                        clear()
                        main_menu()
                    else:
                        print("Invalid choice. Try again.")
                        perform_trigonometry_operations()

                def repeat_trigonometry_menu():
                    perform_trigonometry_operations()
                    repeat = input("\nAgain?(Y/n): ")
                    if repeat.lower() == "n":
                        clear()
                        main_menu()
                    else:
                        clear()
                        repeat_trigonometry_menu()

                repeat_trigonometry_menu()

            except KeyboardInterrupt:
                exit_prompt = input("\n\nExit? (Y/n): ")
                if exit_prompt.lower() == "n":
                    clear()
                    main_menu()
                else:
                    clear()
                    print("Made by pioliX000")

        def pq_menu():
            pq()
            repeat = input("\nAgain?(Y/n): ")
            if repeat.lower() == "n":
                clear()
                main_menu()
            else:
                clear()
                pq_menu()

        def quadratic_menu():
            quadratics()
            repeat = input("\nAgain?(Y/n): ")
            if repeat.lower() == "n":
                clear()
                main_menu()
            else:
                clear()
                quadratic_menu()

        def linear_menu():
            linear_solve()
            repeat = input("\nAgain?(Y/n): ")
            if repeat.lower() == "n":
                clear()
                main_menu()
            else:
                clear()
                linear_menu()

        def median_differential_menu():
            clear()
            median_diff()
            repeat = input("\nAgain?(Y/n): ")
            if repeat.lower() == "n":
                clear()
                main_menu()
            else:
                clear()
                median_differential_menu()

        def display_menu():
            user_choice = input("\nTrigonometry(t), PQ(pq), Quadratics(q), Linear Functions(l), Median Differential(m) or exit?: ")
            if user_choice == "pq":
                clear()
                pq_menu()    
            elif user_choice == "t":
                clear()
                trigonometry_menu()
            elif user_choice == "l":
                clear()
                linear_menu()
            elif user_choice == "q":
                clear()
                quadratic_menu()
            elif user_choice == "exit":
                clear()
                exit()
            elif user_choice == "m":
                clear()
                median_differential_menu()
            elif user_choice == "credits":
                clear()
                print("Made by pioliX000")
                display_menu()

        while True:
            display_menu()

    except KeyboardInterrupt:
        exit_prompt = input("\n\nExit? (Y/n): ")
        if exit_prompt.lower() == "n":
            clear()
            main_menu()
        else:
            clear()
            print("Made by pioliX000")

main_menu()
