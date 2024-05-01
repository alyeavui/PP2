import psycopg2
import csv

conn = psycopg2.connect(
    dbname='phoneboook',
    user='alyeavui',
    password='1234',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook
              (id SERIAL PRIMARY KEY, username TEXT, phone TEXT)''')
conn.commit()

def insert_data_from_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            cursor.execute('INSERT INTO phonebook (username, phone) VALUES (%s, %s)', row)
    conn.commit()

def insert_data_from_console():
    username = input('Enter username: ')
    phone = input('Enter phone number: ')
    cursor.execute('INSERT INTO phonebook (username, phone) VALUES (%s, %s)', (username, phone))
    conn.commit()

def update_data(username, new_username=None, new_phone=None):
    if new_username:
        cursor.execute('UPDATE phonebook SET username = %s WHERE username = %s', (new_username, username))
    if new_phone:
        cursor.execute('UPDATE phonebook SET phone = %s WHERE username = %s', (new_phone, username))
    conn.commit()

def query_data(filter_by=None, value=None):
    if filter_by and value:
        cursor.execute(f'SELECT * FROM phonebook WHERE {filter_by} = %s', (value,))
    else:
        cursor.execute('SELECT * FROM phonebook')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_data(filter_by, value):
    cursor.execute(f'DELETE FROM phonebook WHERE {filter_by} = %s', (value,))
    conn.commit()

insert_data_from_csv('phonebook_data.csv')
insert_data_from_console()
update_data('Alice', new_phone='1234567890')
query_data()
delete_data('username', 'Alice')

conn.close()
