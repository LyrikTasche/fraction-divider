#!/usr/bin/env python3

#Coded by @LyrikTasche - Strings and Variable names in german

print("If these aren't mixed fractions then just enter zeros on the next two questions")
zahl1 = int(input("Enter number 1: "))
zahl2 = int(input("Enter number 2: "))

zähler1 = int(input("Enter Counter 1: "))
zähler2 = int(input("Enter Counter 2: "))
nenner1 = int(input("Enter denominator 1: "))
nenner2 = int(input("Enter denominator 2: "))

umwandeln1 = zahl1*nenner1+zähler1
umwandeln2 = zahl2*nenner2+zähler2
output1 = umwandeln1*nenner2
output2 = umwandeln2*nenner1

print(output1)
print("/")
print(output2)

if output1 > output2:
	

		
	
		
