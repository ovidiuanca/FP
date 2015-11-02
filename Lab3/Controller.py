from domain import *

class Controller:
	def __init__(self, person_repository, activity_repository):
		self._person_repository = person_repository
		self._activity_repository = activity_repository
	
	def add_person(self, ID, name, phone, address, activities):
		self._person_repository.add(Person(ID, name, phone, address, activities))

	def add_activity(self, ID, date, time, description):
		self._activity_repository.add(Activity(ID, date, time, description))

	def search_activity(self, activity_id):
		activities = self._activity_repository.getAll()
		for act in activities:
			if (act.ID == activity_id):
				return (True)
		return (False)

	def get_activity(self, activity_id):
		activities = self._activity_repository.getAll()
		for act in activities:
			if (act.ID == activity_id):
				return (act)
		return (0)

	def search_person(self, id_to_check):
		self._repository.search_person(id_to_check)

	def getActivities(self):
		return (self._activity_repository.getAll())

	def getPersons(self):
		return (self._person_repository.getAll())
