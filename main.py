import json
from typing import Callable


def login() -> str:

    """
    This function asks the user for his customer ID and password
    """
    target_id = None
    customers_data = get_customers_data()
    while target_id not in customers_data:
        target_id = input("Enter valid customer ID")
    password = None
    while customers_data[target_id]["password"] != password:
        password = input("Enter your password")
    return target_id


def get_customers_data():
    """
    This function opens the file customers.json and loads it into a dictionary
    return: customer data
    """
    with open("customers.json", 'r') as customers_file:
        return json.load(customers_file)


def update_customers_data(customers_data):
    """
    This function opens the file customers.json and dumps the dictionary into it
    param: customers_data: the dictionary that contains the data of the customers
    return: None
    """
    with open("customers.json", 'w') as customers_file_new:
        json.dump(customers_data, customers_file_new, indent=4)


def withdrawal(customer_id: str) -> None:
    """
    This function asks the user for the amount he wishes to withdraw
    param: customer_id: the customer ID of the user who wishes to withdraw money
    return: None
    """
    customers_data = get_customers_data()
    amount = float('inf')
    customer = customers_data[customer_id]
    while amount > customer['balance']:
        amount = int(input("Enter the amount you wish to withdraw"))
    customer['balance'] -= amount
    print(f"Your new balance is {customer['balance']}")
    update_customers_data(customers_data)


def deposit(customer_id: str) -> None:
    """
    This function asks the user for the amount he wishes to deposit
    param: customer_id: the customer ID of the user who wishes to deposit money
    return: None
    """
    customers_data = get_customers_data()
    customer = customers_data[customer_id]
    amount = int(input("Enter the amount you wish to deposit"))
    customer["balance"] += amount
    print(f"Your new balance is {customer['balance']}")
    update_customers_data(customers_data)


def change_password(customer_id: str) -> None:
    """
    This function asks the user for his new password and changes it
    param: customer_id: the customer ID of the user who wishes to change his password
    return: None
    """
    customers_data = get_customers_data()
    password = input("Enter your new password")
    customers_data[customer_id]["password"] = password
    update_customers_data(customers_data)
    print("Your password has been changed")


def balance(customer_id: str) -> None:
    """
    This function prints the balance of the user
    param: customer_id: the customer ID of the user who wishes to see his balance
    return: None
    """
    customers_data = get_customers_data()
    print(f"Your balance is {customers_data[customer_id]['balance']}")


def exit_atm(_) -> None:
    """
    This function exits the program
    return: None
    """
    print("Thank you for using our ATM")
    exit()


def main() -> None:
    """
    This function is the main function of the program, it calls the other functions
    return: None
    """
    customer_id = login()
    actions: dict[str, tuple[str, Callable[[str], None]]] = {
        '1': ("withdrawal", withdrawal),
        '2': ("deposit", deposit),
        '3': ("change password", change_password),
        '4': ("balance", balance),
        '-1': ("exit", exit_atm)}
    print("Welcome to the ATM")
    while True:
        for action_index, (name, _) in actions.items():
            print(f'{("  " + action_index)[-2:]} {name}')
        choice = None
        while choice not in actions:
            choice = input("Enter your choice")
        actions[choice][1](customer_id)


if __name__ == '__main__':
    main()
