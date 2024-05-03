import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456", port=5432)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS phonebook')

cur.execute(""" CREATE TABLE IF NOT EXISTS phonebook(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            surname VARCHAR(255),
            phonenumber VARCHAR(11)
);
""")

cur.execute(""" INSERT INTO phonebook (id, name, surname, phonenumber) VALUES
(1, 'Zhaksylyk', 'Phaka', 87757770000),
(2, 'Akbar', 'Maka', 87769871300),
(3, 'Shyngys', 'China', 87077465360),
(4, 'Alex', 'Ale', 87784886806),
(5, 'Ivan', 'Avanushka', 87780441865),
(6, 'Ayan', 'Ayanchik', 87475895015),
(7, 'Miras', 'Aayra', 87470122354),
(8, 'Marat', 'Gara', 87750054994),
(9, 'Max', 'Vaxi', 87057428066),
(10,'Akhat', 'Akho', 87017481646);
""")

id = 11
def add_data():
    cur.execute('''INSERT INTO phonebook (id,name,surname,phonenumber) VALUES
                (11, 'Kairo' , 'Airosh' , 87715648210)
    ''')

def return_data():
    cur.execute("""SELECT id, name, surname, phonenumber FROM phonebook WHERE SUBSTR (name,1,1) = 'A' OR SUBSTR (surname,1,1) = 'A' """)
    for row in cur.fetchall():
        print(row)

def delete_data():
    print('\n')
    cur.execute("""DELETE FROM phonebook WHERE name = 'Ayau' OR SUBSTR(phonenumber,1,4) = '8778' """)
    cur.execute('SELECT * FROM phonebook')
    for row in cur.fetchall():
        print(row)

def add_users():
    global id
    user = input("Enter name: ")
    surname = input("Enter surname: ")
    phonenumber = input("Enter phonenumber: ")

    if(len(phonenumber) == 11) :
        cur.execute('''INSERT INTO phonebook (id, name, surname, phonenumber) VALUES (%s, %s, %s, %s)''', (id,user,surname,phonenumber))
        id+=1
    else:
        print("Wrong phonenumber!")


add_users()

conn.commit()
cur.close()
conn.close()
