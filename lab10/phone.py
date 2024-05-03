import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="alyeavui", password="1234", port=5432)

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
(1, 'Ayaulym', 'Zhuniskhan', 87757770000),
(2, 'Aisulu', 'Alpamys', 87769871300),
(3, 'Zere', 'Almaskyzy', 87711659281),
(4, 'Ayau', 'Ayauka', 87784886806),
(5, 'Ais', 'Ai', 87780441865),
(6, 'Zer', 'Zereshka' , 87475895015),
(7, 'Aylin', 'Ay', 87470122354),
(8, 'Aiym', 'Aiy', 87750054994),
(9, 'Amina', 'Ami', 87057428066),
(10,'Sabina', 'Sabyn', 87017481646);
""")

cur.execute('''UPDATE phonebook 
            SET name = 'China', phonenumber = 87014567891
            WHERE id = 3;
            ''')

cur.execute("""SELECT id, name,surname, phonenumber FROM phonebook WHERE SUBSTR(name,1,1) = 'A' """)
for row in cur.fetchall():
    print(row)

print('\n')

cur.execute("""SELECT id, name,surname, phonenumber FROM phonebook WHERE SUBSTR(phonenumber,1,4) = '8747' """)
for row in cur.fetchall():
    print(row)

print('\n')
cur.execute("""DELETE FROM phonebook WHERE name = 'Ayau' OR SUBSTR(phonenumber,1,4) = '8778' """)
cur.execute('SELECT * FROM phonebook')
for row in cur.fetchall():
    print(row)


conn.commit()
cur.close()
conn.close()
