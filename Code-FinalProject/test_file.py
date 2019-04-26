# Author: Yarong Liu
# Function: Test if the main program run successfully（Because pytest cannot run input() function,
# I just creat a new python file First_two.py and the only difference between two files is that
# all the input information in First_one.py has been changed to immutable information in First_two.py)


import pytest
from First_two import Auto_order

def test_web():
    ticket = Auto_order()
    a = ticket.run()
    assert(a == True)
