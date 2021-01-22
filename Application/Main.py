import csv
import pyodbc
import sys 

#Open a connection to the DB and start reading the data straight from the CSV file into the DB.
try:
    connection = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=desktop-m3p0ek9\localhost;"
        "Database=Ark;"
        "Trusted_Connection=yes")

    cursor = connection.cursor()

    print("Storing data in the database...")

    #First we will read in SalesmanData.csv and store it in our Salesman table.
    with open('Data\SalesmanData.csv', 'r') as salesmanFile:
        reader = csv.reader(salesmanFile, delimiter = ',')
        next(salesmanFile)
        for row in reader:
            insertStatement = """INSERT INTO salesmanData VALUES (?, ?)"""
            cursor.execute(insertStatement, row)
            connection.commit()
        salesmanFile.close()

    #Next we will read in ProductData.csv and store it in our Product table.
    with open('Data\ProductData.csv', 'r') as productsFile:
        reader = csv.reader(productsFile, delimiter = ',')
        next(productsFile)
        for row in reader:
            insertStatement = """INSERT INTO productData VALUES (?, ?, ?)"""
            cursor.execute(insertStatement, row)
            connection.commit()
        productsFile.close()

    #Finally we will read in SalesData.csv and store it in our Sales table.
    with open('Data\SalesData.csv', 'r') as salesFile:
        reader = csv.reader(salesFile, delimiter = ',')
        next(salesFile)
        for row in reader:
            insertStatement = """INSERT INTO salesData VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(insertStatement, row)
            connection.commit()
        salesFile.close()

        #Close the connection.
        connection.close()

#if an exception occurs, throw an error and exit the program.
except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        if sqlstate == '28000':
            sys.exit("\nAn error has occured while obtaining a connection to SQLServer... \nExiting the program gracefully.")         

#upon completion of the date being persisted, close the cursor and and the connection before exiting the program.
sys.exit("\nTransaction complete: Exiting the program gracefully.")
