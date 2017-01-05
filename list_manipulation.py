# coding=utf-8
print('')
some_numbers = [1, 2, 5, 10, 20]
some_str = ['is', 'not', "rocket", 'science']
print("We can put together two or more lists at one variable ")
all_numbers_str = [some_numbers, some_str]
print(all_numbers_str)
print('')
print('Or we can use only some objects of our lists')
print(some_numbers[0], some_str)
print('')
print("We can assembly two or more lists at one variable ")
family_number = [1, 2, 3, 4, 5, 6]
family_name = ['mado', 'didi', 'djobaf', 'pava', 'koze', 'cedro']
print(family_number[4], family_name[4])
print(family_number + family_name)
