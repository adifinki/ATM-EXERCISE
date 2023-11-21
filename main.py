import json


def login() -> int:

    """
    This function asks the user for his customer ID and password
    return: customer ID when the password is correct
    """

    target_id = int(input("Enter your customer ID"))
    with open("customers.json", 'r') as customers_file:
        customers_data = json.load(customers_file)
        list_of_costumers_dicts = customers_data["customers"]
        for customer in list_of_costumers_dicts:
            if customer["customer_id"] == target_id:
                password = int(input("Enter your password"))
            while customer["password"] != password:
                password = int(input("Enter your password"))
            return target_id
        else:
            print("Invalid customer ID")
            return login()


def withdrawal(customer_id: int) -> None:
    """
    This function asks the user for the amount he wishes to withdraw
    param: customer_id: the customer ID of the user who wishes to withdraw money
    return: None
    """
    with open("customers.json", 'r') as customers_file:
        customers_data = json.load(customers_file)
        list_of_costumers_dicts = customers_data["customers"]
        for customer in list_of_costumers_dicts:
            if customer["customer_id"] == customer_id:
                amount = int(input("Enter the amount you wish to withdraw"))
                while amount > customer["balance"]:
                    amount = int(input("Enter the amount you wish to withdraw"))
                customer["balance"] -= amount
                print(f"Your new balance is {customer['balance']}")
                with open("customers.json", 'w') as customers_file_new:
                    json.dump(customers_data, customers_file_new, indent=4)
                return
        else:
            print("Invalid customer ID")
            return withdrawal(login())


def deposit(customer_id: int) -> None:
    """
    This function asks the user for the amount he wishes to deposit
    param: customer_id: the customer ID of the user who wishes to deposit money
    return: None
    """
    with open("customers.json", 'r') as customers_file:
        customers_data = json.load(customers_file)
        list_of_costumers_dicts = customers_data["customers"]
        for customer in list_of_costumers_dicts:
            if customer["customer_id"] == customer_id:
                amount = int(input("Enter the amount you wish to deposit"))
                customer["balance"] += amount
                print(f"Your new balance is {customer['balance']}")
                with open("customers.json", 'w') as customers_file_new:
                    json.dump(customers_data, customers_file_new, indent=4)
                return
        else:
            print("Invalid customer ID")
            return deposit(login())


def change_password(customer_id: int) -> None:
    """
    This function asks the user for his new password and changes it
    param: customer_id: the customer ID of the user who wishes to change his password
    return: None
    """
    with open("customers.json", 'r') as customers_file:
        customers_data = json.load(customers_file)
        list_of_costumers_dicts = customers_data["customers"]
        for customer in list_of_costumers_dicts:
            if customer["customer_id"] == customer_id:
                password = int(input("Enter your new password"))
                customer["password"] = password
                print("Your password has been changed")
                with open("customers.json", 'w') as customers_file_new:
                    json.dump(customers_data, customers_file_new, indent=4)
                return
        else:
            print("Invalid customer ID")
            return change_password(login())


def balance(customer_id: int) -> None:
    """
    This function prints the balance of the user
    param: customer_id: the customer ID of the user who wishes to see his balance
    return: None
    """
    with open("customers.json", 'r') as customers_file:
        customers_data = json.load(customers_file)
        list_of_costumers_dicts = customers_data["customers"]
        for customer in list_of_costumers_dicts:
            if customer["customer_id"] == customer_id:
                print(f"Your balance is {customer['balance']}")
                return
        else:
            print("Invalid customer ID")
            return balance(login())


def main() -> None:
    """
    This function is the main function of the program, it calls the other functions
    return: None
    """
    customer_id = login()
    print("Welcome to the ATM")
    while True:
        print("What would you like to do?")
        print(" 1. Withdrawal")
        print(" 2. Deposit")
        print(" 3. Change password")
        print(" 4. Balance")
        print("-1. Exit")
        choice = int(input())
        match choice:
            case 1:
                withdrawal(customer_id)
            case 2:
                deposit(customer_id)
            case 3:
                change_password(customer_id)
            case 4:
                balance(customer_id)
            case -1:
                print("Thank you for using our ATM")
                break
            case _:
                print("Invalid choice")


if __name__ == '__main__':
    main()


