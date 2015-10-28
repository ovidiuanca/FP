def verifyDigit(c, number):
	while number:
		if c == int(number % 10):
			return 1
		number = int(number / 10)
	return 0

def testVerifyDigit():
	assert verifyDigit(1,1234) == 1
	assert verifyDigit(3,1024) == 0

def verify(a, b):
	while a:
		if not verifyDigit(int(a % 10), b):
			return 0
		a = int(a / 10)
	return 1

def testVerify():
	assert verify(123, 333322211) == 1
	assert verify(123123, 8124712) == 0

def printResult(a, b):
	if verify(a, b) and verify(b, a):
		print("Numbers have the P property.")
	else:
		print("Numbers DONT have the P property.")

a = int(input("Give the number a: "))
b = int(input("Give the number b: "))


testVerifyDigit()
testVerify()
printResult(a, b)
