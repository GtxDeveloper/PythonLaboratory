import sqlite3

#  1 Створення бази
print("Creating and connecting to 'mydatabase.db' ...")
conn = sqlite3.connect('mydatabase.db')
conn.close()
print("The SQLite connection is closed.")

# 2 Підключення до бази в пам'яті
try:
    sqlite_Connection = sqlite3.connect('temp.db')
    conn = sqlite3.connect(':memory:')
    print("\nMemory database created and connected to SQLite.")
    sqlite_select_Query = "select sqlite_version();"
    cursor = conn.cursor()
    cursor.execute(sqlite_select_Query)
    version = cursor.fetchone()
    print("SQLite Database Version is:", version[0])
    conn.close()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqlite_Connection:
        sqlite_Connection.close()
        print("The SQLite connection is closed.")

# === 3. Створення таблиці agent_master у mydatabase.db ===
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agent_master (
        agent_code CHAR(6),
        agent_name CHAR(40),
        working_area CHAR(35),
        commission DECIMAL(10,2),
        phone_no CHAR(15) NULL
    )
''')
conn.commit()
print("\nTable 'agent_master' created.")
conn.close()

# 4 Створення таблиці salesman і додавання записів
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS salesman (
        salesman_id INTEGER,
        name CHAR(30),
        city CHAR(35),
        commission DECIMAL(7,2)
    )
''')
rows = [
    (5001, 'James Hoog', 'New York', 0.15),
    (5002, 'Nail Knite', 'Paris', 0.25),
    (5003, 'Pit Alex', 'London', 0.15),
    (5004, 'Mc Lyon', 'Paris', 0.35),
    (5005, 'Paul Adam', 'Rome', 0.45)
]
cursor.executemany("INSERT INTO salesman VALUES (?, ?, ?, ?)", rows)
conn.commit()
print("\nTable 'salesman' created and records inserted.")
conn.close()

#  5 Додавання даних у salesman через введення користувачем
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
print("\nEnter salesman data to insert:")
s_id = int(input('Salesman ID: '))
name = input('Name: ')
city = input('City: ')
commission = float(input('Commission: '))
cursor.execute("INSERT INTO salesman VALUES (?, ?, ?, ?)", (s_id, name, city, commission))
conn.commit()
print("Record inserted.")
conn.close()

#  6 Створення таблиці Doctor і додавання записів
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Doctor (
        Doctor_Id INTEGER PRIMARY KEY,
        Doctor_Name TEXT,
        Hospital_Id INTEGER,
        Joining_Date DATE,
        Speciality TEXT,
        Salary INTEGER,
        Experience INTEGER
    )
''')

doctor_data = [
    (101, 'David', 1, '2005-02-10', 'Pediatric', 40000, None),
    (102, 'Michael', 1, '2018-07-23', 'Oncologist', 20000, None),
    (103, 'Susan', 2, '2016-05-19', 'Garnacologist', 25000, None),
    (104, 'Robert', 2, '2017-12-28', 'Pediatric', 28000, None),
    (105, 'Linda', 3, '2004-06-04', 'Garnacologist', 42000, None),
    (106, 'William', 3, '2012-09-11', 'Dermatologist', 30000, None),
    (107, 'Richard', 4, '2014-08-21', 'Garnacologist', 32000, None),
    (108, 'Karen', 4, '2011-10-17', 'Radiologist', 30000, None)
]

cursor.executemany('''
    INSERT INTO Doctor (
        Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date,
        Speciality, Salary, Experience
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
''', doctor_data)

conn.commit()
print("\nTable 'Doctor' created and records inserted.")
conn.close()
