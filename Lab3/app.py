from UI import *
from Repository import *
from Controller import *

def main():
	my_persons = PersonRepository()
	my_activities = ActivityRepository()
	my_Controller = Controller(my_persons, my_activities)

	my_UI = UI(my_Controller)
	my_UI.do_menu()

if (__name__ == '__main__'):
	main()
