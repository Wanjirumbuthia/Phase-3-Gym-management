import sqlite3

CONN = sqlite3.connect('gym.db')
CURSOR = CONN.cursor()

class GymMembershipPlan:

    all = {}

    def __init__(self, name, payment, description, duration, id=None):
        self.id = id
        self.name = name
        self.payment = payment
        self.description = description
        self.duration = duration

    def __repr__(self):
        return (
            f"<GymMembershipPlan {self.id}: {self.name}, Payment: {self.payment}, " +
            f"Description: {self.description}, Duration: {self.duration}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) <= 20:
            self._name = name
        else:
            raise ValueError("Name must be a string with a maximum of 20 characters")

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, payment):
        if isinstance(payment, int) and payment >= 0:
            self._payment = payment
        else:
            raise ValueError("Payment must be a non-negative integer")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise ValueError("Description must be a string")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if isinstance(duration, str) and len(duration) <= 7:
            self._duration = duration
        else:
            raise ValueError("Duration must be a string with a maximum of 7 characters")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of GymMembershipPlan instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS gym_membership_plans (
                id INTEGER PRIMARY KEY,
                name TEXT,
                payment INTEGER,
                description TEXT,
                duration TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists GymMembershipPlan instances"""
        sql = """
            DROP TABLE IF EXISTS gym_membership_plans;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the gym membership plan details into the gym_membership_plans table"""
        sql = """
            INSERT INTO gym_membership_plans (name, payment, description, duration)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.payment, self.description, self.duration))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current GymMembershipPlan instance"""
        sql = """
            UPDATE gym_membership_plans
            SET name = ?, payment = ?, description = ?, duration = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.payment, self.description, self.duration, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current GymMembershipPlan instance"""
        sql = """
            DELETE FROM gym_membership_plans
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, payment, description, duration):
        """Initialize a new GymMembershipPlan instance and save the object to the database"""
        gym_membership_plan = cls(name, payment, description, duration)
        gym_membership_plan.save()
        return gym_membership_plan

    @classmethod
    def instance_from_db(cls, row):
        """Return a GymMembershipPlan object having the attribute values from the table row"""
        gym_membership_plan = cls.all.get(row[0])
        if gym_membership_plan:
            gym_membership_plan.name = row[1]
            gym_membership_plan.payment = row[2]
            gym_membership_plan.description = row[3]
            gym_membership_plan.duration = row[4]
        else:
            gym_membership_plan = cls(row[1], row[2], row[3], row[4])
            gym_membership_plan.id = row[0]
            cls.all[gym_membership_plan.id] = gym_membership_plan
        return gym_membership_plan

    @classmethod
    def get_all(cls):
        """Return a list containing one GymMembershipPlan object per table row"""
        sql = """
            SELECT *
            FROM gym_membership_plans
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        """Return a list of GymMembershipPlan objects corresponding to all table rows matching the specified name"""
        sql = """
            SELECT *
            FROM gym_membership_plans
            WHERE name = ?
        """
        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a GymMembershipPlan object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM gym_membership_plans
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
