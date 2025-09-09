def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

# Accessing command line args
import sys

num1 = sys.argv[1]
operation = sys.argv[2]
num2 = sys.argv[3]

if operation == "add":
 print(f"Addition of {num1} and {num2} is {add(int(num1), int(num2))}")
