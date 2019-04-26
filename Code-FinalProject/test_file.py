import pytest
from First_two import Auto_order

def test_web():
    ticket = Auto_order()
    a = ticket.run()
    assert(a == True)
