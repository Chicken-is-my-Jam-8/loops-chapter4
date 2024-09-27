
# Alexander J. Jackson
# four_digit2.py

proof = 1

while proof == 1:
    four_digit_num = int(input("Enter a four digit integer: "))

    if 1000 <= four_digit_num <= 9999:
        proof = 0
        digit_1 = four_digit_num // 1000
        digit_2 = (four_digit_num // 100) % 10
        digit_3 = (four_digit_num // 10) % 10
        digit_4 = four_digit_num % 10

        sum_digits = digit_1 + digit_2 + digit_3 + digit_4

        print("The individual digits of your input are:", digit_1, digit_2, digit_3, digit_4)
        print("The sum of teh digits is:", sum_digits)
    else:
        print("Invalid input. Please infer a four-digit integer.")
