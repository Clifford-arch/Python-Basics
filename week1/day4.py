## Handling multiple items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

print("First fruit:", fruits[0])
print("All fruits:", fruits)

# Looping through lists
for fruit in fruits:
    print(f"I like {fruit}")

for number in range(1, 6):
    print(number * number)  # Squares


""" Checklist """
items = []

n = int(input("Number of items: "))
for i in range(n):
    items.append(input())

def printlist():
    print("\nCurrent list:")
    for x in items:
        print("-", x)
    print("")

def itemops():
    while True:
        print("Operations: 1. Add  2. Remove  3. Print  4. Exit")
        op = input("Choose operation: ")

        match op:
            case "1":
                items.append(input("Enter item to add: "))
            case "2":
                val = input("Enter item to remove: ")
                if val in items:
                    items.remove(val)
                else:
                    print("Item not found.")
            case "3":
                printlist()
            case "4":
                print("Exiting...")
                break
            case _:
                print("Invalid operation.\n")

itemops()


