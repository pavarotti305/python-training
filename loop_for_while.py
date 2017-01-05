from random import randint
print('''for x in range(1, 11):
print x, x**2 print x and x exponent 2
print 'break' end of statement
mean variable x will browse range between 1 to 10, 1 included 11 is excluded''')
a = randint(2, 20)
b = randint(22, 40)


for x in range(a, b):
    if x % 2 == 0:
        print(x)
print('')
print('''try even number with while loop first initialize even_numbers to 0
Second use your loop while with expression after to avoids an indefinite loop use statement to limit loop
after your limit statement you can print you variable''')
even_numbers = 0

while even_numbers < 21:
    print(even_numbers)
    if even_numbers % 2 != 0:
        break
    even_numbers += 2