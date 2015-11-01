from domain import *
from Controller import *
from Validator import *

class UI:
	def __init__(self, my_controller):
		self._controller = my_controller

	@staticmethod
	def error():
		print("Error! Please review your input.")
	
	@staticmethod
	def print_menu():
		print("Available commands:")
		print("<1> Add a person and its activities")
		print("<2> Remove")
		print("<3> Update")
		print("<4> List persons and activities")
		print("<5> Search a person")
		print("<6> Search an activity")
		print("<7> Sorting")
		print("<8> Undo")
		print("<9> Redo")
		print("<0> Exit")
	
	def do_menu(self):
		UI.print_menu()
		while (True):
			comm = input("Give your command: ")
			if (comm == '0'):
				print("Goodbye!")
				return
			elif (comm == '1'):
				print("Adding the person and its activities.")
				p = UI.read_person()
				while (True):
					a = UI.read_activity(p)
					self._controller.add_activity(a)
					ok = input("Do you want to add another activity to this person? <y> or <n>: ")
					if (ok == 'y'):
						pass
					elif (ok =='n'):
						break
					else:
						print("Please answer with 'y' or 'n'.")
				self._controller.add_person(p)
			elif (comm == '4'):
				self._controller.print_persons()
			else:
				UI.error()						
	
	@staticmethod
	def read_person():
		while (True):
			ID = input("Give the person's ID: ")
			if (not Validator.verify_numeric(ID)):
				print("Please enter a valid ID. Only numericals!")
			else:
				break
		while (True):
			name = input("Give the person's name: ")
			if (not Validator.verify_name(name)):
				print("Please enter a valid name. No spaces!")
			else:
				break
		while (True):
			phone = input("Give the person's phone number: ")
			if (not Validator.verify_numeric(phone)):
				print("Please enter a valid phone number. Only numericals!")
			else:
				break
		address = input("Give the person's address: ")
		return (Persons(ID, name, phone, address))

	@staticmethod
	def read_activity(person):
		while (True):
			date = input("Give the date of the activity, (its year): ")
			if (not Validator.verify_time(date)):
				print("Please enter a valid year!")
			else:
				break
		while (True):
			time = input("Give the duration of the activity: ")
			if (not Validator.verify_time(time)):
				print("Please enter a valid duration, in hours!")
			else:
				break
		description = input("Give the description of this activity: ")
		return (Activities(person.ID, date, time, description))
