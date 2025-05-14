# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'fast_car_relational.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" fast_car "
            "LEFT JOIN makes ON fast_car.make_id = makes.make_id "
            "LEFT JOIN aspiration ON fast_car.aspiration_id = aspiration.aspiration_id "
            "LEFT JOIN cylinders ON fast_car.cylinders_id = cylinders.cylinder_id ")


def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  



make = input('Which make cars do you want to see: ')
print_parameter_query("model, top_speed, horsepower, torque, price",  "make = ? ORDER BY top_speed DESC",make)
