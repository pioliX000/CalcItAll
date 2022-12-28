#!/usr/bin/env python3

from trigonometry import costher, sinther
from pq import pq
from quadratic import quadratics
from clear import clear
from linear_equation import linear_solve

clear()

def HAHALMAO():
	try:
		def t():
			lmao = input("\nCosine Theorem(ct), Sine Theorem(st) or back?: ")
			if lmao == "ct":
				clear()
				costher()
			elif lmao == "st":
				clear()
				sinther()
			elif lmao == "back":
				clear()
				lol()
			else:
				print("bruh")
				t()

		def ta():
			t()
			XD = input("\nAgain?(Y/n): ")
			if XD == "n":
				clear()
				lol()
			else:
				clear()
				ta()
				
		def q():
			quadratics()
			XD = input("\nAgain?(Y/n): ")
			if XD == "n":
				clear()
				lol()
			else:
				clear()
				q()
		
		def lin():
			linear_solve()
			XD = input("\nAgain?(Y/n): ")
			if XD == "n":
				clear()
				lol()
			else:
				clear()
				lin()		
				
		def pqa():
			pq()
			XD = input("\nAgain?(Y/n): ")
			if XD == "n":
				clear()
				lol()
			else:
				clear()
				pqa()

		def lol():
			xdlol = input("\ntrigonometry(t), pq(pq), quadratics(q), linear functions(l) or exit?: ")
			if xdlol == "pq":
				clear()
				pqa()	
			elif xdlol == "t":
				clear()
				ta()
			elif xdlol == "l":
			    clear()
			    lin()
			elif xdlol == "q":
			    clear()
			    q()
			elif xdlol == "exit":
				clear()
				exit()
			elif xdlol == "credits":
				clear()
				print("Made by pioliX000")
				lol()

		while True:
			lol()

	except KeyboardInterrupt:
		stfu = input("\n\nexit? (Y/n): ")
		if stfu == "n":
			clear()
			HAHALMAO()
		else:
			clear()
			print("Made my pioliX000")
			
HAHALMAO()