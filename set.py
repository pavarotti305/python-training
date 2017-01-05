# Set french is Ensemble mean Unordered set of unique elements and set is alterable you can add replace or delete object
# All objects in the sets must be unique object, set are powerful for membership test
lucien_set = {1234, "Fruits", 'Sport', 25.25, "Kingston", "Sport"}
lucien_list = [1234, "Fruits", 'Sport', 25.25, "Kingston", "Sport"]
# Transform list to set
lucien_list_set = set(lucien_list)

print("After transforming list to set")
print(lucien_list_set)
lucien_list_set.add("Printer")
print("After added on set printer")
print(lucien_list_set)
lucien_list_set.remove(1234)
print("After removed 1234")
print(lucien_list_set)
lucien_list_set.update([4321, 'Ensemble'])
print("After updated 4321 and string Ensemble in this form update([])")
print(lucien_list_set)
print('')
print("Example operations in set - Difference between 2 sets + add 2 set | Unity or union & Intersection")
print('')
print('How to create unalterable set that mean you cannot modify object in this frozenset')
unalterable_lucien_set = frozenset(lucien_list_set)
print("You cannot modify this set")
print(unalterable_lucien_set)