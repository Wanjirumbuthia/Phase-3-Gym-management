from models.gym_member import GymMember
from models.gym_membership_plan import GymMembershipPlan
from models.payment import Payment

def exit_program():
    print("Exiting program.")
    exit()

def list_gym_members():
    members = GymMember.get_all()
    for member in members:
        print(member)

def find_gym_member_by_name():
    name = input("Enter the member's name: ")
    member = GymMember.find_by_name(name)
    if member:
        print(member)
    else:
        print(f"No gym member found with name {name}")

def find_gym_member_by_id():
    member_id = int(input("Enter the member's id: "))
    member = GymMember.find_by_id(member_id)
    if member:
        print(member)
    else:
        print(f"No gym member found with id {member_id}")

def create_gym_member():
    first_name = input("Enter the member's first name: ")
    last_name = input("Enter the member's last name: ")
    age = int(input("Enter the member's age: "))
    gender = input("Enter the member's gender (Male, Female, Other): ")
    phone_number = input("Enter the member's phone number: ")
    email = input("Enter the member's email: ")
    member = GymMember.create(first_name, last_name, age, gender, phone_number, email)
    print(f"Created gym member: {member}")

def update_gym_member():
    member_id = int(input("Enter the member's id to update: "))
    member = GymMember.find_by_id(member_id)
    if member:
        member.first_name = input("Enter the member's new first name: ")
        member.last_name = input("Enter the member's new last name: ")
        member.age = int(input("Enter the member's new age: "))
        member.gender = input("Enter the member's new gender (Male, Female, Other): ")
        member.phone_number = input("Enter the member's new phone number: ")
        member.email = input("Enter the member's new email: ")
        member.update()
        print(f"Updated gym member: {member}")
    else:
        print(f"No gym member found with id {member_id}")

def delete_gym_member():
    member_id = int(input("Enter the member's id to delete: "))
    member = GymMember.find_by_id(member_id)
    if member:
        member.delete()
        print(f"Deleted gym member with id {member_id}")
    else:
        print(f"No gym member found with id {member_id}")

def list_gym_membership_plans():
    plans = GymMembershipPlan.get_all()
    for plan in plans:
        print(plan)

def find_gym_membership_plan_by_name():
    name = input("Enter the plan name: ")
    plan = GymMembershipPlan.find_by_name(name)
    if plan:
        print(plan)
    else:
        print(f"No gym membership plan found with name {name}")

def find_gym_membership_plan_by_id():
    plan_id = int(input("Enter the plan id: "))
    plan = GymMembershipPlan.find_by_id(plan_id)
    if plan:
        print(plan)
    else:
        print(f"No gym membership plan found with id {plan_id}")

def create_gym_membership_plan():
    name = input("Enter the plan name: ")
    payment = int(input("Enter the plan payment amount: "))
    description = input("Enter the plan description: ")
    duration = input("Enter the plan duration (e.g., 1 month, 2 months): ")
    plan = GymMembershipPlan.create(name, payment, description, duration)
    print(f"Created gym membership plan: {plan}")

def update_gym_membership_plan():
    plan_id = int(input("Enter the plan id to update: "))
    plan = GymMembershipPlan.find_by_id(plan_id)
    if plan:
        plan.name = input("Enter the plan's new name: ")
        plan.payment = int(input("Enter the plan's new payment amount: "))
        plan.description = input("Enter the plan's new description: ")
        plan.duration = input("Enter the plan's new duration (e.g., 1 month, 2 months): ")
        plan.update()
        print(f"Updated gym membership plan: {plan}")
    else:
        print(f"No gym membership plan found with id {plan_id}")

def delete_gym_membership_plan():
    plan_id = int(input("Enter the plan id to delete: "))
    plan = GymMembershipPlan.find_by_id(plan_id)
    if plan:
        plan.delete()
        print(f"Deleted gym membership plan with id {plan_id}")
    else:
        print(f"No gym membership plan found with id {plan_id}")

def list_payments():
    payments = Payment.get_all()
    for payment in payments:
        print(payment)

def find_payments_by_member_id():
    member_id = int(input("Enter the member's id: "))
    payments = Payment.find_by_member_id(member_id)
    if payments:
        for payment in payments:
            print(payment)
    else:
        print(f"No payments found for member id {member_id}")

def find_payments_by_membership_plan_name():
    plan_name = input("Enter the membership plan name: ")
    payments = Payment.find_by_membership_plan_name(plan_name)
    if payments:
        for payment in payments:
            print(payment)
    else:
        print(f"No payments found for membership plan {plan_name}")

def create_payment():
    member_id = int(input("Enter the member's id: "))
    membership_plan_name = input("Enter the membership plan name: ")
    payment_method = input("Enter the payment method: ")
    amount = int(input("Enter the payment amount: "))
    payment_date = input("Enter the payment date (YYYY-MM-DD): ")
    payment = Payment.create(member_id, membership_plan_name, payment_method, amount, payment_date)
    print(f"Created payment: {payment}")

def update_payment():
    payment_id = int(input("Enter the payment id to update: "))
    payment = Payment.find_by_id(payment_id)
    if payment:
        payment.member_id = int(input("Enter the new member id: "))
        payment.membership_plan_name = input("Enter the new membership plan name: ")
        payment.payment_method = input("Enter the new payment method: ")
        payment.amount = int(input("Enter the new payment amount: "))
        payment.payment_date = input("Enter the new payment date (YYYY-MM-DD): ")
        payment.update()
        print(f"Updated payment: {payment}")
    else:
        print(f"No payment found with id {payment_id}")

def delete_payment():
    payment_id = int(input("Enter the payment id to delete: "))
    payment = Payment.find_by_id(payment_id)
    if payment:
        payment.delete()
        print(f"Deleted payment with id {payment_id}")
    else:
        print(f"No payment found with id {payment_id}")
