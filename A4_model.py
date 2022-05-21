#!/usr/bin/env python
""" Model part of an MVC structured program.
    This program allows a user to analyze and manipulate the data from a csv file.
    This program was written for a class assignment at Algonquin College
"""

import csv
import A4_view
import A4_model
import re

__author__ = "Lillian Poon"
__version__ = "1.4"
__email__ = "poon0030@algonquinlive.com"




list=[]
i=1

def loadDataFromFile():
        fileName='InternationalCovid19Cases.csv'
        recordsShowing=200;
        # opening the CSV file and entering data into an array
        with open(fileName, 'r') as csv_file:
                        reader=csv.DictReader(csv_file)
                        #initializing counter for unique ID for each record
                        i=1
                        #creating for-loop to read data from csv file
                        for row in reader:
                                #force a TypeError exception if field has a None value (null)
                                if ((row['id']) is None) or ((row['date']) is None) or ((row['cases']) is None) or ((row['deaths']) is None) or ((row['name_fr']) is None) or ((row['name_en']) is None):
                                        raise TypeError("ERROR: Row is missing one or more fields")
                                else:
                                        #counter will only print the number of entries as specified on varilable recordsShowing
                                        if i>=(recordsShowing+1):
                                                break
                                        #entering data into the list/array
                                        list.append((row['id'], row['date'], int(row['cases']), int(row['deaths']), row['name_fr'], row['name_en'], i, 'Lillian Poon'))
                                        i+=1
# ----------------------------------FUNCTIONS FOR USER MENU START HERE---------------------------------
# ----------------------------- PROGRAM WRITTEN BY LILLIAN POON, 040899245------------------------------                              

                                
# Menu option 1: Reloadig the data from dataset, replacing the in-memory data (READ)                        
def option1():
        # erasing in-memory data
        list.clear()

        # loading new data into array               
        loadDataFromFile()

        print('data has been reloaded')


# Menu option 2: Persist data to CSV file to a new file (WRITING TO FILE I/O)
def option2():
        #opening a new file to write the data to
        with open('NewRecord.csv', 'w', newline='') as writeToNew:
                        writer=csv.writer(writeToNew, quoting=csv.QUOTE_ALL)
                        writer.writerows(list)
        # printing to console
        print('printing rows now')
        for row in list:
                print(row)
        print("The file has been written to NewRecord.csv")


def option3():
        id_input=input('Please enter numerical ID of record you wish to DISPLAY.\n')
        j=0
        counter=0
        for row in list:
                # scanning the array for the user's selection
                if list[j][6]==int(id_input):
                        # confirming whether or not the user wants to edit their selection
                        print('this is the row you\'ve selected to DISPLAY:')
                        print(row)
                        counter+=1
                        yesOrNo=input('Would you like to edit it? (Y/N)\n')
                        if (yesOrNo=='Y') or (yesOrNo=='y'):
                                # removing the row to replace with new data
                                list.remove(row)
                                # asking user input for new data
                                newID=input('enter new ID: ')
                                newDate=input('enter date in format yyyy-mm-dd: ')
                                newCases=input('enter number of cases: ')
                                newDeaths=input('enter number of deaths: ')
                                newNameFr=input('enter Country name in French: ')
                                newNameEn=input('enter Country name in English: ')
                                newValues=[newID, newDate, newCases, newDeaths, newNameFr, newNameEn, int(id_input), 'Lillian Poon']
                                # new data will be appended to the existing list
                                list.append(newValues)
                                print('your updated record: [' + newID + ', '+ newDate +', '+ newCases +', '+ newDeaths +', '+ newNameFr +', '+ newNameEn + '] has been saved to the in-memory data.')
                                # the data won't be persisted onto the new CSV file until the user chooses to
                                print('select option 2 from the main menu if you would like to save to new CSV file.')
                                break
                        else:
                                # if the user did not want to edit their selection, this option ends and user goes back to main menu
                                break
                j+=1
        if counter==0:
                print('no records matched your ID')

                
# Menu Option 4: Create a new record and store it in memory (CREATE)
def option4():
        print('CREATE A NEW RECORD')
        # asking user input for the new Record
        newID=input('enter ID: ')
        newDate=input('enter date in format yyyy-mm-dd: ')
        newCases=input('enter number of cases: ')
        newDeaths=input('enter number of deaths: ')
        newNameFr=input('enter Country name in French: ')
        newNameEn=input('enter Country name in English: ')
        newValues=[newID, newDate, newCases, newDeaths, newNameFr, newNameEn, i, 'Lillian Poon']
        # new data will be appended to the existing list
        list.append(newValues)
        print('your new record: ' + newID + ', '+ newDate +', '+ newCases +', '+ newDeaths +', '+ newNameFr +', '+ newNameEn + ' has been saved to the in-memory data.')
        # the data won't be persisted onto the new CSV file until the user chooses to
        print('select option 2 from the main menu if you would like to save to new CSV file.')

# Menu Option 5: DELETE a record
def option5(id_input):
        #id_input=input('Please enter numerical ID of record you wish to DELETE.\n')
        j=0
        counter=0
        for row in list:
                if list[j][6]==int(id_input):
                        # confirming whether or not the user wants to edit their selection
                        print('You have DELETED this row:')
                        print(row)
                        #yesOrNo=input('Would you like to proceed? (Y/N)\n')
                        #if (yesOrNo=='Y') or (yesOrNo=='y'):
                        print('\nSelect 2 from Main menu if you want to save to new CSV file')
                        country=list[j][4]
                        list.remove(row)
                        counter+=1
                        return country

                        #else:
                                # if the user did not want to proceed with their selection above, they will be brought back to the start of the
                                #       function and asked for a new ID to be deleted
                                #option6()
                j+=1
        if counter==0:
                print('no records matched your ID')

#written by Lillian Poon
# sort the list. User has the option to sort using any of the first four columns
def option6():
        # displaying the menu to choose which column to sort.
        A3_view.sort_menu()
        inputSort=int(input('how would you like your records sorted?\n'))
        sortedList=sorted(list, key=lambda covid: covid[inputSort-1])
        # writing the sorted records onto a new file
        with open('NewRecord_sorted.csv', 'w', newline='') as writeToNew:
                writer=csv.writer(writeToNew, quoting=csv.QUOTE_ALL)
                writer.writerows(sortedList)
        # displaying the new sorted list to the console
        for row in sortedList:
                print(row)
        print('list has been sorted and entered into a file called NewRecord_sorted.csv')
        A3_view.view_menu()

#written by Lillian Poon, 040899245
def option7():
        print('Column Names:\n1. id \n2. date \n3. cases \n4. deaths \n5. name_fr \n6. name_en\n')
        # user input for which columns to search
        colsToSearch=input('enter the column number(s) you wish to search, separated by a comma.\n')
        # user input for the search term, case sensitive
        searchString=input('enter your search term. Dates shoudl be in YYYY-MM-DD format\n')

        #parsing the column choices so we can search through each column            
        colNum=re.split('\W+', colsToSearch)

        # starting for-loop to seach one of the columns in order that the user entered
        for x in colNum:
            j=0
            counter=0
            #print(x)

            #translating column numbers to names
            if x=="1":
                searchColName="ID"
            elif x=="2":
                searchColName="Date"
            elif x=="3":
                searchColName="Cases"
            elif x=="4":
                searchColName="Deaths"
            elif x=="5":
                searchColName="Name_Fr"
            elif x=="6":
                searchColName="Name_En"
            else:
                searchColName="_____"
            searchCol=int(x)-1

            print("Search results for column: " + searchColName)

            # looping through the list to search the search term. Exception handling in case there is an error
            for row in list:
                try:
                    if str(list[j][searchCol])==searchString:
                        print(row)
                        counter+=1
                    j=j+1
                except NameError:
                    break
            # printing a string if no records are found in that column
            if counter==0:
                print("no records found for: " + searchString)


        


               
# ----------------------------------MENU FUNCTIONS END HERE---------------------------------

