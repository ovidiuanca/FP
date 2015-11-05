from domain import *

class Controller:
	def __init__(self, person_repository, activity_repository):
		self._person_repository = person_repository
		self._activity_repository = activity_repository
	
	def add_person(self, ID, name, phone, address, activities):
		pers = Person(ID, name, phone, address, activities)
		self._person_repository.add(pers)

	def add_activity(self, ID, date, time, description):
		act = Activity(ID, date, time, description)
		self._activity_repository.add(act)

	def search_activity(self, activity_id):
		activities = self._activity_repository.getAll()
		for act in activities:
			if (act.ID == activity_id):
				return (True)
		return (False)

	def search_activity_of(self, activity_id, activities):
		for act in activities:
			if (act.ID == activity_id):
				return (True)
		return (False)

	def search_person(self, person_id):
		persons = self.getPersons()
		for pers in persons:
			if (person_id == pers.ID):
				return (True)
		return (False)

	def get_activity(self, activity_id):
		activities = self._activity_repository.getAll()
		for act in activities:
			if (act.ID == activity_id):
				return (act)
		return (False)

	def get_person(self, person_id):
		persons = self._person_repository.getAll()
		for pers in persons:
			if (pers.ID == person_id):
				return (pers)
		return (False)

	def getActivities(self):
		return (self._activity_repository.getAll())

	def getPersons(self):
		return (self._person_repository.getAll())

	def exist_activities(self):
		activities = self._activity_repository.getAll()
		if (len(activities) == 0):
			return (False)
		else:
			return (True)

	def exist_persons(self):
		persons = self._person_repository.getAll()
		if (len(persons) == 0):
			return (False)
		else:
			return (True)

	def remove_activity(self, activity_id):
		self._activity_repository.remove(activity_id)
		self._person_repository.remove_person_activities(activity_id)

	def remove_person(self, person_id):
		self._person_repository.remove(person_id)

