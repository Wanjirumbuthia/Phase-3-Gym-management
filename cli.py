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
    Welcome to Gym Management System
    Please select a category:
    1. Gym Member Management
    2. Membership Plan Management
    3. Payment Management
    4. Exit the system
    """
    print_menu(menu)          