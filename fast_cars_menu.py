# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'fast_car_relational.db'

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


menu_choice =''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Cars database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: Fastest 0 to 60 and top speed > 245\n'
                        'B: Higher torque\n'
                        'C: V-12 engine and naturally aspirated\n'
                        'D: horsepower > 900\n'
                        'E: price greater than 2.5 million and engine capacity greater than 2L\n'
                        'F: price less than 2m\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('0to60 and speed 245+')
    elif menu_choice == 'B':
        print_query('>torque')
    elif menu_choice == 'C':
        print_query('V-12 engine and naturally aspirated')
    elif menu_choice == 'D':
        print_query('horsepower > 900')
    elif menu_choice == 'E':
        print_query('price greater than 2.5 million and engine capacity greater than 2L')
    elif menu_choice == 'F':
        print_query('price less than 2m')
