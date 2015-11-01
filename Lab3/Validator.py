class Validator:
	@staticmethod
	def verify_numeric(string):
		'''
		Returns 1 if the string is numerical and 0 otherwise.
		'''
		if (string.isdigit()):
			return (1)
		else:
			return (0)

	@staticmethod
	def verify_name(string):
		'''
		Returns 1 if the string contains only letters and 0 otherwise.
		'''
		if (string.isalpha()):
			return (1)
		else:
			return (0)

	@staticmethod
	def verify_time(string):
		if (string.isdigit() and string[0] != '0'):
			return (1)
		else:
			return (0)
