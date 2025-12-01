"""
Today's Mission:
Create functions for:

Converting Celsius to Fahrenheit

Calculating area of a rectangle

Checking if a number is positive

"""
def greet(name):
    return f"Hello {name}."

def add(a,b):
    return a+b

def even_odd(num):
    if(num%2==0):
        return "even"
    return "odd"

name=input("What's your name?")
print(greet(name))
x, y = input("Values: ").split()
print(add(int(x),int(y)))
num=int(input("What number?"))
print(even_odd(num))


""" Converting Celsius to Fahrenheit / Fahrenheit to Celsius"""

def CTF(Celsius):
    return Celsius*(9/5)+32

def FTC(Fahrenheit):
    return (Fahrenheit-32)*(5/9)

def activity():
    # while True:
        print("Operations: 1. Celsius to Fahrenheit  2. Fahrenheit to Celsius 3. Exit")
        op = input("Choose operation: ")
        match op:
            case "1":
                data=float(input("Data: "))
                print(CTF(data))
            case "2":
                data=float(input("Data: "))
                print(FTC(data))
            case "3":
                print("Existing")
                # break

activity()

"""Area of Rectangle"""
def AreaOfRectangle(l,b):
    return l*b

print(AreaOfRectangle(5,3))

"""Checking if a number is positive"""
def CheckPositive(num):
    if(num>0):
        return f"{num} is positive"
    else:
        return f"{num} is negative"

print(CheckPositive(-2))