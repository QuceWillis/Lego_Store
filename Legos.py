import mysql.connector

def mode():
    print("+------MODE SELECT------+")
    print("|   1. Online Mode      |")
    print("|   2. Store Mode       |")
    print("|   X. Exit             |")
    print("+-----------------------+")

def menu():
    print("+-------MAIN MENU-------+")
    print("|   1. Browse           |")
    print("|   2. Search           |")
    print("|   3. Place an Order   |")
    print("|   4. Buggy            |")
    print("|   5. Checkout         |")
    print("|   X. Exit             |")
    print("+-----------------------+")

def employee_menu():
    print("+-----EMPLOYEE MENU-----+")
    print("|   1. Employee Portal  |")
    print("|   2. Sale/Sell        |")
    print("|   3. Order Management |")
    print("|   4. Reports          |")
    print("|   X. Exit             |")
    print("+-----------------------+")

def search_bar():
    print("+------SEARCH MENU------+")
    print("|---Enter x to return---|")

def buggy():
    print("+------ORDER SELECT-----+")
    print("|   1. SETS             |")
    print("|   2. Individual legos |")
    print("|   X. Exit             |")
    print("+-----------------------+")

def report():
    print("+---------REPORTS--------+")
    print("|   1. Employee Report   |")
    print("|   2. Parts Report      |")
    print("|   X. Exit              |")
    print("+------------------------+")

def deleteorder():
    print("+------CANCEL ORDER-----+")
    print("|   1. SETS             |")
    print("|   2. Individual legos |")
    print("|   X. Exit             |")
    print("+-----------------------+")

def order():
    print("+------ORDER SELECT-----+")
    print("|   1. Order SETS       |")
    print("|   2. Order legos      |")
    print("|   3. Stop Orders      |")
    print("|   X. Exit             |")
    print("+-----------------------+")

def cart():
    print("+------Your Cart------+")

def shop():
    print("+----Start Shopping----+")
    print("|    1.Pick Items      |")
    print("|    2.Checkout        |")
    print("|    3.Return Items    |")
    print("+----------------------+")

def cash():
    print("+-------Register-------+")
    print("|    1. Cash           |")
    print("|    2. Credit         |")
    print("+----------------------+")

def returns():
    print("+--------Returns--------+")
    print("|    1. Brick           |")
    print("|    2. None            |")
    print("+-----------------------+")

def payment():
    print("+-------Pay Menu-------+")
    print("|    1. Create new     |")
    print("|    2. Use Existing   |")
    print("+----------------------+")

def employee():
    print("+-----Manager Menu-----+")
    print("|    1. Hire           |")
    print("|    2. Fire           |")
    print("|    3. Alter          |")
    print("+----------------------+")



def login():
    print("+------Enter Login------+")


#Menu Screens

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123Quentin",
    database='Today'
)
#To connect to db

mycursor = mydb.cursor() #Cursor used to run sql code through python

mode()
mode_choice = input("> ")
if mode_choice == "1":
    login()
    test = input("Enter an id: ")
    test2 = input("Enter a password: ")
    print("+-----------------------+")
    mycursor.execute("DELETE FROM Buggy")
    mydb.commit()
    query = "SELECT * FROM Users WHERE id =%s AND Password =%s"
    mycursor.execute(query, (test, test2))
    login = mycursor.fetchone()
    #Logs in user if data is correct
    #Deletes search history once you exit app

    if login is None:
        print("Incorrect Login")
    else:
        cont = True
        while cont is True:
            menu()
            menu_choice = input("> ")
            if menu_choice == "1": #To view all tables
               mycursor.execute("SELECT Set_id, Name FROM SETS") #Shows the data from sets table
               result = mycursor.fetchall()
               for row in result:
                    print(row) #Prints the data
               mycursor.execute("SELECT Part_id, Name FROM BRICKS") #Shows the data from bricks table
               result = mycursor.fetchall()
               for row in result:
                    print(row) #Prints the data
               view = True
               while view is True: #loop continues to ask user to view more/Select
                    print("Enter item id or item name to view more or (x) to return")
                    select = input("> ")
                    if select == "x":
                        view = False
                        break
                    query2 = "SELECT * FROM SETS WHERE Set_id =%s OR Name =%s" #Selects data from chosen params
                    mycursor.execute(query2, (select, select))
                    select_sets = mycursor.fetchone()
                    query3 = "SELECT * FROM BRICKS WHERE Part_id =%s OR Name =%s" #Selects data from chosen params
                    mycursor.execute(query3, (select, select))
                    select_bricks = mycursor.fetchone()
                    if select_sets != None:
                        print(select_sets) #Prints the selected set
                    elif select_bricks != None:
                        print(select_bricks) #Prints the selected brick
                    else:
                        print("Item does not exist") #Error
            elif menu_choice == "2": #To search for legos
                cont_search = True
                while cont_search is True: #Continues to search
                    search_bar()
                    select = input("> ")
                    if select == "x":
                        view = False
                        break
                    query2 = "SELECT * FROM SETS WHERE Set_id =%s OR Name =%s" #Selects from entered params
                    mycursor.execute(query2, (select, select))
                    select_sets = mycursor.fetchone()
                    query3 = "SELECT * FROM BRICKS WHERE Part_id =%s OR Name =%s" #Selects from entered params
                    mycursor.execute(query3, (select, select))
                    select_bricks = mycursor.fetchone()
                    if select_sets != None:
                        print(select_sets) #Prints out Sets
                    elif select_bricks != None:
                        print(select_bricks) #Prints out Bricks
                    else:
                        print("Item does not exist") #Error
            elif menu_choice == "3": #Add item to cart
                place_order = True
                while place_order is True:
                    buggy()
                    buggy_choice = input("> ")
                    if buggy_choice == "1": #Shows the data from SETS
                        mycursor.execute("SELECT Name, Description FROM SETS")
                        result = mycursor.fetchall()
                        for row in result:
                            print(row)
                        set_view = True
                        while set_view is True:
                            print("Enter name of set to order or (x) to return")
                            order = input("> ") #User input for selected SET
                            if order == "x":
                                set_view = False
                                break
                            query4 = "SELECT * FROM LEGOS WHERE Set_id =%s" #Selects SET where user chose
                            mycursor.execute(query4, (order,))
                            order_sets = mycursor.fetchall()
                            if order_sets != None:
                                query_order = "INSERT INTO Buggy (id, Set_id, Name, Price) SELECT Description, Set_id, Name, Price FROM LEGOS WHERE Set_id =%s"
                                #Inserts what the user chose inside a buggy
                                print(order)
                                mycursor.execute(query_order, (order,))
                                query_user = "UPDATE Buggy SET id =%s"
                                #Corrects Buggy id to the user purchasing
                                mycursor.execute(query_user, (test,))
                                mydb.commit()
                                query_checkout = "INSERT INTO Checkout (id, Set_id, Name, Price) SELECT Buggy.id, LEGOS.Set_id, LEGOS.Name, LEGOS.Price FROM LEGOS RIGHT JOIN Buggy ON LEGOS.Set_id = Buggy.Set_id WHERE LEGOS.Set_id =%s GROUP BY Buggy.id, LEGOS.Set_id, LEGOS.Name, LEGOS.Price"
                                #Stores the data somewhere it wont get lost/ History
                                mycursor.execute(query_checkout, (order,))
                                mydb.commit()
                                query_data = "UPDATE SETS SET Quantity = Quantity - 1 WHERE Name =%s" #Erases from database
                                mycursor.execute(query_data, (order,))
                                mydb.commit()
                                mycursor.execute("SELECT * FROM Buggy") #Selects from cart
                                buggy_order = mycursor.fetchall()
                                for row in buggy_order:
                                    print(row) #Prints out what you added to cart
                            else:
                                print("Item does not exist") #error
                    elif buggy_choice == "2": #Shows the data from Bricks
                        mycursor.execute("SELECT Name, Description FROM BRICKS") #Shows name from BRICKS
                        result = mycursor.fetchall()
                        for row in result:
                            print(row) #Print out the Legos
                        set_view = True
                        while set_view is True: #Asks user continuously
                            print("Enter name of lego to order or (x) to return")
                            order = input("> ")
                            if order == "x":
                                set_view = False
                                break
                            query5 = "SELECT * FROM LEGOS WHERE Name =%s" #Select legos where user selects
                            mycursor.execute(query5, (order,))
                            order_brick = mycursor.fetchone()
                            if order_brick != None:
                                query_order = "INSERT INTO Buggy (id, Set_id, Name, Price) SELECT Description, Set_id, Name, Price FROM LEGOS WHERE Name =%s"
                                #inserts the lego into the cart
                                print(order)
                                mycursor.execute(query_order, (order,))
                                query_user = "UPDATE Buggy SET id =%s"
                                #Corrects user id
                                mycursor.execute(query_user, (test,))
                                mydb.commit()
                                query_checkout = "INSERT INTO Checkout (id, Set_id, Name, Price) SELECT Buggy.id, LEGOS.Set_id, LEGOS.Name, LEGOS.Price FROM LEGOS RIGHT JOIN Buggy ON LEGOS.Set_id = Buggy.Set_id WHERE LEGOS.Name =%s GROUP BY Buggy.id, LEGOS.Set_id, LEGOS.Name, LEGOS.Price"
                                #Stores data where it cannot be lost
                                mycursor.execute(query_checkout, (order,))
                                mydb.commit()
                                query_data1 = "UPDATE BRICKS SET Quantity = Quantity - 1 WHERE Name =%s" #Erases 1 from database
                                mycursor.execute(query_data1, (order,))
                                mydb.commit()
                                mycursor.execute("SELECT * FROM Buggy") #Selects what user has chosen
                                buggy_order = mycursor.fetchall()
                                for row in buggy_order:
                                    print(row) #prints all of the user items
                            else:
                                print("Item does not exist")
                    elif buggy_choice == "x": #Exits menu
                        place_order = False
                        break
                    else: #Error
                        print("Not an option")
            elif menu_choice == "4": #Shows what's in the cart
                cart()
                query_buggy = "SELECT * FROM Checkout WHERE id =%s"
                #Used Checkout to select because data from their is saved for each user and not lost
                mycursor.execute(query_buggy, (test,))
                buggy_order = mycursor.fetchall()
                for row in buggy_order:
                    print(row) #Shows everything user has selected
                print("+--------Cart--------+")
            elif menu_choice == "5": #Close tab
                query_buggy = "SELECT * FROM Checkout WHERE id =%s"
                mycursor.execute(query_buggy, (test,))
                buggy_order = mycursor.fetchall()
                for row in buggy_order:
                    print(row) #Prints everything in the cart
                print("----your total----")
                query_price = "SELECT ROUND(SUM(Price), 2) FROM Checkout WHERE id =%s" #Selecets total price
                mycursor.execute(query_price, (test,))
                select_price = mycursor.fetchone()
                print(select_price) #prints out the total price
                print("")
                payment()
                pay = input("> ")
                if pay == "1":
                    address = input("Enter Address > ")
                    phone = input("Enter phone > ")
                    email = input("Enter email > ")
                    card = input("Enter Card# > ")
                    name = ""
                    #enter new data used to pay for item
                    mycursor.execute(name, (test,))
                    select_name = mycursor.fetchone()
                    print(select_name)
                    query_pay = "INSERT INTO Billing (id, Name, address, phone, email, Card_num) VALUES (%s, %s, %s, %s, %s, %s)"
                    mycursor.execute(query_pay, (test, name, address, phone, email, card))
                    #Insert the data entered into the billing table for reuse
                    mydb.commit()
                    query_card = "SELECT * FROM Billing WHERE Card_num =%s"
                    mycursor.execute(query_card, (card,))
                    billing_order = mycursor.fetchone()
                    print(billing_order)
                    print("Payment was processed using above data")
                    close_bill = "DELETE FROM Checkout WHERE id =%s"
                    mycursor.execute(close_bill, (test,))
                    mydb.commit()
                    #Deletes item from database
                elif pay == "2":
                    mycursor.execute("SELECT * FROM Billing")
                    result = mycursor.fetchall()
                    for row in result:
                        print(row)
                    credit = input("Enter card# to use > ")
                    query5 = "SELECT * FROM Billing WHERE Card_num =%s"  # Select billing where user selects
                    mycursor.execute(query5, (credit,))
                    credit_card = mycursor.fetchone()
                    if credit_card != None:
                        query_card = "SELECT * FROM Billing WHERE Card_num =%s"
                        mycursor.execute(query_card, (credit,))
                        billing_order = mycursor.fetchone()
                        print(billing_order)
                        print("Payment was processed using above data")
                        close_bill = "DELETE FROM Checkout WHERE id =%s"
                        mycursor.execute(close_bill, (test,))
                        mydb.commit()
                    else:
                        print("Credit Card was not found!")
                        break
                        #Takes the stored credit info and uses to pay
                        #Deletes if data was found
            elif menu_choice == "x" or "X":
                break



if mode_choice == "2":
    login()
    test = input("Enter an id: ")
    test2 = input("Enter a password: ")
    print("+-----------------------+")
    query = "SELECT * FROM Employees WHERE id =%s AND Password =%s"
    mycursor.execute(query, (test, test2))
    login = mycursor.fetchone()
    # Logs in user if data is correct

    if login is None:
        print("Incorrect Login")
    else:
        cont = True
        while cont is True:
            employee_menu()
            menu_choice = input("> ")
            if menu_choice == "1":
                if test == "Manager" or "manager":
                    emp = True
                    while emp is True:
                        employee()
                        emp_choice = input("> ")
                        if emp_choice == "1":
                            position = input("Position of new hire > ")
                            new_name = input("Name of new hire > ")
                            password = input("Password of new hire > ")
                            query_emp = "INSERT INTO Employees (id, Name, Password) VALUES (%s, %s, %s)"
                            mycursor.execute(query_emp, (position, new_name, password))
                            mydb.commit()
                        elif emp_choice == "2":
                            fire = input("Enter name of Employee to fire > ")
                            query_fire = "DELETE FROM Employees WHERE Name =%s"
                            mycursor.execute(query_fire, (fire,))
                            mydb.commit()
                        elif emp_choice == "3":
                            change = input("Enter name of Employee you'd like to change > ")
                            change_pos = input("Enter new or same Position > ")
                            change_name = input("Enter new or same Name > ")
                            change_pass = input("Enter new or same password > ")
                            query_change = "UPDATE Employees SET id =%s, Name =%s, Password =%s WHERE Name =%s"
                            mycursor.execute(query_change, (change_pos, change_name, change_pass, change))
                        else:
                            emp = False
                            break
                else:
                    print ("You must be a manager to enter this screen!")
            elif menu_choice == "2":
                shopping = True
                while shopping is True:
                    shop()
                    store = input("> ")
                    if store == "1":
                        place_order = True
                        while place_order is True:
                            buggy()
                            buggy_choice = input("> ")
                            if buggy_choice == "1":  # Shows the data from SETS
                                mycursor.execute("SELECT Name, Description FROM SETS")
                                result = mycursor.fetchall()
                                for row in result:
                                    print(row)
                                set_view = True
                                while set_view is True:
                                    print("Enter name of set to order or (x) to return")
                                    order = input("> ")  # User input for selected SET
                                    if order == "x":
                                        set_view = False
                                        break
                                    query4 = "SELECT * FROM LEGOS WHERE Set_id =%s"  # Selects SET where user chose
                                    mycursor.execute(query4, (order,))
                                    order_sets = mycursor.fetchall()
                                    if order_sets != None:
                                        query_order = "INSERT INTO Buggy (id, Set_id, Name, Price) SELECT Description, Set_id, Name, Price FROM LEGOS WHERE Set_id =%s"
                                        # Inserts what the user chose inside a buggy
                                        print(order)
                                        mycursor.execute(query_order, (order,))
                                        query_user = "UPDATE Buggy SET id =%s"
                                        # Corrects Buggy id to the user purchasing
                                        mycursor.execute(query_user, (test,))
                                        mydb.commit()
                                        query_checkout = "INSERT INTO StoreCheckout (id, Set_id, Name, Price) SELECT Buggy.id, LEGOS.Set_id, LEGOS.Name, LEGOS.Price FROM LEGOS RIGHT JOIN Buggy ON LEGOS.Set_id = Buggy.Set_id WHERE LEGOS.Set_id =%s GROUP BY Buggy.id, LEGOS.Set_id, LEGOS.Name, LEGOS.Price"
                                        # Stores the data somewhere it wont get lost/ History
                                        mycursor.execute(query_checkout, (order,))
                                        mydb.commit()
                                        mycursor.execute("SELECT * FROM Buggy")  # Selects from cart
                                        buggy_order = mycursor.fetchall()
                                        for row in buggy_order:
                                            print(row)  # Prints out what you added to cart
                                    else:
                                        print("Item does not exist")  # error
                            elif buggy_choice == "2":  # Shows the data from Bricks
                                mycursor.execute("SELECT Name, Description FROM BRICKS")  # Shows name from BRICKS
                                result = mycursor.fetchall()
                                for row in result:
                                    print(row)  # Print out the Legos
                                set_view = True
                                while set_view is True:  # Asks user continuously
                                    print("Enter name of lego to order or (x) to return")
                                    order = input("> ")
                                    if order == "x":
                                        set_view = False
                                        break
                                    query5 = "SELECT * FROM LEGOS WHERE Name =%s"  # Select legos where user selects
                                    mycursor.execute(query5, (order,))
                                    order_brick = mycursor.fetchone()
                                    if order_brick != None:
                                        query_order = "INSERT INTO Buggy (id, Set_id, Name, Price) SELECT Description, Set_id, Name, Price FROM LEGOS WHERE Name =%s"
                                        # inserts the lego into the cart
                                        print(order)
                                        mycursor.execute(query_order, (order,))
                                        query_user = "UPDATE Buggy SET id =%s"
                                        # Corrects user id
                                        mycursor.execute(query_user, (test,))
                                        mydb.commit()
                                        query_checkout = "INSERT INTO StoreCheckout (id, Set_id, Name, Price) SELECT Buggy.id, LEGOS.Set_id, LEGOS.Name, LEGOS.Price FROM LEGOS RIGHT JOIN Buggy ON LEGOS.Set_id = Buggy.Set_id WHERE LEGOS.Name =%s GROUP BY Buggy.id, LEGOS.Set_id, LEGOS.Name, LEGOS.Price"
                                        # Stores data where it cannot be lost
                                        mycursor.execute(query_checkout, (order,))
                                        mydb.commit()
                                        mycursor.execute("SELECT * FROM Buggy")  # Selects what user has chosen
                                        buggy_order = mycursor.fetchall()
                                        for row in buggy_order:
                                            print(row)  # prints all of the user items
                                    else:
                                        print("Item does not exist")
                            elif buggy_choice == "x":  # Exits menu
                                place_order = False
                                break
                            else:
                                place_order = False
                                break
                    elif store == "2":
                        cash()
                        payway = input("> ")
                        if payway == "1":
                            print("youve made the payment")
                        elif payway == "2":
                            cardnum = input("Enter your card info > ")
                            print("youve made a payment")
                        else:
                            break
                    elif store == "3":
                        cart()
                        query_buggy = "SELECT * FROM StoreCheckout WHERE id =%s"
                        # Used Checkout to select because data from their is saved for each user and not lost
                        mycursor.execute(query_buggy, (test,))
                        buggy_order = mycursor.fetchall()
                        for row in buggy_order:
                            print(row)  # Shows everything user has selected
                        print("+--------Cart--------+")
                        print("")
                        returns()
                        item_return = input("> ")
                        if item_return == "1":
                            returning = input("Name of object returning > ")
                            query_return = "DELETE FROM StoreCheckout WHERE Name =%s AND id =%s"
                            mycursor.execute(query_return, (returning, test))
                            mydb.commit()
                        elif item_return == "2":
                            print("Shop again")
                            break
                    else:
                        place_order = False
                        break
            elif menu_choice == "3": #Managing the orders
                ordering = True
                while ordering is True:
                    order()
                    orders = input("> ")
                    if orders == "1": #Manages the orders by inserting new sets and a new lego for the set
                        set_id = input("New Set id > ")
                        new_name = input("Name of new Set > ")
                        new_lego = input("Lego belonging to Set > ")
                        lego_id = input("New Lego id > ")
                        lego_quantity = input("New Lego quantity > ")
                        lego_price = input("Price of new lego > ")
                        set_price = 0
                        set_quantity = 10
                        set_description = input("description of new Set > ")
                        lego_description = input("Description of new Lego > ")
                        query_set = "INSERT INTO SETS (Set_id, Name, Price, Quantity, Description) VALUES (%s, %s, %s, %s, %s)"
                        query_lego = "INSERT INTO BRICKS (Set_id, Part_id, Name, Price, Quantity, Description) VALUES (%s, %s, %s, %s, %s, %s)"
                        mycursor.execute(query_set, (set_id, new_name, int(set_price), int(set_quantity), set_description))
                        mycursor.execute(query_lego, (set_id, lego_id, new_lego, float(lego_price), int(lego_quantity), set_description))
                        mydb.commit()
                    elif orders == "2": #Manages the orders by inserting new legos
                        sets = input("Set it belongs to > ")
                        new_lego = input("Lego belonging to Set > ")
                        lego_id = input("New Lego id > ")
                        lego_quantity = input("New Lego quantity > ")
                        lego_price = input("Price of new lego > ")
                        lego_description = input("Description of new Lego > ")
                        query_lego = "INSERT INTO BRICKS (Set_id, Part_id, Name, Price, Quantity, Description) VALUES (%s, %s, %s, %s, %s, %s)"
                        mycursor.execute(query_lego, (set_id, lego_id, new_lego, float(lego_price), int(lego_quantity), set_description))
                        mydb.commit()
                    elif orders == "3":  #Manages the orders by deleting
                        deleteorder()
                        delete = input("> ")
                        if delete == "1":
                            delete_set = input("Enter set id to cancel > ")
                            query_delete = "DELETE FROM SETS WHERE Set_id =%s"
                            query_deletelego = "DELETE FROM BRICKS WHERE Set_id =%s"
                            mycursor.execute(query_deletelego, (delete_set,))
                            mycursor.execute(query_delete, (delete_set,))
                            mydb.commit()
                        elif delete == "2":
                            delete_lego = input("Enter Lego id to cancel > ")
                            query_deletelego = "DELETE FROM BRICKS WHERE Part_id =%s"
                            mycursor.execute(query_deletelego, (delete_lego,))
                            mydb.commit()
                        else:
                            break
                    else:
                        break
            elif menu_choice == "4": #Menu choice to get the user daily reports
                report()
                emp_reports = input("Enter daily employee report > ")
                pts_reports = input("Enter daily parts report > ")
                get_date = "2010/12/20 10:25:00"
                query_report = "INSERT INTO Reports (Report_date, Report_employee, Report_parts) VALUES (%s, %s, %s)"
                mycursor.execute(query_report, (get_date, emp_reports, pts_reports))
                mycursor.execute("UPDATE Reports SET Report_date = CURRENT_DATE()")
                mydb.commit()
            elif menu_choice == "X" or "x":
                cont = False
                break
