from domain import *

class Controller:
	def __init__(self, my_repository):
		self._repository = my_repository
	
	def add_person(self, person):
		self._repository.add_p(person)

	def add_activity(self, activity):
		self._repository.add_a(activity)

	def print_persons(self):
		self._repository.print()

	
	
