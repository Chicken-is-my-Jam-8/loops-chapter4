
# Alexander J. Jackson
# four_digit.py

four_digit_num = int(input("Enter a four digit integer: "))

while not 1000 <= four_digit_num <= 9999:
    print("Invalid input. Please infer a four-digit integer.")
    four_digit_num = int(input("Enter a four digit integer: "))
else:
    digit_1 = four_digit_num // 1000
    digit_2 = (four_digit_num // 100) % 10
    digit_3 = (four_digit_num // 10) % 10
    digit_4 = four_digit_num % 10

    sum_digits = digit_1 + digit_2 + digit_3 + digit_4

    print("The individual digits of your input are:", digit_1, digit_2, digit_3, digit_4)
    print("The sum of teh digits is:", sum_digits)
