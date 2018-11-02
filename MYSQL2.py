# SQl_insert_query -  insert.py

import mysql.connector
from mysql.connector import Error
from mysql.connector import error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Entry',
                                         user='root',
                                         password='Alle')

    sql_insert_query = """ INSERT INTO Entry                                                                                                                                                                
                           (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99) 
                           VALUES 
                           ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}",
                           "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}") 
                           """.format()

    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query)
    connection.commit()

    print("Namn lagrats i person tabellen")

except mysql.connector.Error as error:
    connection.rollback()  # rollback if any exception occured
    print("Lagring misslyckades {}".format(error))
finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL koppling nerkopplad")



# Jag får no module named 'mysql', Varför?
