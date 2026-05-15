#Create a program that will check if the user is a minor or an adult
#This project is in-line with learning the ff: print(), input(), variables, and data types

print("Welcome to Age Checker. This will check if you are a minor or an adult.")
age_of_user = int(input("How old are you? ")) #Put the data type

if age_of_user <= 18:
	print("You are a minor.")
else:
	print("You are an adult.")