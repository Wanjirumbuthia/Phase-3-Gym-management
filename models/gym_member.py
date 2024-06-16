import sqlite3

CONN = sqlite3.connect('gym.db')
CURSOR = CONN.cursor()


class GymMember:

    all = {}

    def __init__(self, first_name, last_name, age, gender, phone_number, email, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return (
            f"<GymMember {self.id}: {self.first_name} {self.last_name}, Age: {self.age}, " +
            f"Gender: {self.gender}, Phone: {self.phone_number}, Email: {self.email}>"
        )

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name) <= 10:
            self._first_name = first_name
        else:
            raise ValueError("First name must be a string with a maximum of 10 characters")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name) <= 10:
            self._last_name = last_name
        else:
            raise ValueError("Last name must be a string with a maximum of 10 characters")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise ValueError("Age must be a positive integer")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and gender in {"male", "female", "other"}:
            self._gender = gender
        else:
            raise ValueError("Gender must be 'male', 'female', or 'other'")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if isinstance(phone_number, str) and len(phone_number) == 10:
            self._phone_number = phone_number
        else:
            raise ValueError("Phone number must be a string of 10 characters")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self._email = email
        else:
            raise ValueError("Email must be a string")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of GymMember instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS gym_members (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                gender TEXT,
                phone_number TEXT,
                email TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists GymMember instances"""
        sql = """
            DROP TABLE IF EXISTS gym_members;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the gym member details into the gym_members table"""
        sql = """
            INSERT INTO gym_members (first_name, last_name, age, gender, phone_number, email)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.age, self.gender, self.phone_number, self.email))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current GymMember instance"""
        sql = """
            UPDATE gym_members
            SET first_name = ?, last_name = ?, age = ?, gender = ?, phone_number = ?, email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.age, self.gender, self.phone_number, self.email, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current GymMember instance"""
        sql = """
            DELETE FROM gym_members
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, first_name, last_name, age, gender, phone_number, email):
        """Initialize a new GymMember instance and save the object to the database"""
        gym_member = cls(first_name, last_name, age, gender, phone_number, email)
        gym_member.save()
        return gym_member

    @classmethod
    def instance_from_db(cls, row):
        """Return a GymMember object having the attribute values from the table row"""
        gym_member = cls.all.get(row[0])
        if gym_member:
            gym_member.first_name = row[1]
            gym_member.last_name = row[2]
            gym_member.age = row[3]
            gym_member.gender = row[4]
            gym_member.phone_number = row[5]
            gym_member.email = row[6]
        else:
            gym_member = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            gym_member.id = row[0]
            cls.all[gym_member.id] = gym_member
        return gym_member

    @classmethod
    def get_all(cls):
        """Return a list containing one GymMember object per table row"""
        sql = """
            SELECT *
            FROM gym_members
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a GymMember object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM gym_members
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
