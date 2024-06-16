# Phase 3 Project 

# PROJECT TITLEGYM MANAGEMENT SYSTEM

#### Date, 2024/06/15

#### By *Mbuthia Wanjiru Thuo*

## Description
The Gym Management System  is an application designed to manage gym memberships, membership plans, and payments efficiently. This project allows gym administrators to perform various tasks, including adding and managing gym members, creating and deleting membership plans, and recording and viewing payments. 

## Features

It is divided into three main categoriesGym Member, Membership Plan , and Payment.

### Gym Member Management

1. **List all gym members**
2. **Find gym member by ID**
3. **Create a new gym member**.
4. **Update a gym member**
5. **Delete a gym member**

### Membership Plan Management

1. **List all gym membership plans**
2. **Find gym membership plan by name** 
3. **Find gym membership plan by ID**
4. **Create a new gym membership plan** 
5. **Update a gym membership plan**
6. **Delete a gym membership plan** 

### Payment Management

1. **List all payments**
2. **Find payments by member ID**.
3. **Find payments by membership plan name**
4. **Create a new payment**
5. **Update a payment**
6. **Delete a payment**

## Technologies Used

- **Python**
- **SQLite**
- **Pipenv**

## Project Structure
.
├── database
│   ├── __init__.py
│   ├── connection.py
│   └── setup.py
├── models
│   ├── __init__.py
│   ├── gym_member.py
│   ├── gym_membership_plan.py
│   └── payment.py
├── cli.py
├── gym.db
├── debug.py
├── helpers.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── seed.py