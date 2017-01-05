print("print the absolute value of a number")
print(abs(-10.2))

print(list(range(2, 21, 2)))
print(list(range(20, 0, -2)))

print(sum([2, 6, 10]))

file_text = open('/Users/lucienntumba/Desktop/python.txt', 'w')
file_text.write('I\'m very happy because my training advance very well,')
file_text.write(' I can erase and write like I want this file Amazing')
file_text.close()


file_text = open('/Users/lucienntumba/Desktop/python.txt')
text = file_text.read()
print(text)

print("The lenght of the text is", len(text), "characters.") 