import csv
from Models.Product import Product
from Models.Sales import Sales
from Models.Salesman import Salesman

productRecords = []
salesRecords = []
salesmanRecords = []

def readData():
    #Read in the data from the CSV Files.
    print("Reading in data...")

    #First we will read in ProductData.csv and store it in our Product object.
    with open('Data\ProductData.csv', 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        next(file)
        for row in reader:
            productRecords.append(Product(row[0], row[1], row[2]))
            print(row)
        file.close()

    #Next we will read in SalesData.csv and store it in our Sales object.
    with open('Data\SalesData.csv', 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        next(file)
        for row in reader:
            salesRecords.append(Sales(row[0], row[1], row[2], row[3], row[4]))
            print(row)
        file.close()

     #First we will read in SalesmanData.csv and store it in our Salesman object.
    with open('Data\SalesmanData.csv', 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        next(file)
        for row in reader:
            salesmanRecords.append(Salesman(row[0], row[1]))
            print(row)
        file.close()

                  


def getConnectionString(): 
    #Get connection string values.
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    hostName = input("Enter host name: ")
    databaseName = input("Enter database name: ")

readData()
getConnectionString()