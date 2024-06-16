from models.gym_member import GymMember
from models.gym_membership_plan import GymMembershipPlan
from models.payment import Payment


GymMember.drop_table()
GymMember.create_table()
    
GymMembershipPlan.drop_table()
GymMembershipPlan.create_table()
    
Payment.drop_table()
Payment.create_table()

member1 = GymMember.create("Nilla", "Kwamboka", 28, "female", "1234567890", "nilla@gmail.com")
member2 = GymMember.create("Tom", "Holland", 40, "male", "4567890123", "tom@gmail.com")
member3 = GymMember.create("Jane", "Nduta", 25, "female", "9876543210", "jane@gmail.com")
member4 = GymMember.create("Justin", "Tim", 30, "male", "0154658438", "justin@gmail.com")
member5 = GymMember.create("Hakilah", "Tshiku", 20, "male", "4567890123", "hakilah@gmail.com")
print(member1)
print(member2)

   
plan1 = GymMembershipPlan.create("Basic Plan", 250, "Basic gym access", "1 month")
plan2 = GymMembershipPlan.create("Silver Plan", 500, "gym access and selected group classes", "2 month")
plan3 = GymMembershipPlan.create("Gold Plan", 1000, "full gym access, classes, and personal training sessions", "3 month")
plan4 = GymMembershipPlan.create("Premium Plan", 2000, "unlimited access to all facilities, group classes, and personal training", "6 month")
plan5 = GymMembershipPlan.create("Silver Plan", 500, "Includes gym access and selected group classes", "2 month")
print(plan1)
print(plan2)


payment1 = Payment.create(member1.id, plan1.name, "Credit Card", 250, "2024-06-01")
payment2 = Payment.create(member2.id, plan2.name, "Mpesa", 500, "2024-04-15")
payment3 = Payment.create(member3.id, plan3.name, "Debit Card", 1000, "2024-06-12")
payment4 = Payment.create(member4.id, plan4.name, "Bank Transfer",2000, "2024-05-2")
payment5 = Payment.create(member5.id, plan5.name, "Mpesa", 500, "2024-03-13")
print(payment1)
print(payment2)



   