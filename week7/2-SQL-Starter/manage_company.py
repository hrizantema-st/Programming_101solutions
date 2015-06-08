import sqlite3

class ManageCompany:

    def __init__(self, command):
        self.command = command

    def list_employees(self):
        cursor.execute("SELECT id, name, position FROM company;")

        for row in cursor:
            print('{} - {} - {}').format(row[0], row[1], row[2])

    def monthly_spending(self):
        cursor.execute("SELECT monthly_salary FROM company")
        total_spending = 0
        for each in cursor:
            total_spending += each[0]
        print("The company is spending {} every month!".format(total_spending)

    def yearly_spending(self):
        cursor.execute("SELECT monthly_salary, yearly_bonus FROM company")
        total = 0
        for each in cursor:
            total += each[0]*12 + each[1]
        print("The company is spending {} every year!".format(total)

    def add_employee(self):
        pass

    def delete_employee(self, employee_id):
        pass

    def update_employee(self, employee_id):
        pass
"""
