from domain import *

class Repository:
	'''
	This is the Repository class, the parent class, that containes an empty list.
	'''
	def __init__(self):
		self.my_list = []

	def add(self, object):
		self.my_list.append(object)

	def getAll(self):
		return (self.my_list)
	
class PersonRepository(Repository):
	'''
	This is the PersonRepository class, that inherits from Repository class.
	'''
	def remove(self, person_id):
		for pers in self.my_list:
			if (pers.ID == person_id):
				self.my_list.remove(pers)
	
	def remove_person_activities(self, activity_id):
		for pers in self.my_list:
			for act in pers.activities:
				if (activity_id == act.ID):
					pers.activities.remove(act)

class ActivityRepository(Repository):
	def remove(self, activity_id):
		persons = PersonRepository()
		for act in self.my_list:
			if (act.ID == activity_id):
				self.my_list.remove(act)

