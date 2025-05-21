# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'cousin_music.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

TABLES = (" cousin_music "
            "LEFT JOIN instrument ON cousin_music.instrument_id = instrument.instrument_id "
            "LEFT JOIN gender ON cousin_music.gender_id = gender.gender_id "
            "LEFT JOIN school ON cousin_music.school_id = school.school_id "
            "LEFT JOIN day ON cousin_music.day_id = day.day_id ")


def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  

new_students = []

menu_choice =''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Music lessons database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: All data\n'
                        'B: Lessons on Monday\n'
                        'C: Lessons on Wednesday\n'
                        'D: People that owe money and amount owed\n'
                        'G: Get info of a specific person\n'
                        'J: Add data for a new person.\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('all_data')
    elif menu_choice == 'B':
        print_query('lesson_monday')
    elif menu_choice == 'C':
        print_query('lesson_wednesday')
    elif menu_choice == 'D':
        print_query('not_paid')
    elif menu_choice == 'G':
        name = input("Which child's info do you want to see: ")
        print_parameter_query("first_name, gender, school, instrument, day, lesson_time",  "first_name = ?",name)
    elif menu_choice == 'J':
        db = sqlite3.connect(DB_NAME)
        cursor = db.cursor()
        first_name = input("Student's first name: ")
        new_students.append(first_name)
        last_name = input("Student's last name: ")
        new_students.append(last_name)
        gender_id = int(input("Student's gender id number: "))
        new_students.append(gender_id)
        dob = input("Student's date of birth - type in DOB in form YYYY-MM-DD: ")
        new_students.append(dob)
        instrument_id = int(input("Student's instrument id number: "))
        new_students.append(instrument_id)
        school_id = int(input("Student's school - enter abbreviation eg - LMS : "))
        new_students.append(school_id)
        day_id = int(input("Day of lesson - give full word eg - Monday: "))
        new_students.append(day_id)
        lesson_time = input("Lesson time, give in 24 hour time: ")
        new_students.append(lesson_time)
        parent_name = input("Parent first name: ")
        new_students.append(parent_name)
        parent_last = input("Parent last name: ")
        new_students.append(parent_last)
        parent_phone = int(input("Parent phone number, no spaces: "))
        new_students.append(parent_phone)
        paid = int(input('Amount already paid: '))
        new_students.append(paid)
        a =  '''INSERT INTO cousin_music(first_name, last_name, gender_id, dob, instrument_id,
                     school_id, day_id, lesson_time, parent_name, parent_last, parent_phone, paid) 
                     VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
        
        cursor.execute(a, new_students)
        db.commit()  
        db.close()
