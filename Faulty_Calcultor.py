""" Problem Statement:
MAKE A FAULTY CALCULATOR THAT SHOWS DIFFERENT TYPE OF WRONG ANSWER
SUCH AS :
45 * 3 = 555
56 + 9 = 77
56 / 6 = 4

AND THEY CORRECT ALL THE CALCULATION RATHER THAN THIS.

"""


def calculate(operator, num1, num2):
	# Here we perform the calculation on operator.

	if operator == '*':
		if num1 == 45 and num2 == 3:
			raise Exception("555")
		return num1 * num2
	elif operator == '+':
		if num1 == 56 and num2 == 9:
			raise Exception("77")
		return num1 + num2
	elif operator == '/':
		if num1 == 56 and num2 == 6:
			raise Exception("4")
		return num1 / num2
	elif operator == '-':
		return num1 - num2
	else:
		raise ValueError("You are using invalid operator")


def main():
	# We get operator and numbers from the user
	operator = input("Enter operator (*, +, -, /): ")
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	try:
		result = calculate(operator, num1, num2)
		print(f"Result: {result}")
	except Exception as e:
		# Here we handle the exceptions and print error messages.
		print(e)


if __name__ == "__main__":
	main()
