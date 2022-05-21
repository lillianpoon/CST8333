# program written by Lillian Poon, student # 040899245

#!/usr/bin/env python
""" Controller part of an MVC structured program.
    This program allows a user to analyze and manipulate the data from a csv file.
    This program was written for a class assignment at Algonquin College
"""

import A4_model
import unittest
import A4_view
from collections import OrderedDict

__author__ = "Lillian Poon"
__version__ = "1.3"
__email__ = "poon0030@algonquinlive.com"


i=1

#recordsShowing=100;
A4_model.loadDataFromFile()

A4_view.view_menu()
input_menu=0

# processing which option to direct the user to
while input_menu!=7:
    input_menu=input('Please select an option from 1-7. (Enter \'9\' to display Menu) \n')
    if (input_menu=='1'):
        A4_model.option1()
    elif (input_menu=='2'):
        A4_model.option2()
    elif (input_menu=='3'):
        A4_model.option3()
    elif (input_menu=='4'):
        A4_model.option4()
        i+=1
    elif (input_menu=='5'):
        id_input=input('Please enter numerical ID of record you wish to DELETE.\n')
        A4_model.option5(id_input)
    elif (input_menu=='6'):
        A4_model.option6()
    elif (input_menu=='7'):
        A4_model.option7()
    elif (input_menu=='8'):
        break
    elif (input_menu=='9'):
        A4_view.view_menu()

    A4_view.print_owner()
            
print('goodbye')
print('program written by Lillian Poon, student # 040899245')


