#Create a calculator that requests 2 numbers from the user and then perform addition, subtraction, multiplication, and division
#The output should show or print what kind of operation was made and then the answer
#This project is in-line with learning the ff: print(), input(), variables, and data types

print("Simple Calculator: Performing all operations using two numbers")

#Create a variable that will store the input value of the user
number_1 = float(input("Please enter the first number: ")) #float is used as a data type since I dont know what number the user will input
number_2 = float(input("Please enter the second number: "))

#print all the values of the number based on each math operation
print("Addition: ", number_1 + number_2)
print("Subtraction: ", number_1 - number_2)
print("Multiplication: ", number_1 * number_2)
print("Division: ", number_1 / number_2)
