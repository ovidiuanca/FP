from Repository import *
from Controller import *
from UI import *
from domain import *


'''
Initializing objects for the test.
'''
my_persons = PersonRepository()
my_activities = ActivityRepository()
my_controller = Controller(my_persons, my_activities)
'''
Testing getters and setters.
'''
activities = Activity(1, 2008, 25, "desc")
person = Person(1, "Nicu", "0745667300", "Motilor 101", activities)
try:
	assert person.get_ID() == 1
except:
	print("The ID getter is wrong!")
try:
	assert person.get_name() == "Nicu"
except:
	print("The name getter is wrong!")
try:
	assert person.get_phone() == "0745667300"
except:
	print("The phone getter is wrong!")
try:
	assert person.get_address() == "Motilor 101"
except:
	print("The address getter is wrong!")

person.set_ID(2)
person.set_name("Ovidiu")
person.set_phone("0722888222")
person.set_address("Memorandumului")

assert person.get_ID() == 2
assert person.get_name() == "Ovidiu"
assert person.get_phone() == "0722888222"
assert person.get_address() == "Memorandumului"

'''
Testing some Controller functions.
'''
#activities = []
#activities.append(Activity(1, 2008, 25, "Dancing"))
#activities.append(Activity(2, 1999, 20, "Bouncing"))
#assert my_controller.search_activity_of('1', activities[0]) == True
#assert my_controller.search_activity_of('3', activities[0]) == False
