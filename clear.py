#!/usr/bin/env python3

from os import system, name

#clear function
def clear():
	system('clear')
	if name == 'nt': 
		_ = system('cls')
