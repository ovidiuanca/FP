def error():
	'''
	Prints error message if the input is wrong.
	'''
	print("Input error. Please review your input.")

def addElement(list, number):
	'''
	Adds an element at the end of the list.
	list - the list.
	number - the value to be added.
	'''
	list.append(number)

def addElementAt(list, position, number):
	'''
	Adds an element in a list at a given position, replacing what was initially.
	'''
	list[position] = number

def removePosition(list, position):
	'''
	Removes the element at the given position from the list.
	'''
	list.pop(position)

def removeBetween(list, begin, end):
	'''
	Removes a sequence between two positions from the list.
	'''
	i = 1
	while (i <= end - begin + 1):
			list.pop(begin)
			i += 1

def isSublist(list, poz, sublist):
	'''
	Returns 1 if the sublist is the same as the sublist starting at the given position in the main list.
	'''
	j = 0
	i = poz
	while (i < (poz + len(sublist) - 1)):
			if (list[i] != sublist[j]):
					return (0)
			j += 1
			i += 1
	return (1)

def verifyIsSublist(list, poz, sublist):
	'''
	Verifies isSublist()
	'''
	assert isSublist([1, 2, 3, 4, 5], 1, [2, 3, 4]) == 1
	assert isSublist([1, 2, 3, 4, 5], 0, [2, 3, 4]) == 0

def removeSublist(list, poz, size):
	'''
	Removes a sublist from the list, having the starting position of the sublist and its size.
	'''
	for i in range(size):
			list.pop(poz)

def insertElement(list, poz, result):
	'''
	Inserts a sublist into the list, at the given position.
	'''
	j = 0
	for i in range(len(result)):
			list.insert(poz, result[j])
			poz += 1
			j += 1
			
def replaceSublist(list, sublist, result):
	'''
	Replaces a sublist with the given sublist in the main list.
	'''
	for i in range(len(list) - len(sublist) + 1):
			if (isSublist(list, i, sublist)):
					removeSublist(list, i, len(sublist))
					insertElement(list, i, result)

def prime(number):
	'''
	Returns 1 if the number is prime and 0 otherwise.
	'''
	if number < 2:
			return (0)
	for i in range (2, int(number / 2 + 1)):
			if number % i == 0:
					return (0)
	return (1)

def verifyPrime():
	'''
	Verifies prime().
	'''
	assert prime(13) == 1
	assert prime(4) == 0

def primeBetween(list, begin, end):
	'''
	Prints the prime numbers between two given positions.
	'''
	for i in range(begin, end + 1):
			if prime(list[i]):
					print(list[i], end = " ")
	print()

def oddBetween(list, begin, end):
	'''
	Prints the odd numbers between two given positions.
	'''
	for i in range(begin, end + 1):
			if list[i] % 2 != 0:
					print(list[i], end = " ")
	print()

def sumBetween(list, begin, end):
	'''
	Prints the sum of a sequence between two positions.
	'''
	sum = 0
	for i in range(begin, end + 1):
			sum += list[i]
	print(sum)

def gcd(a, b):
	'''
	Returns the gcd of two numbers.
	'''
	while (a != b):
			if (a > b):
					a -= b
			else:
					b -= a
	return a

def verifyGcd():
	'''
	verifies gcd().
	'''
	assert gcd(12, 36) == 12
	assert gcd(13, 28) == 1

def gcdBetween(list, begin, end):
	'''
	Prints the gcd of a sublist between two positions.
	'''
	res = gcd(list[begin], list[begin + 1])
	for i in range(begin + 2, end):
			res = gcd(res, list[i])
	print(res)

def maxBetween(list, begin, end):
	'''
	Prints the maximum value between two positions.
	'''
	max = 0
	for i in range(begin, end + 1):
		if (list[i] > max):
				max = list[i]
	print(max)

def retainPrimes(list):
	'''
	Modifies the list retaining only the prime numbers.
	'''
	i = 0
	while (i < len(list)):
			if (not prime(list[i])):
					list.pop(i)
			else:
					i += 1

def retainNegatives(list):
	'''
	Modifies the list retaining only the negative numbers.
	'''
	i = 0
	while (i < len(list)):
			if (list[i] >= 0):
					list.pop(i)
			else:
					i += 1

def undo(Thelist, copy):
	'''
	Undoes the last operation.
	'''
	Thelist = list(copy)
	return (Thelist)

def replaceCommand(Thelist, menu):
	'''
	Doeis the actual 'replace with' command. Returns 0 if it's an error input.
	'''
	ok = 1
	sublist = []
	result = []
	i = 1
	while (menu[i].isdigit()):
			sublist.append(int(menu[i]))
			i += 1
	if (menu[i] != 'with'):
			return (0)
	i += 1
	while (i < len(menu) and menu[i].isdigit()):
			result.append(int(menu[i]))
			i += 1
	if (i != len(menu)):
			return (0)
	replaceSublist(Thelist, sublist, result)
	return (1)

def copyList(Thelist, undoList):
	y = list(Thelist)
	undoList.append(y)

def doMenu(Thelist):
	'''
	Implementation of the user interface. It's based on the command given by the user.
	Thelist - the initial list.
	copy - a copy of the list, before the last made change.
	'''
	ok = 1
	undoList = []
	redoList = []
	while (ok):
		string = input("Give the command: ")
		menu = string.split() # Menu will become a list, the delimitator is a 'space' in the given string.
		v_error = 0
		if (len(menu) == 2 and menu[0] == 'add'):
				copyList(Thelist, undoList)
				addElement(Thelist, int(menu[1]))
				copyList(Thelist, redoList)
		elif (len(menu) == 4 and menu[0] == 'insert' and menu[1].isdigit() and menu[2] == 'at' and menu[3].isdigit()):
				copyList(Thelist, undoList)
				addElementAt(Thelist, int(menu[3]), int(menu[1]))
				copyList(Thelist, redoList)
		elif (len(menu) == 2 and menu[0] == 'remove' and menu[1].isdigit()):
				copyList(Thelist, undoList)
				removePosition(Thelist, int(menu[1]))
				copyList(Thelist, redoList)
		elif (len(menu) == 5 and menu[0] == 'remove' and menu[1] == 'from' and menu[2].isdigit() and menu[3] == 'to' and menu[4].isdigit()):
				copyList(Thelist, undoList)
				removeBetween(Thelist, int(menu[2]), int(menu[4]))
				copyList(Thelist, redoList)
		elif (menu[0] == 'replace'):
				copyList(Thelist, undoList)
				replaceCommand(Thelist, menu)
				copyList(Thelist, redoList)
				if (not replaceCommand(Thelist, menu)):
						v_error = 1
						undoList.pop(-1)
						redoList.pop(-1)
		elif (menu[0] == 'prime' and menu[1] == 'from' and menu[2].isdigit() and menu[3] == 'to' and menu[4].isdigit()):
				primeBetween(Thelist, int(menu[2]), int(menu[4]))
		elif (menu[0] == 'odd' and menu[1] == 'from' and menu[2].isdigit() and menu[3] == 'to' and menu[4].isdigit()):
				oddBetween(Thelist, int(menu[2]), int(menu[4]))
		elif (menu[0] == 'sum' and menu[1] == 'from' and menu[2].isdigit() and menu[3] == 'to' and menu[4].isdigit()):	
				sumBetween(Thelist, int(menu[2]), int(menu[4]))
		elif (menu[0] == 'gcd' and menu[1] == 'from' and menu[2].isdigit() and menu[3] == 'to' and menu[4].isdigit()):
				gcdBetween(Thelist, int(menu[2]), int(menu[4]))
		elif (menu[0] == 'max' and menu[1] == 'from' and menu[2].isdigit() and menu[3] == 'to' and menu[4].isdigit()):
				maxBetween(Thelist, int(menu[2]), int(menu[4]))
		elif (menu[0] == 'filter' and menu[1] == 'prime'):
				copyList(Thelist, undoList)
				retainPrimes(Thelist)
				copyList(Thelist, redoList)
		elif (menu[0] == 'filter' and menu[1] == 'negative'):
				copyList(Thelist, undoList)
				retainNegatives(Thelist)
				copyList(Thelist, redoList)
		elif (menu[0] == 'undo' and len(menu) == 1):
				copyList(Thelist, redoList)
				Thelist = list(undoList[-1])
				undoList.pop(-1)
		elif (menu[0] == 'redo' and len(menu) == 1):
				copyList(Thelist, undoList)
				Thelist = list(redoList[-1])
				redoList.pop(-1)
		elif (menu[0] == 'exit' and len(menu) == 1):
				ok = 0
		else:
				v_error = 1
		if (not v_error):
				print("List after: ", Thelist)
		else:
				error()

def main():
	'''
	The main function.
	'''
	Thelist = []
	print("List before: ", Thelist)
	doMenu(Thelist)

# Required for running the main function.
if __name__ == "__main__":
	main()
