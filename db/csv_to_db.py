# --------------------------------------------------------------------------------------------------------------------
# <copyright file="csv_to_db.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
import csv
import re
import sqlite3
from sqlite3 import Error

DATABASE = "truck.db"
CSVFILE = "trucks.csv"

def createConnection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def insertTruck(conn, truckRecord):

    # short circuit
    if (len(truckRecord) < 1):
        return -1

    # append the record
    sql = ''' INSERT INTO Trucks(truckName,truckAddress,menu,latitude,longitude,hoursOfOp)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, truckRecord)

    return cur.lastrowid

def transformRow(truckRecordRaw):
    truckRecord = []

    # escape conditions:
    #   remove food trucks with no lat/long
    #   remove food trucks with expired licenses
    if ((float(truckRecordRaw[4]) != 0) and 
        (float(truckRecordRaw[5]) != 0) and 
        (truckRecordRaw[2] != "EXPIRED")):
        truckRecord = truckRecordRaw
        truckRecord[3] = truckRecord[3].replace(":", ",")
        truckRecord[3] = re.sub("( )+", " ", truckRecord[3])
        if (truckRecord[6].strip() == ""):
            truckRecord[6] = "Information not available."
        else:
            truckRecord[6] = truckRecord[6].replace("/", ", ")
            truckRecord[6] = truckRecord[6].replace("-", " - ")
            truckRecord[6] = truckRecord[6].replace(":", ": ")
            truckRecord[6] = truckRecord[6].replace(";", "; ")
            truckRecord[6] = re.sub("( )+", " ", truckRecord[6])
        del truckRecord[2]

    return truckRecord

def main():

    # connect to db
    with createConnection(DATABASE) as conn:

        # load csv file
        with open(CSVFILE, newline = "") as csvFile:
            truckRecords = csv.reader(csvFile, delimiter=",", quotechar="\"")
            for truckRecordRaw in truckRecords:
                insertTruck(conn, transformRow(truckRecordRaw))

if __name__ == '__main__':
    main()