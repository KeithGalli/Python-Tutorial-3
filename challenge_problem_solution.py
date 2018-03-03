number = 123

if (number < 100 or number >= 300) and (number % 3 == 0 or number % 7 == 0):
	if number % 3 == 0 and number % 7 == 0:
		print("Divisible by both")
	elif number % 3 == 0:
		print("Divisible by 3")
	else:
		print("Divisible by 7")
else:
	print("Not a special number")