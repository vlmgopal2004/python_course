atm_user_details = {
    1: {"acc_num": 123456, "pin": 9849, "bal": 500, "view_trans": []},
    2: {"acc_num": 234567, "pin": 9090, "bal": 200, "view_trans": []},
    3: {"acc_num": 987654, "pin": 1234, "bal": 250, "view_trans": []},
    4: {"acc_num": 654321, "pin": 8790, "bal": 500, "view_trans": []}
}

print("Welcome to the ATM")
acc_num = int(input("Enter your account number: "))
pin = int(input("Enter your PIN: "))

for i in atm_user_details:
    if atm_user_details[i]["acc_num"] == acc_num and atm_user_details[i]["pin"] == pin:
        print("Login Successful")
        while True:
            print("\nATM MENU")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Transactions")
            print("5. Exit")

            user_in = int(input("Enter Your choice: "))

            if user_in == 1:
                print(f"Your Balance: {atm_user_details[i]['bal']}")
            elif user_in == 2:
                dep = int(input("Enter your deposit amount: "))
                atm_user_details[i]["view_trans"].append(f"Deposit: {dep}")
                atm_user_details[i]["bal"] += dep
                print(f"You deposited amount {dep}")
            elif user_in == 3:
                withdraw = int(input("Enter the withdraw amount: "))
                if withdraw > atm_user_details[i]["bal"]:
                    print("Insufficient Balance!")
                else:
                    atm_user_details[i]["view_trans"].append(f"Withdraw: {withdraw}")
                    atm_user_details[i]["bal"] -= withdraw
                    print(f"You withdrew amount {withdraw}")
            elif user_in == 4:
                print("Your transactions:")
                for trans in atm_user_details[i]["view_trans"]:
                    print(trans)
            elif user_in == 5:
                print("Thank You for using the ATM!")
                break
            else:
                print("Invalid choice. Please try again.")
        break
else:
    print("Invalid account number or PIN.")
