import sqlite3

CONN = sqlite3.connect('gym.db')
CURSOR = CONN.cursor()

class Payment:

    all = {}

    def __init__(self, member_id, membership_plan_name, payment_method, amount, payment_date, id=None):
        self.id = id
        self.member_id = member_id
        self.membership_plan_name = membership_plan_name
        self.payment_method = payment_method
        self.amount = amount
        self.payment_date = payment_date

    def __repr__(self):
        return (
            f"<Payment {self.id}: Member ID {self.member_id}, Membership Plan {self.membership_plan_name}, " +
            f"Payment Method: {self.payment_method}, Amount: {self.amount}, Payment Date: {self.payment_date}>"
        )

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        if isinstance(member_id, int) and member_id > 0:
            self._member_id = member_id
        else:
            raise ValueError("Member ID must be a positive integer")

    @property
    def membership_plan_name(self):
        return self._membership_plan_name

    @membership_plan_name.setter
    def membership_plan_name(self, membership_plan_name):
        if isinstance(membership_plan_name, str) and membership_plan_name:
            self._membership_plan_name = membership_plan_name
        else:
            raise ValueError("Membership Plan Name must be a non-empty string")

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        if isinstance(payment_method, str) and payment_method:
            self._payment_method = payment_method
        else:
            raise ValueError("Payment Method must be a non-empty string")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int) and amount >= 0:
            self._amount = amount
        else:
            raise ValueError("Amount must be a non-negative integer")

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        self._payment_date = payment_date

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Payment instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY,
                member_id INTEGER,
                membership_plan_name TEXT,
                payment_method TEXT,
                amount INTEGER,
                payment_date DATE,
                FOREIGN KEY (member_id) REFERENCES gym_members(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Payment instances"""
        sql = """
            DROP TABLE IF EXISTS payments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the payment details into the payments table"""
        sql = """
            INSERT INTO payments (member_id, membership_plan_name, payment_method, amount, payment_date)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.member_id, self.membership_plan_name, self.payment_method, self.amount, self.payment_date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Payment instance"""
        sql = """
            UPDATE payments
            SET member_id = ?, membership_plan_name = ?, payment_method = ?, amount = ?, payment_date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.member_id, self.membership_plan_name, self.payment_method, self.amount, self.payment_date, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Payment instance"""
        sql = """
            DELETE FROM payments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, member_id, membership_plan_name, payment_method, amount, payment_date):
        """Initialize a new Payment instance and save the object to the database"""
        payment = cls(member_id, membership_plan_name, payment_method, amount, payment_date)
        payment.save()
        return payment

    @classmethod
    def instance_from_db(cls, row):
        """Return a Payment object having the attribute values from the table row"""
        payment = cls.all.get(row[0])
        if payment:
            payment.member_id = row[1]
            payment.membership_plan_name = row[2]
            payment.payment_method = row[3]
            payment.amount = row[4]
            payment.payment_date = row[5]
        else:
            payment = cls(row[1], row[2], row[3], row[4], row[5])
            payment.id = row[0]
            cls.all[payment.id] = payment
        return payment

    @classmethod
    def get_all(cls):
        """Return a list containing one Payment object per table row"""
        sql = """
            SELECT *
            FROM payments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_member_id(cls, member_id):
        """Return a list of Payment objects corresponding to all table rows matching the specified member_id"""
        sql = """
            SELECT *
            FROM payments
            WHERE member_id = ?
        """
        rows = CURSOR.execute(sql, (member_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_membership_plan_name(cls, membership_plan_name):
        """Return a list of Payment objects corresponding to all table rows matching the specified membership_plan_name"""
        sql = """
            SELECT *
            FROM payments
            WHERE membership_plan_name = ?
        """
        rows = CURSOR.execute(sql, (membership_plan_name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Payment object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM payments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None



