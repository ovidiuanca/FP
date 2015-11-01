from domain import *

class Repository:
	def __init__(self):
		self.list_persons = []
		self.list_activities = []

	def add_p(self, person):
		self.list_persons.append(person)

	def add_a(self, activity):
		self.list_activities.append(activity)

	def print(self):
		for obj in self.list_persons:
			print("ID: " + obj.ID)
			print("Name: " + obj.name)
			print("Phone: " + obj.phone)
			print("Address: " + obj.address)
			print("\nThe activities for " + obj.name + ": ")
			for act in self.list_activities:
				if (act.ID == obj.ID):
					print("	ID: " + act.ID)
					print("	Date: " + act.date)
					print("	Time: " + act.time)
					print("	Description: " + act.description + '\n')
