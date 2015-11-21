from domain import *

class Validator:
	@staticmethod
	def verify_phone(string):
		if (not string.isdigit()):
			raise ValueError("Please insert a valid mobile number!")

	@staticmethod
	def verify_name(string):
		if (not string.isalpha()):
			raise ValueError("Please insert a valid name, no spaces allowed!")

	@staticmethod
	def verify_year(string):
		if (not(string.isdigit() and string[0] != '0')):
			raise ValueError("Please insert a valid year!")

	@staticmethod
	def verify_duration(string):
		if (not(string.isdigit())):
			raise ValueError("Please insert a valid duration!")

	@staticmethod
	def verify_ID(string):
		if (not(string.isdigit() and string[0] != '0')):
			raise ValueError("Please insert a valid ID!")

	@staticmethod
	def search_activity(my_list, my_object):
		for obj in my_list:
			if (obj.ID == my_object.ID):
				raise ValueError("That object already exists!")

	@staticmethod
	def exist_activities(exist):
		if(not exist):
			raise ValueError("There are no activities!")

	@staticmethod
	def exist_persons(exist):
		if (not exist):
			raise ValueError("There are no persons!")

	@staticmethod
	def exist_year(exist):
		if (not exist):
			raise ValueError("No activity is marked on that date!")
