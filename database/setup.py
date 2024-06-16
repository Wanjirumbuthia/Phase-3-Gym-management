from connection import CONN, CURSOR

def create_tables():
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS gym_members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(10),
            last_name VARCHAR(10),
            age INTEGER,
            gender TEXT,
            phone_number VARCHAR(10),
            email TEXT
        );
    ''')

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS gym_membership_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20),
            payment INTEGER,
            description TEXT,
            duration VARCHAR(8)
        );
    ''')

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            membership_plan_name TEXT,
            payment_method TEXT,
            amount INTEGER,
            payment_date DATE,
            FOREIGN KEY (member_id) REFERENCES gym_members(id),
            FOREIGN KEY (membership_plan_name) REFERENCES gym_membership_plans(name)
        );
    ''')

    CONN.commit()

# Call the function to create tables
create_tables()
