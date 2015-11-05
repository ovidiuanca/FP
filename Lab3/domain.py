class Person:
	def __init__(self, ID, name, phone, address, activities):
		self.ID = ID
		self.name = name
		self.phone = phone
		self.address = address
		self.activities = activities

	def get_ID(self):
		return (self.ID)

	def get_name(self):
		return self.name

	def get_phone(self):
		return self.phone

	def get_address(self):
		return self.address

	def set_ID(self, ID):
		self.ID = ID

	def set_name(self, name):
		self.name = name

	def set_phone(self, phone):
		self.phone = phone

	def set_address(self, address):
		self.address = address

class Activity:
	def __init__(self, ID, date, time, description):
		self.ID = ID
		self.date = date
		self.time = time
		self.description = description

	def get_ID(self):
		return (self.ID)

	def get_date(self):
		return (self.date)

	def get_time(self):
		return (self.time)

	def get_description(self):
		return (self.description)

	def set_ID(self, ID):
		self.ID = ID

	def set_date(self, date):
		self.date = date

	def set_time(self, time):
		self.time = time

	def set_description(self, description):
		self.description = description
