#!/usr/bin/env python
""" View part of an MVC structured program.
    This program allows a user to analyze and manipulate the data from a csv file.
    This program was written for a class assignment at Algonquin College
"""

import A4_model

__author__ = "Lillian Poon"
__version__ = "1.3"
__email__ = "poon0030@algonquinlive.com"

import A4_model                               

# main menu for user selection
def view_menu():
    print('program written by Lillian Poon, student # 040899245')
    print('---------------------------------')
    print('MENU:')
    print('1. Reload data from Dataset')
    print('2. Persist data to a new file and display on console')
    print('3. Select, display and edit a file from the database')
    print('4. Create a new record and store it in memory')
    print('5. Select and delete a record')
    print('6. Sort the list')
    print('7. Search the records')
    print('8. Exit')

# prints author information
def print_owner():
    print ('program written by Lillian Poon, student # 040899245')

# menu options of columns that the user can sort
def sort_menu():
    print('1. Sort by Country ID')
    print('2. Sort by date')
    print('3. Sort by Number of cases')
    print('4. Sort by Number of deaths')
