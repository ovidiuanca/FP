from Repository import *
from Controller import *
from UI import *
from domain import *


'''
Testing getters and setters.
'''
activities = Activity(1, 2008, 25, "desc")
person = Person(1, "Nicu", "0745667300", "Motilor 101", activities)

assert person.get_ID() == 1
assert person.get_name() == "Nicu"
assert person.get_phone() == "0745667300"
assert person.get_address() == "Motilor 101"

person.set_ID(2)
person.set_name("Ovidiu")
person.set_phone("0722888222")
person.set_address("Memorandumului")

assert person.get_ID() == 2
assert person.get_name() == "Ovidiu"
assert person.get_phone() == "0722888222"
assert person.get_address() == "Memorandumului"
