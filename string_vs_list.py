# coding=utf-8
print('')
print('first we will begin with one variable that contain a multiple words inside ')
print('')
trolley_str = "fruit, vegetable, meat, bread, fish, frozen"
trolley_list = ['fruit', "vegetable", 'meat', 'bread', "fish", 'frozen']
print('This is string contain multiple words inside but we cannot manipulate it')
print(trolley_str)
print('')
print('This is list that contain multiple objects inside')
print(trolley_list)
print('')
print('Advantage of list we can manipulate objects')
print(trolley_list[3])
print('')
print('Advantage of list we can manipulate objects, remove, delete, replace, insert')
trolley_list.remove('fruit')
print(trolley_list)
print('')
trolley_list.insert(4, 'drink')
print(trolley_list)
print('')
trolley_list.append('food')
print(trolley_list)
print('')
trolley_list[4] = "hygiene"
print(trolley_list[2:5])
print('')
print('This is default list that we can manipulate easily')
print(trolley_list)
print('We can delete object at exact position like delete position 0 that mean first object')
del trolley_list[0]
print(trolley_list)