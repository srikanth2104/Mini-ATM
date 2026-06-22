#Initial Data

pin = "1928"
balance = 1000
mini_statement = []

#Function for checking PIN
def check_pin():
    input_pin = input("ENter your PIN: ")
    if input_pin == pin:
        print("Login Successfull!!!")
        return True
    else:
        print("Incorrect PIN")
        return False
    
#Main ATM Function
def mini_atm():
    global pin,balance,mini_statement
    while True:
        print("\n=======ATM Menu=========\n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Mini Statement")
        print("6. Exit")
        
        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Please enter valid option!")
            continue

        if option == 1:
            print(f"Current Balance: ₹{balance}")
            mini_statement.append(f"Checked Balance: ₹{balance}")

        elif option == 2:
            try:
                amount = float(input("Enter amount to deposit: ₹"))
            except ValueError:
                print("Invalid Amount !!!")
                continue

            if amount > 0:
                balance += amount
                print(f"₹{amount} has been deposited successfully")
                print(f"Updated Balance: ₹{balance}")
                mini_statement.append(f"Deposited: ₹{amount} | Balance: {balance}")
            else:
                print("Invalid Amount")
        
        elif option == 3:
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
            except ValueError:
                print("Invalid Amount !")
            

            if amount <= balance:
                if amount > 0:
                    balance -= amount
                    print(f"₹{amount} has been withdrawn successfully")
                    print(f"Updated Balance: ₹{balance}")
                    mini_statement.append(f"Withdrawn: ₹{amount} | Balance: {balance}")
                else:
                    print("Invalid Amount !")
                
            else:
                print("Insufficient Balance !")

        elif option == 4:
            print("\n--------MINI STATEMENT----------\n")
            if len(mini_statement) == 0:
                print("No Transactions yet")
            else:
                for l in mini_statement:
                    print("--> ",l)

        elif option == 5:
            old_pin = input("Enter OLD PIN: ")

            if old_pin == pin:
                new_pin = input("Enter NEW PIN: ")
                confirm_pin = input("Confirm NEW PIN: ")
                if confirm_pin == new_pin:
                    if len(new_pin) == 4 and new_pin.isdigit():
                        pin = new_pin
                        print("PIN changed successfully")
                        mini_statement.append("PIN changed successfully")
                    else:
                        print("PIN must contain exactly 4 digits")
                else:
                    print("PIN mismatched")
            else:
                print("Incorrect OLD PIN")

        elif option == 6:
            print("Thank you for usinf our ATM service")
            print("Exiting System ...")
            break

        else:
            print("Invalid option !")


#Program Start
attempts = 3
while attempts > 0:
    if check_pin():
        mini_atm()
        break

    attempts -= 1
    print(f"Remaining attempts: {attempts}")


if attempts == 0:
    print("Max attempts reached ...")
    print("!!! Account is Locked !!!")

