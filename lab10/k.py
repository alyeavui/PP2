import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="alyeavui", password="1234", port=5432)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS person')

cur.execute(""" CREATE TABLE IF NOT EXISTS person(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
);
""")


cur.execute(""" INSERT INTO person (id, name, age, gender) VALUES
(1, 'Ayau', 18, 'f'),
(2, 'Ayim',   25, 'f'),
(3, 'Zheka', 58, 'm'),
(4, 'Zere',  34, 'f'),
(5, 'Misha', 10, 'm'),
(6, 'Alan',  34, 'm');
            
""")

cur.execute("""SELECT * FROM person WHERE name = 'Alan'; """)
print(cur.fetchone())

cur.execute("""SELECT * FROM person WHERE age < 50;""")
for row in cur.fetchall():
    print(row)

sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ("A", 30)) 
print(sql)

conn.commit()

cur.close()
conn.close()
