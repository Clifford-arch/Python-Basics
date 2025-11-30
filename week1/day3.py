""" 
Today's Mission:
Create a number grader (A: 90-100, B: 80-89, etc.)

"""

age = int(input("How old are you? "))

if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're an adult")
else:
    print("You're a senior")

""" Simple password checker """
password = input("Enter password: ")
if password == "secret123":
    print("Access granted!")
else:
    print("Access denied!")

""" Grade Assigner """
marks=input("\nEnter your Marks: ")

if int(marks) > 90:
    print("You have secured S Grade")
elif int(marks) > 80:
    print("You have secured A Grade")
elif int(marks) >70:
    print("You have secured B Grade")
elif int(marks) >60:
    print("You have secured C Grade")
elif int(marks) >50:
    print("You have secured D Grade")
else:
    print("You have secured E Grade and you have no hopes")