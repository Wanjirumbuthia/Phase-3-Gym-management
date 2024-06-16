from helpers import (
    exit_program,
    list_gym_members,
    find_gym_member_by_id,
    create_gym_member,
    update_gym_member,
    delete_gym_member,
    list_gym_membership_plans,
    find_gym_membership_plan_by_name,
    find_gym_membership_plan_by_id,
    create_gym_membership_plan,
    update_gym_membership_plan,
    delete_gym_membership_plan,
    list_payments,
    find_payments_by_member_id,
    find_payments_by_membership_plan_name,
    create_payment,
    update_payment,
    delete_payment,
)

def print_menu(menu):
    """Print the specified menu"""
    print(menu)

def main():
    current_menu = "main"
    
    while True:
        if current_menu == "main":
            main_menu()
            choice = input("Enter your choice: ")
            
            if choice == "1":
                current_menu = "gym_member"
            elif choice == "2":
                current_menu = "membership_plan"
            elif choice == "3":
                current_menu = "payment"
            elif choice == "4":
                exit_program()
            else:
                print("Invalid choice. Please try again.")
        
        elif current_menu == "gym_member":
            gym_member_menu()
            current_menu = "main"
        
        elif current_menu == "membership_plan":
            membership_plan_menu()
            current_menu = "main"
        
        elif current_menu == "payment":
            payment_menu()
            current_menu = "main"
def main_menu():
    menu = """
       Gym Management System
    Please select a category:
    1. Gym Member
    2. Membership Plan
    3. Payment
    4. Exit the system
    """
    print_menu(menu)  

def gym_member_menu():
    while True:
        menu = """
        Gym Member Menu:
        1. List all gym members
        2. Find gym member by ID
        3. Create a new gym member
        4. Update a gym member
        5. Delete a gym member
        6. Return to main menu
        """
        print_menu(menu)
        choice = input("Enter your choice: ")

        if choice == '1':
            list_gym_members()
        elif choice == '2':
            find_gym_member_by_id()
        elif choice == '3':
            create_gym_member()
        elif choice == '4':
            update_gym_member()
        elif choice == '5':
            delete_gym_member()
        elif choice == '6':
            return

def membership_plan_menu():
    while True:
        menu = """
        Membership Plan Menu:
        1. List all gym membership plans
        2. Find gym membership plan by name
        3. Find gym membership plan by ID
        4. Create a new gym membership plan
        5. Update a gym membership plan
        6. Delete a gym membership plan
        7. Return to main menu
        """
        print_menu(menu)
        choice = input("Enter your choice: ")

        if choice == '1':
            list_gym_membership_plans()
        elif choice == '2':
            find_gym_membership_plan_by_name()
        elif choice == '3':
            find_gym_membership_plan_by_id()
        elif choice == '4':
            create_gym_membership_plan()
        elif choice == '5':
            update_gym_membership_plan()
        elif choice == '6':
            delete_gym_membership_plan()
        elif choice == '7':
            return

def payment_menu():
    while True:
        menu = """
        Payment Menu:
        1. List all payments
        2. Find payments by member ID
        3. Find payments by membership plan name
        4. Create a new payment
        5. Update a payment
        6. Delete a payment
        7. Return to main menu
        """
        print_menu(menu)
        choice = input("Enter your choice: ")

        if choice == '1':
            list_payments()
        elif choice == '2':
            find_payments_by_member_id()
        elif choice == '3':
            find_payments_by_membership_plan_name()
        elif choice == '4':
            create_payment()
        elif choice == '5':
            update_payment()
        elif choice == '6':
            delete_payment()
        elif choice == '7':
            return

# Start the program
if __name__ == "__main__":
    main()        