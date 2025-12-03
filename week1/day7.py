"""
Complete the bank system with:

Deposit money

Withdraw money (check if enough funds)

View balance

"""

accounts={
    "user1":{"password":"pass123","amount":5000},
    "user2":{"password":"pass234","amount":15000}
}

def login():
    username=input("username: ")
    if username not in accounts:
        print("Username Invalid")
        exit()
    password=input("password: ")
    if accounts[username]["password"]==password:
        while True:
            print("Operations that can be done: 1) Deposit 2) Withdraw 3) Print Amount 4) Exit: ")
            ops=input()
            match ops:
                case "1":
                    deposit=float(input("Enter the Value:"))
                    accounts[username]["amount"]=accounts[username]["amount"]+deposit
                case "2":
                    Withdraw=float(input("Enter the value: "))
                    accounts[username]["amount"]=accounts[username]["amount"]-Withdraw
                case "3":
                    print(f"Total Amount: { accounts[username]["amount"]}")
                case "4":
                    break


login()