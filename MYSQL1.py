# DBconnector - connect.py

__author__ = 'JeffKing'

import mysql.connector
from mysql.connector import Error
from mysql.connector import error


try:
    connect = mysql.connector.connect(
        user='root',
        password='Alle',
        host='localhost',
        database='Entry')
    print(2 * '\n', "Det Funkar!! Du har lyckats att koppla Dig till Din databas!", 2 * '\n')


except mysql.connector.Error as e:

    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(2 * '\n', "Kopplingen fungerar inte!", 2 * '\n')

    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print(2 * '\n', "Databas namn hittades inte!!", 2 * '\n')

    else:
        print(e)



# Jag får no module named 'mysql', Varför ?
