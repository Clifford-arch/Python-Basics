"""
Today's Mission:
Build a mad libs game that asks for:

Adjective

Noun

Verb

Prints a funny story using them

"""
#interactive programming
name=input("What's your name?")
age=input("What's your age?")

print(f'Hello {name}')
print(f'In 5 years time,you will be {int(age)+5} years.')

# String tricks
message = "i am learning python"
print(message.upper())        # I AM LEARNING PYTHON
print(message.title())        # I Am Learning Python

"""mad libs game"""

print("\n Mad Libs Game")
noun=input("Give a noun? ")
adjective=input("Give an adjective? ")
verb=input("Give a verb? ")

print(f'Once a upon there was a {noun}.')
print(f'He was very {adjective}')
print(f'He used to {verb} the horse')
