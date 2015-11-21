from domain import *
from Validator import *
class Repository:
	'''
	This is the Repository class, the parent class, that containes an empty list.
	'''
	def __init__(self):
		self.my_list = []
		self.undo_list = []
		self.redo_list = []

	def add(self, my_object):
		Validator.search_activity(self.my_list, my_object)
		self.my_list.append(my_object)
		self.undo_list.append(my_object)
		self.redo_list.append(my_object)

	def getAll(self):
		return (self.my_list)

	def undo(self):
		if (len(self.undo_list) > 0):
			self.redo_list.append(self.my_list)
			self.my_list = self.undo_list[-1]
			self.undo_list.pop(-1)
			return (1)
		return (0)
	
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

	def update_name(self, person_id, new_name):
		for pers in self.my_list:
			if (pers.ID == person_id):
				pers.set_name(new_name)

	def update_phone(self, person_id, new_phone):
		for pers in self.my_list:
			if (pers.ID == person_id):
				pers.set_phone(new_phone)

	def update_address(self, person_id, new_address):
		for pers in self.my_list:
			if (pers.ID == person_id):
				pers.set_address(new_address)

	def update_activities(self, person_id, new_activities, all_activities):
		for pers in self.my_list:
			if (pers.ID == person_id):
				del(pers.activities[:])
				for n_act in new_activities:
					for a_act in all_activities:
						if (n_act == a_act.ID):
							pers.activities.append(a_act)

class ActivityRepository(Repository):
	def remove(self, activity_id):
		persons = PersonRepository()
		for act in self.my_list:
			if (act.ID == activity_id):
				self.my_list.remove(act)

	def update_date(self, activity_id, new_date):
		for act in self.my_list:
			if (act.ID == activity_id):
				act.set_date(new_date)

	def update_time(self, activity_id, new_time):
		for act in self.my_list:
			if (act.ID == activity_id):
				act.set_time(new_time)
				
	def update_description(self, activity_id, new_description):
		for act in self.my_list:
			if (act.ID == activity_id):
				act.set_description(new_description)
