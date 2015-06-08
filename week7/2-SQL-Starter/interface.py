import sqlite3
from settings import DB_NAME


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

while True:
    command = input("Enter a command:")
    command_list = command.split(" ")

    if command == "list_employees":
        info = cursor.execute("""SELECT id, name, position FROM company""")

        info_to_print = info.fetchall()
        for each in info_to_print:
            print(each)

    elif command == "monthly_spending":
        info = cursor.execute("""SELECT monthly_salary FROM company""")
        info_to_use = info.fetchall()

        total_spending = 0
        for each in info_to_use:
            total_spending += each[0]
        print("The company is spending {} every month!".format(total_spending))

    elif command == "yearly_spending":
        info = cursor.execute("""SELECT monthly_salary, yearly_bonus
            FROM company""")
        info_to_use = info.fetchall()
        total = 0
        for each in info_to_use:
            total += each[0]*12 + each[1]
        print("The company is spending {} every year!".format(total))

    elif command == "add_employee":
        new_name = input("User name: ")
        new_monthly_salary = input("User's salary: ")
        new_yearly_bonus = input("User's bonus: ")
        new_position = input("User's position: ")
        cursor.execute("""INSERT INTO company(name, monthly_salary, yearly_bonus, position)
         VALUES(?,?,?,?)""", (new_name, new_monthly_salary, new_yearly_bonus, new_position))

    elif len(command_list) == 2:
        if command_list[0] == "delete_employee":
            cursor.execute("DELETE FROM company WHERE id = ?", command_list[1])

        elif command_list[0] == "update_employee":
            new_name = input("User name: ")
            new_monthly_salary = input("User's salary: ")
            new_yearly_bonus = input("User's bonus: ")
            new_position = input("User's position: ")
            cursor.execute("""UPDATE company SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
                 WHERE id = ? """, (new_name, new_monthly_salary, new_yearly_bonus, new_position, command_list[1]))

    else:
        print("Invalid input!")
