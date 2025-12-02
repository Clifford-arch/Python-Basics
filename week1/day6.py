"""
Today's Mission:
Build a simple contact book that stores names and phone numbers

"""
######################################
person={
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person["name"])
print(person.get("age"))

######################################
users = {
    "alice": "password123",
    "bob": "secret456"
}

username = input("Username: ")
if username not in users:
    print("Invalid Username")
else:
    password = input("Password: ")
    if users[username] == password:
        print("Login successful!")
    else:
        print("Invalid credentials")


######################################


phone_dictionary = {} 

def Perform():
    while True:
        ops=input("Operations: 1) Add  2) Remove 3) print 4) exit")
        match ops:
            case "1":
                name=input("Name: ")
                number=input("Number: ")
                phone_dictionary.update({name:number})
            case"2":
                name=input("Name: ")
                phone_dictionary.pop(name)
            case "3":
                print(f"phone dictionary: ${phone_dictionary}")

            case "4":
                print("exiting....")
                break


Perform()
