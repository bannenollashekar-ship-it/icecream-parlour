balance = 10000
pin = 1234
name= "shekar"
city="hyderabd"
entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    while True:
        print("\n---- ATM Menu ----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Your Balance is:", balance)

        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Amount Deposited Successfully")

        elif choice == '3':
            amount = float(input("Enter withdraw amount: "))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash")
            else:
                print("Insufficient Balance")

        elif choice == '4':
            print("Thank you for using ATM")
            break

        else:
            print("Invalid Option")

else:
    print("Incorrect PIN")