#!/usr/bin/env python3

#Coded by @LyrikTasche - Strings and Variable names in german

#Ask for the fraction
print("If these aren't mixed fractions then just enter zeros on the next two questions")
zahl1 = int(input("Enter number 1: "))
zahl2 = int(input("Enter number 2: "))

zähler1 = int(input("Enter Counter 1: "))
zähler2 = int(input("Enter Counter 2: "))
nenner1 = int(input("Enter denominator 1: "))
nenner2 = int(input("Enter denominator 2: "))

#Calculate the results
umwandeln1 = zahl1*nenner1+zähler1
umwandeln2 = zahl2*nenner2+zähler2
output1 = umwandeln1*nenner2
output2 = umwandeln2*nenner1

#Print the results
print(output1, end=""),
print("/", end=""),
print(output2)

#Normal Fraction -> Mixed Fraction
if output1 > output2:
	sus1 = int(output1//output2)
	sus2 = int(sus1*output2)
	sus3 = int(sus2 - output1)
	
	#Print the mixed fraction
	print(" ", sus3)
	print(sus1)
	print(" ", output2)
