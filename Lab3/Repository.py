from domain import *

class Repository:
	def __init__(self):
		self.my_list = []

class PersonRepository(Repository):

	def getAll(self):
		return self.my_list

	def add(self, person):
		self.my_list.append(person)

class ActivityRepository(Repository):
	def __init__(self):
		self.my_list = []

	def add(self, activity):
		self.my_list.append(activity)

	def getAll(self):
		return(self.my_list)
