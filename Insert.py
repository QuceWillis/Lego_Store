import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123Password",
    database='Lego'
)
#Connects to our server


mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE SETS (Set_id VARCHAR(50), Name VARCHAR(50), Price INT NOT NULL, Quantity INT NOT NULL, Description VARCHAR(350), CONSTRAINT lego_pk PRIMARY KEY (Set_id))")
mycursor.execute("CREATE TABLE LEGOS (Set_id VARCHAR(50), Name VARCHAR(50), Price FLOAT(2), Brick_Quantity INT NOT NULL, Description VARCHAR(350))")
mycursor.execute("CREATE TABLE BRICKS (Set_id VARCHAR(50), Part_id VARCHAR(50), Name VARCHAR(50), Price FLOAT(2), Quantity INT NOT NULL, Description VARCHAR(350), PRIMARY KEY (Part_id), FOREIGN KEY (Set_id) REFERENCES SETS(Set_id))")
mycursor.execute("CREATE TABLE Employees (id VARCHAR(50), Name VARCHAR(50), Password VARCHAR(50), PRIMARY KEY (id))")
mycursor.execute("CREATE TABLE Users (id VARCHAR(50), Name VARCHAR(50), Password VARCHAR(50), PRIMARY KEY (id))")
mycursor.execute("CREATE TABLE Buggy (id VARCHAR(50), Set_id VARCHAR(50), Name VARCHAR(50), Price FLOAT(2))")
mycursor.execute("CREATE TABLE Checkout (id VARCHAR(50), Set_id VARCHAR(50), Name VARCHAR(50), Price FLOAT(2))")
mycursor.execute("CREATE TABLE StoreCheckout (id VARCHAR(50), Set_id VARCHAR(50), Name VARCHAR(50), Price FLOAT(2))")
mycursor.execute("CREATE TABLE Billing (id VARCHAR(50), Name VARCHAR(50), address VARCHAR(50), phone VARCHAR(50), email VARCHAR(50), Card_num VARCHAR(50))")
mycursor.execute("CREATE TABLE Reports (Report_date DATE, Report_employee VARCHAR(250), Report_parts VARCHAR(250))")

#Creates our tables

sqlFormula = "INSERT INTO Employees (id, Name, Password) VALUES (%s, %s, %s)"
Employees = [("Manager", "Nick Fury", "NF12345678"),
             ("Mechanic", "Iron Man", "IM12345678"),
             ("Scientist", "The Hulk", "TH12345678")]
#The login for employees
#Used for the "Store Mode"

sqlFormula2 = "INSERT INTO Users (id, Name, Password) VALUES (%s, %s, %s)"
Users = [("Spider", "Peter Parker", "Spiderman1"),
         ("Panther", "T'Challa", "Blackpanther1"),
         ("Captain", "Steve Rogers", "CptAmerica1")]
#The login for customers
#Used for the "Online Mode"

sqlFormula3 = "INSERT INTO SETS (Set_id, Name, Price, Quantity, Description) VALUES (%s, %s, %s, %s, %s)"
Sets = [("411", "Red Set", 0, 10, "Contains multiple red blocks"),
        ("222", "Blue Set", 0, 10, "Contains multiple blue blocks"),
        ("333", "Green Set", 0, 10, "Contains multiple green blocks"),
        ("444", "Gold Set", 0, 10, "Contains multiple gold blocks"),
        ("555", "Black Set", 0, 10, "Contains multiple black blocks")]
#Random Sets for the legos
#Will be used as the sets for purchase

sqlFormula4 = "INSERT INTO BRICKS (Set_id, Part_id, Name, Price, Quantity, Description) VALUES (%s, %s, %s, %s, %s, %s)"
Bricks = [("411", "0001", "Red square", .80, 10, "A Red square block" ),
          ("411", "0002", "Red rectangle", .80, 10, "A Red rectangle block" ),
          ("411", "0003", "Red SpiderMan", 1.80, 3, "A Red SpiderMan Lego" ),
          ("411", "0004", "Red IronMan", 1.80, 3, "A Red IronMan Lego" ),
          ("411", "0005", "Red circle", 1.80, 10, "A Red Hulk Lego" ),
          ("222", "0011", "Blue square", .80, 10, "A Blue square block" ),
          ("222", "0012", "Blue rectangle", .80, 10, "A Blue rectangle block" ),
          ("222", "0013", "Blue IronMan", 1.80, 3, "A Blue Ironman Lego" ),
          ("222", "0014", "Blue Aquaman", 1.80, 3, "A Blue Aquaman Lego" ),
          ("222", "0015", "Blue circle", .80, 10, "A Blue circle block" ),
          ("333", "0111", "Green square", .80, 10, "A Green square block" ),
          ("333", "0112", "Green rectangle", .80, 10, "A Green rectangle block" ),
          ("333", "0113", "Green Goblin", 1.80, 3, "A Green Goblin Lego" ),
          ("333", "0114", "Green Arrow", 1.80, 3, "A Green Arrow Lego" ),
          ("333", "0115", "Green Hornet", 1.80, 3, "A Green Hornet Lego" ),
          ("444", "1111", "Gold square", .80, 10, "A Gold square block" ),
          ("444", "1112", "Gold rectangle", .80, 10, "A Gold rectangle block" ),
          ("444", "1113", "Gold IronMan", 1.80, 3, "A Gold IronMan Lego" ),
          ("444", "1114", "Gold Superman", 1.80, 3, "A Gold Superman Lego" ),
          ("444", "1115", "Gold circle", .80, 10, "A Gold circle block" ),
          ("555", "0021", "Black square", .80, 10, "A Black square block" ),
          ("555", "0022", "Black rectangle", .80, 10, "A Black rectangle block" ),
          ("555", "0023", "Black Panther", 1.80, 3, "A Black Panther Lego" ),
          ("555", "0024", "Black SpiderMan", 1.80, 3, "A Black SpiderMan Lego" ),
          ("555", "0025", "Black Venom", 1.80, 3, "A Black Venom Lego" )]
#Random Individual legos to store into the database
#Will be used as the legos to be purchased

mycursor.executemany(sqlFormula, Employees)
mycursor.executemany(sqlFormula2, Users)
mycursor.executemany(sqlFormula3, Sets)
mycursor.executemany(sqlFormula4, Bricks)
mydb.commit()
#Inserts data into Employees and Users Sets and Bricks

mycursor.execute("INSERT INTO LEGOS (Set_id, Name, Price, Brick_Quantity, Description) SELECT SETS.Name, BRICKS.Name, BRICKS.Price, SETS.Quantity, BRICKS.Description FROM BRICKS INNER JOIN SETS ON BRICKS.Set_id = SETS.Set_id")
mycursor.execute("UPDATE LEGOS SET Brick_quantity = 1") #Makes all data in the set 1
mydb.commit()
