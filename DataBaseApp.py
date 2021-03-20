import sys
import sqlite3 as db
import random
import timeit

def create_table_users():
    conn = db.connect('database.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users(
    
    user_last_name TEXT,
    user_first_name TEXT,
    user_middle_name TEXT,
    user_birthdate TEXT,
    user_gender TEXT

    );""")

    conn.close()

def add_record(lname, fname, mname, birthdate, gender):
    conn = db.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(?,?,?,?,?)", [lname, fname, mname, birthdate, gender])
    conn.commit()
    conn.close()

def print_unique_users():
    conn = db.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT user_last_name || ' ' || user_first_name || ' ' || user_middle_name || ' ' || user_birthdate || ' ' || user_gender FROM users ORDER BY user_last_name")
    conn.commit()
    print(c.fetchall())
    conn.close()

def get_random_letter():
    letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    random_letter = letter_list[random.randint(0, (len(letter_list)))-1]
    return random_letter

def choose_gender():
    gender_list = ['Male', 'Female']
    random_gender = gender_list[random.randint(0, (len(gender_list)))-1]
    return random_gender

def auto_fill():
    conn = db.connect('database.db')
    c = conn.cursor()
    for row in range(1000000):
        c.execute("INSERT INTO users VALUES(?,?,?,?,?)", [get_random_letter(), get_random_letter(), get_random_letter(), get_random_letter(), choose_gender()])
        conn.commit()

    for row in range(100):
        c.execute("INSERT INTO users VALUES(?,?,?,?,?)", ['f', get_random_letter(), get_random_letter(), get_random_letter(), 'Male'])
        conn.commit()
    
    conn.close()

def select_male_f():
    conn = db.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT user_last_name || ' ' || user_first_name || ' ' || user_middle_name || ' ' || user_birthdate || ' ' || user_gender FROM users WHERE user_gender = 'Male' AND user_last_name = 'f'")
    conn.close()

def main():

    if sys.argv[1] == '1':
        create_table_users()

    elif sys.argv[1] == '2':
        add_record(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

    elif sys.argv[1] == '3':
        print_unique_users()

    elif sys.argv[1] == '4':
        auto_fill()

    elif sys.argv[1] == '5':
        select_male_f()
        execution_time = timeit.timeit(select_male_f, number=1)
        print('Время выполнения: ', execution_time, ' секунд')


if __name__ == '__main__':
    main()