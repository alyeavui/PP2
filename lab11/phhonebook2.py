import psycopg2

conn = psycopg2.connect(
    dbname='phoonebook',
    user='alyeavui',
    password='1234',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

def get_records_by_pattern(pattern):
    cursor.execute("""
    SELECT * FROM users
    WHERE name LIKE %s
    OR surname LIKE %s
    OR phone LIKE %s
    """, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
    return cursor.fetchall()

def insert_or_update_user(name, phone):
    cursor.execute("""
    DO $$
    BEGIN
        IF EXISTS (SELECT 1 FROM users WHERE name = %s) THEN
            UPDATE users SET phone = %s WHERE name = %s;
        ELSE
            INSERT INTO users (name, phone) VALUES (%s, %s);
        END IF;
    END;
    $$ LANGUAGE plpgsql;
    """, (name, phone, name, name, phone))
    conn.commit()

def insert_many_users(user_data):
    cursor.execute("""
    DO $$
    DECLARE
        user_name TEXT;
        user_phone TEXT;
    BEGIN
        FOREACH user_data_item IN ARRAY %s LOOP
            user_name := split_part(user_data_item, ',', 1);
            user_phone := split_part(user_data_item, ',', 2);
            IF LENGTH(user_phone) != 10 OR NOT user_phone ~ '^\d+$' THEN
                RAISE EXCEPTION 'Invalid phone number format: %', user_phone;
            END IF;
            INSERT INTO users (name, phone) VALUES (user_name, user_phone);
        END LOOP;
    END;
    $$ LANGUAGE plpgsql;
    """, (user_data,))
    conn.commit()

def get_users_with_pagination(limit_val, offset_val):
    cursor.execute("""
    SELECT * FROM users
    ORDER BY id
    LIMIT %s
    OFFSET %s
    """, (limit_val, offset_val))
    return cursor.fetchall()

def delete_user(username=None, phone=None):
    cursor.execute("""
    DELETE FROM users
    WHERE name = %s OR phone = %s
    """, (username, phone))
    conn.commit()

conn.close()
