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

def print_menu():
    menu = """
    1. List all gym members
    2. Find gym member by ID
    3. Create a new gym member
    4. Update a gym member
    5. Delete a gym member
    6. List all gym membership plans
    7. Find gym membership plan by name
    8. Find gym membership plan by ID
    9. Create a new gym membership plan
    10. Update a gym membership plan
    11. Delete a gym membership plan
    12. List all payments
    13. Find payments by member ID
    14. Find payments by membership plan name
    15. Create a new payment
    16. Update a payment
    17. Delete a payment
    18. Exit
    """
    print(menu)

def main():
    while True:
        print_menu()
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
            list_gym_membership_plans()
        elif choice == '7':
            find_gym_membership_plan_by_name()
        elif choice == '8':
            find_gym_membership_plan_by_id()
        elif choice == '9':
            create_gym_membership_plan()
        elif choice == '10':
            update_gym_membership_plan()
        elif choice == '11':
            delete_gym_membership_plan()
        elif choice == '12':
            list_payments()
        elif choice == '13':
            find_payments_by_member_id()
        elif choice == '14':
            find_payments_by_membership_plan_name()
        elif choice == '15':
            create_payment()
        elif choice == '16':
            update_payment()
        elif choice == '17':
            delete_payment()
        elif choice == '18':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
