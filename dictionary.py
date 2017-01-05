# coding=utf-8
print('')
print('''Dictionary also called map is a collection of object like tuple or list but the
major difference is that each object in dictionary possess a key and corresponding value, dictionary
can be compare at association of a key and a value like application if we talk for mathematics''')
print('')
favorite_sport = {'Lucien Ntumba': 1234,
                  'Kingston': 'Basket and Football',
                  'Melchior': 'Baseball',
                  'Djokovic': 'Tennis',
                  'Peyton Manning': 'NFL',
                  'Thierry Omeyer': 'Hand-Ball'}
print(favorite_sport['Djokovic'])
print(favorite_sport['Lucien Ntumba'])
print('')
print("Like list we can manipulate easily dictionary, we can delete, remove or replace value and key")
del favorite_sport['Peyton Manning']
print(favorite_sport)
print('')
favorite_sport['Lucien Ntumba'] = 'Rugby'
print(favorite_sport)
print("We cannot put together dictionary because all object have already value and key")

favorite_sport['Peyton Manning'] = 'Jerome'
print(favorite_sport)