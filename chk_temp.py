
# Alexander J. Jackson
# chk_temp.py

max_temp = 80
real_temp = int(input("Please enter a temperature(Fahrenheit): "))

while real_temp >= max_temp:
	print()
	print("The temperature is too high.")
	real_temp = int(input("Please enter a temperature(Fahrenheit): "))
else:
	print()
	print("The temperature is acceptable.")
