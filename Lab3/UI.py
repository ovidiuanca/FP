from domain import *
from Controller import *
from Validator import *

class UI:
	'''
	This is The UI of the application.
	'''
	def __init__(self, my_controller):
		self._controller = my_controller

	def print_menu(self):
		print("X=================MENU===================X")
		print("# <1>  Add an activity                   #")
		print("# <2>  Add a person                      #")
		print("# <3>  Remove person                     #")
		print("# <4>  Remove activity                   #")
		print("# <5>  List activities                   #")
		print("# <6>  List persons and their activities #")
		print("# <7>  Search an activity                #")
		print("# <8>  Search a person                   #")
		print("# <9>  Update an activity                #")
		print("# <10> Update a person                   #")
		print("# <11> Sorting                           #")
		print("# <12> Undo                              #")
		print("# <13> Redo                              #")
		print("# <0>  Exit                              #")
		print("X========================================X\n")
	
	def do_menu(self):
		'''
		This is the menu selector.
		'''
		while (True):
			self.print_menu()
			comm = input("Give your command: ")
			if (comm == '0'):
				print("Goodbye!")
				return
			elif (comm == '1'):
				self.add_activity()
			elif (comm == '2'):
				self.add_person()
			elif (comm == '3'):
				self.remove_person()
			elif (comm == '4'):
				self.remove_activity()
			elif (comm == '5'):
				self.print_activities()
			elif (comm == '6'):
				self.print_persons()
			elif (comm == '7'):
				self.search_activity()
			elif (comm == '8'):
				self.search_person()
			elif (comm == '9'):
				pass
			elif (comm == '10'):
				pass
			elif (comm == '11'):
				pass
			elif (comm == '12'):
				pass
			elif (comm == '13'):
				pass
			else:
				print("Command error!")

	def add_activity(self):
		while (True):
			ID = input("Insert the ID of the activity: ")
			if (Validator.verify_time(ID)):
				break
			else:
				print("ID must be numeric!")
		while (True):
			date = input("Insert the year of the activity: ")
			if (Validator.verify_time(date)):
				break
			else:
				print("Year must be numeric!")
		while (True):
			time = input("Insert the duration of the activity: ")
			if (Validator.verify_time(time)):
				break
			else:
				print("Duration has to be numeric!")
		description = input("Insert the description for this activity: ")
		if (not self._controller.search_activity(ID)):
			self._controller.add_activity(ID, date, time, description)
			print("\nActivity added succesfully.\n")
		else:
			print("\nActivity already exists!\n")

	def print_activities(self):
		if (not self._controller.exist_activities()):
			print("There are no activities, please add some")
		my_list = self._controller.getActivities()
		for act in my_list:
			self.print_one_activity(act)
	def print_persons(self):
		if (not self._controller.exist_persons()):
			print("There are no persons, please add some!")
			self.add_person()
		my_list = self._controller.getPersons()
		for pers in my_list:
			print("\nPerson:")
			self.print_one_person(pers)	

	def add_person(self):
		while (True):
			if (not self._controller.exist_activities()):
				print("Please add some activities first!")
				self.add_activity()
			ID = input("\nGive the ID for the person: ")
			if (Validator.verify_time(ID)):
				break
			else:
				print("Please enter a valid ID!")
		while (True):
			name = input("Give the name for the person: ")
			if (Validator.verify_name(name)):
				break
			else:
				print("Please enter a valid name. No spaces!")
		while (True):
			phone = input("Give the person's mobile number: ")
			if (Validator.verify_numeric(phone)):
				break
			else:
				print("Please enter a valid mobile number!")
		address = input("Give the address of the person: ")
		activities = []
		ok = 1
		while (ok):
			activity_id = input("\nGive the ID of an activity for the person: ")
			if (activity_id == '0'):
				break
			if (self._controller.search_activity(activity_id)):
				if (not self._controller.search_activity_of(activity_id, activities)):
					activities.append(self._controller.get_activity(activity_id))
				else:
					print("This person has already that activity!")
				while (True):
					dec = input("Do you want to add another activity for the person? <y> or <n>: ")
					if (dec == 'y'):
						break
					elif (dec == 'n'):
						ok = 0
						break
					else:
						print("Only answer with 'y' or 'n'!")	
			else:
				print("There is no such activity!")
		if (not self._controller.search_person(ID)):
			self._controller.add_person(ID, name, phone, address, activities)
			print("\nPerson succesfully added.\n")
		else:
			print("\nThis person already exists!\n")

	def remove_activity(self):
		if (not self._controller.exist_activities()):
			print("There are no activities!")
			self.add_activity()
		print("These are the current activities: ")
		self.print_activities()
		activity_id = input("Give the ID of the activity you want to remove: ")
		if (self._controller.search_activity(activity_id)):
			self._controller.remove_activity(activity_id)
		else:
			print("There is no such activity!")

	def remove_person(self):
		if (not self._controller.exist_persons()):
			print("There are no persons!")
		print("These are the current persons: ")
		self.print_persons()
		person_id = input("Give the ID of the person you want to remove: ")
		if (self._controller.search_person(person_id)):
			self._controller.remove_person(person_id)
		else:
			print("That person does not exist!")

	def search_activity(self):
		activity_id = input("Give the ID of the activity you want to search: ")
		if (self._controller.search_activity(activity_id)):
			activity = self._controller.get_activity(activity_id)
			self.print_one_activity(activity)
		else:
			print("There is no such activity!")

	def search_person(self):
		person_id = input("Give the ID of the person you want to search: ")
		if (self._controller.search_person(person_id)):
			person = self._controller.get_person(person_id)
			self.print_one_person(person)
		else:
			print("There is no such person!")

	def print_one_activity(self, activity):
		print("\nID: " + activity.ID + " Date: " + activity.date + " Time: " + activity.time + " Description: " + activity.description + '\n')

	def print_one_person(self, person):
		print("\nID: " + person.ID + " Name: " + person.name + " Mobile: " + person.phone + " Address: " + person.address + '\n')
		print("This person's activities are: \n")
		for act in person.activities:
			self.print_one_activity(act)
