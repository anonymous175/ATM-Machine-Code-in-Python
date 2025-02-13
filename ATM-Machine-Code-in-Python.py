import time

print("\n----------------------------Welcome to the Anonymous Bank-------------------------------")
print("\nPlease Insert your ATM Card")

time.sleep(3)  # Simulating card reading delay

pin = 1234  # Default PIN
balance = 200  # Initial balance
attempts = 4  # Max attempts

for i in range(attempts):
    pin_input = int(input("\nEnter your 4-DIGIT PIN: "))
    
    if pin_input == pin:
        print("\nAccess Granted. Welcome!")
        
        while True:
            print('''
            Choose an option:
            1. Add Money
            2. Withdraw Money
            3. Check Balance
            4. Exit
            ''')

            option = int(input("Choose an option: "))

            # **Deposit Money**
            if option == 1:
                money = int(input("Enter amount to deposit: "))
                balance += money
                print(f"\nNow your balance is ${balance}")

                # Log transaction
                with open("transactions.txt", "a") as file:
                    file.write(f"Deposit: ${money} | Balance: ${balance}\n")

                print("Thanks for visiting our bank.")

            # **Withdraw Money**
            elif option == 2:
                money = int(input("Enter amount to withdraw: "))
                if money <= balance:
                    balance -= money
                    print(f"\nYou withdrew ${money}.")
                    print(f"Remaining balance: ${balance}")

                    # Log transaction
                    with open("transactions.txt", "a") as file:
                        file.write(f"Withdraw: ${money} | Balance: ${balance}\n")

                else:
                    print("\nInsufficient balance!")
                
                print("Thanks for visiting our bank.")

            # **Check Balance**
            elif option == 3:
                print(f"\nYour current balance is: ${balance}")

                # Log transaction
                with open("transactions.txt", "a") as file:
                    file.write(f"Balance Check: $0 | Balance: ${balance}\n")

                print("Thanks for visiting our bank.")

            # **Exit**
            elif option == 4:
                print("\nYou have exited the ATM.")
                print("Thanks for visiting our bank.")
                break

            else:
                print("\nInvalid Option! Please choose again.")
        
        break  # Exit the outer loop once the user logs in and finishes transactions

    else:
        print("\nIncorrect PIN. Try again.")
        if i == attempts - 1:
            print("\nToo many failed attempts! Your account is locked.")
            with open("transactions.txt", "a") as file:
                file.write("Failed Login Attempt\n")
