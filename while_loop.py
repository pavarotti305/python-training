print('')
print("Use while with modulus this expression for x in xrange(2, 21): is the same as i = 2 while i < 21:")
i = 2
while i < 21:
    print(i)
    stop10 = i == 10
    if i % 2 != 0:
        break
    if stop10:
        break
    i += 2
print('')
print("Same code with for")

for x in range(2, 21):
    if x % 2 == 0:
        print(x)
    if x > 10:
        break

print('''Syntax while expression is true:
statements
if expression is true:
break
i += 2 condition''')
l = list(range(10))
print(l, 'List of range the 10 like (0, 10) 0 included 10 excluded')
while l:
    l.pop(0)
    print(l)
