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
		'''
			Prints the menu
		'''
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
				self.update_activity()	
			elif (comm == '10'):
				self.update_person()
			elif (comm == '11'):
				self.sort()
			elif (comm == '12'):
				self.undo()
			elif (comm == '13'):
				pass
			else:
				print("Command error!")

	def add_activity(self):
		'''
			Add an activity command:\nAdds an activity to the activity repository.
		'''
		while (True):
			ID = input("Insert the ID of the activity: ")
			try:
				Validator.verify_ID(ID)
			except ValueError as e:
				print(e)
			else:
				break
		while (True):
			date = input("Insert the year of the activity: ")
			try:
				Validator.verify_year(date)
			except ValueError as e:
				print(e)
			else:
				break
		while (True):
			time = input("Insert the duration of the activity: ")
			try:
				Validator.verify_duration(time)
			except ValueError as e:
				print(e)
			else:
				break
		description = input("Insert the description for this activity: ")
		try:
			self._controller.add_activity(ID, date, time, description)
		except ValueError:
			print("That activity already exists!")
		else:
			print("Activity added succesfully.")

	def print_activities(self):
		'''
			List activities command:\nPrints the list of activities.
		'''
		if (not self._controller.exist_activities()):
			print("There are no activities, please add some")
		my_list = self._controller.getActivities()
		for act in my_list:
			self.print_one_activity(act)

	def print_persons(self):
		'''
			List persons command:\nPrints the list of persons, and each person's activities.
		'''
		if (not self._controller.exist_persons()):
			print("There are no persons, please add some!")
			self.add_person()
		my_list = self._controller.getPersons()
		for pers in my_list:
			print("Person:")
			self.print_one_person(pers)	

	def add_person(self):
		'''
			Add a person command:\nAdds a person to the person repository.
		'''
		exist = self._controller.exist_activities()
		try:
			Validator.exist_activities(exist)
		except ValueError:
			print("There are no activities. Please add some first!")
			self.add_activity()
		while (True):
			ID = input("Give the ID for the person: ")
			try:
				Validator.verify_ID(ID)
			except ValueError as e:
				print(e)
			else:
				break
		while (True):
			name = input("Give the name for the person: ")
			try:
				Validator.verify_name(name)
			except ValueError as e:
				print(e)
			else:
				break
		while (True):
			phone = input("Give the person's mobile number: ")
			try:
				Validator.verify_phone(phone)
			except ValueError as e:
				print(e)
			else:
				break
		address = input("Give the address of the person: ")
		activities = []
		ok = 1
		while (ok):
			activity_id = input("Give the ID of an activity for the person: ")
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
			print("Person succesfully added.")
		else:
			print("This person already exists!")

	def remove_activity(self):
		'''
			Remove an activity command:\nRemoves an activity from the activity repository. An ID is given by the user.
		'''
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
		'''
			Remove a person command:\nRemoves a person from the person repository. An ID is given by the user.
		'''
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
		'''
			Search an activity command:\nSearches for an activity in the activity repository that has the given ID. Prints the activity.
		'''
		activity_id = input("Give the ID of the activity you want to search: ")
		if (self._controller.search_activity(activity_id)):
			activity = self._controller.get_activity(activity_id)
			self.print_one_activity(activity)
		else:
			print("There is no such activity!")

	def search_person(self):
		'''
			Search a person command: Searches for a person in the person repository that has the given ID. Prints the person.
		'''
		person_id = input("Give the ID of the person you want to search: ")
		if (self._controller.search_person(person_id)):
			person = self._controller.get_person(person_id)
			self.print_one_person(person)
		else:
			print("There is no such person!")

	def print_one_activity(self, activity):
		'''
			Prints one activity.
		'''
		print("\nID: " + activity.ID + " Date: " + activity.date + " Time: " + activity.time + " Description: " + activity.description + '\n')

	def print_one_person(self, person):
		print("\nID: " + person.ID + " Name: " + person.name + " Mobile: " + person.phone + " Address: " + person.address + '\n')
		print("This person's activities are: \n")
		for act in person.activities:
			self.print_one_activity(act)

	def update_activity(self):
		'''
			Update activity command: The user gives an ID of an activity. Then he can update a field of his choice.
		'''
		self.print_activities()
		activity_id = input("Give the ID of the activity you want to update: ")
		if (not self._controller.search_activity(activity_id)):
			print("There is no such activity!")
		else:
			print("This is the current activity: ")
			activity = self._controller.get_activity(activity_id)
			self.print_one_activity(activity)
			self.print_activity_update_menu()
			comm = input("Give your command: ")
			if (comm == '1'):
				new_date = input("Give the new date: ")
				self._controller.update_date(activity_id, new_date)
			elif (comm == '2'):
				new_time = input("Give the new duration: ")
				self._controller.update_time(activity_id, new_time)
			elif (comm == '3'):
				new_description = input("Give the new description: ")
				self._controller.update_description(activity_id, new_description)
			elif (comm == '4'):
				self.do_menu()
			else:
				print("Wrong command!")

	def print_activity_update_menu(self):
		'''
			Prints the update activity submenu.
		'''
		print("\nWhat do you want to update?\n")
		print("X========================X")
		print("# <1> Change date        #")
		print("# <2> Change duration    #")
		print("# <3> Change description #")
		print("# <0> Abort              #")
		print("X========================X")
			
	def update_person(self):
		'''
			Update person command:\nThe user gives an ID of a person. Then he can update a field of his choice.
		'''
		print("These are the current persons: ")
		self.print_persons()
		person_id = input("Give the ID of the person you want to update: ")
		if (not self._controller.search_person(person_id)):
			print("There is no such person!")
		else:
			print("This is the person:")
			person = self._controller.get_person(person_id)
			self.print_one_person(person)
			self.print_person_update_menu()
			comm = input("Give your command: ")
			if (comm == '1'):
				new_name = input("Give the new name: ")
				self._controller.update_name(person_id, new_name)
			elif (comm == '2'):
				new_phone = input("Give the new mobile number: ")
				self._controller.update_phone(person_id, new_phone)
			elif (comm == '3'):
				new_address = input("Give the new address: ")
				self._controller.update_address(person_id, new_address)
			elif (comm == '4'):
				print("These are the current activities:")
				self.print_activities()
				new_activities = []
				act_string  = input("This person's activities are removed. Please add the ID's for the new ones: ")
				new_activities = act_string.split()
				self._controller.update_activities(person_id, new_activities)
			elif (comm == '0'):
				self.do_menu()				
			else:
				print("Wrong command!")

	def print_person_update_menu(self):
		'''
			Prints the update person submenu.
		'''
		print("\nWhat do you want to update?\n")
		print("X==========================X")
		print("# <1> Change name          #")
		print("# <2> Change mobile number #")
		print("# <3> Change address       #")
		print("# <4> Change activities    #")
		print("# <0> Abort                #")
		print("X==========================X")

	def sort(self):
		'''
			Lets the user select a command from the sorting submenu and reach a functionality.
		'''
		self.print_sort_menu()
		comm = input("Give your command: ")
		if (comm == '1'):
			self.print_sort1()
		elif (comm == '2'):
			self.print_sort2()
		elif (comm == '3'):
			self.print_sort3()
		elif (comm == '4'):
			self.print_sort4()
		elif (comm == '0'):
			self.do_menu()
		else:
			print("Wrong command!")

	def print_sort_menu(self):
		'''
			Prints the sorting submenu.
		'''
		print("X================================================================X")
		print("# <1> List a person's activities alphabetically                  #")
		print("# <2> List a person's activities by date                         #")
		print("# <3> List persons having activities between date1 and date2    #")
		print("# <4> List activities from a date, alphabetically by description #")
		print("# <0> Abort                                                      #")
		print("X================================================================X")

	def print_sort1(self):
		'''
			Lists a person's activity alphabetically. The user gives the ID of that person.
		'''
		person_id = input("Give the ID of the person you want its activities listed alphabetically: ")
		activities = self._controller.sort1(person_id)
		for act in activities:
			print(act.ID + " " + act.date + " " + act.time + " " + act.description)

	def print_sort2(self):
		'''
			Lists a person's activity by its date. The user gives the ID of that person.
		'''
		person_id = input("Give the ID of the person you want its activities listed by date: ")
		activities = self._controller.sort2(person_id)
		for act in activities:
			print(act.ID + " " + act.date + " " + act.time + " " + act.description)

	def print_sort3(self):
		'''
			Lists persons having activities between date1 and date2 given by the user.
		'''
		date1 = input("Give the date1, as an year: ")
		date2 = input("Give the date2, as an year: ")
		new_persons = self._controller.sort3(date1, date2)
		if (len(new_persons) == 0):
			print("No persons have activities in that interval!")
		else:
			for pers_name in new_persons:
				print(pers_name)

	def print_sort4(self):
		'''
			Lists activities from a date alphabetically by description. The date is given by the user.
		'''
		while (True):
			year = input("Give the date for the activities, to be ordered alphabetically: ")
			exist_year = self._controller.exist_year(year)
			try:
				Validator.exist_year(exist_year)
			except ValueError as e:
				print(e)
			else:
				break
		exist_act = self._controller.exist_activities()
		try:
			Validator.exist_activities(exist_act)
		except ValueError as e:
			print(e)
		else:
			activities = self._controller.sort4(year)
			for act in activities:
				print(act.ID + " " + act.date + " " + act.time + " " + act.description)

	def undo(self):
		'''
			Returns the list of persons to its previous state.
		'''
		code = UI.compute_undo(self)
		if (code == 1):
			print("Undo: Success!")
		else:
			print("Already at oldest change.")

	def compute_undo(self):
		'''
			
		'''
		code = self._controller.undo()
		return (code)
