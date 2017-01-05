print('\n')
print("Welcome to our simple calculator ")


def input_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("You must enter a number please")
            pass
number1 = input_int("Insert your first number:")
number2 = input_int("Insert your second number:")
result_add = number1 + number2
result_mult = number1 * number2
result_sub = number1 - number2
result_div = number1 / number2

print("The result of addition between", number1, "and", number2, "equals", result_add)
print("The result of multiplication between", number1, "and", number2, "equals", result_mult)
print("The result of subtraction between", number1, "and", number2, "equals", result_sub)
print("The result of division between", number1, "and", number2, "equals", result_div)
