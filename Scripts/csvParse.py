#!/usr/bin/env python

import sqlite3
import csv
import pandas as pd
import copy
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

# def create_address(conn, address):
#     """
#     Add address to database
#     """
#     sql = '''INSERT INTO  address'''


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def openCSV():
    #with open('E:/revre/revreTech\EdmontonData/EdmontonHseData.csv', newline='') as csvfile:
    test = pd.read_csv('E:/revre/revreTech\EdmontonData/EdmontonHseData.csv',sep=',')    
    # get number of columns
    test.columns = test.columns.str.replace('\s+','_')

    masterList =[]

    # Snaggin all the things
    hood = test.Neighbourhood
    price = test.Assessed_Value
    number = test.House_Number
    street = test.Street_Name
    suite = test.Suite


    maxLen = len(number)-1
    i = 0 # i refers to index

    while(i <= maxLen):
        totalAddress = ""
        hnplist = []
        # Street Number Style Change
        sn = str(number[i])
       # sn = number[i].astype(str)
        sn = str(sn)
        sn = sn.replace('.0','')

        # Works
        if(type(suite[i]) != float):
            totalAddress = str(suite[i]) + " " + sn + " " + str(street[i])
        else:
            totalAddress = sn + " " + str(street[i])

        # If no street exists then take it out
        if(str(street[i]) == 'nan'):
            i+=1
            continue

        # Price Stuff
        intPrice = price[i][1:]
        intPrice = int(intPrice)

        # Holds the address
        hnplist.append(totalAddress)
        hnplist.append(intPrice)
        hnplist.append(hood[i])

        masterList.append(hnplist)
        i+=1

    # reset index
    # Dict contains price and count
    print("Dict One Starting")
    i = 0
    aDict = {}
    print(len(masterList))
    while( i <= len(masterList)-1):
        print(masterList[i][2])
        if(masterList[i][2] not in aDict):
            aDict[masterList[i][2]] = [masterList[i][1], 1]
        else:
            aDict[masterList[i][2]][0] += masterList[i][1]
            aDict[masterList[i][2]][1] += 1
        print(aDict[masterList[i][2]])
        i+=1
        

    # once dict is made create average
    nbhdavg = {}
    for aKey in aDict:
        nbhdavg[aKey] = int(aDict[aKey][0]/aDict[aKey][1])


    return masterList, nbhdavg


def main():
    database = 'E:/revre/revreTech/testSite.sqlite3'
 
    # create a database connection
    addyList, averages = openCSV()

    # Connection to Database works
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        print("2. Query all tasks")
        print("DataBaseCONNECT")


if __name__ == '__main__':
    main()