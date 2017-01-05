print('\n')
print("Please can you enter your first name beginning to Upper case")
while True:
    name = input('What this your first name:')
# if name is the same as if bool(name) or if name == true
    if name:
        print("Thank you for your validation %s." % name)
    if name == 'Kingston':
        print("Well done Kingston you are the master.")
        break
    if name == 'Melchior':
        print("Morning Melchior what are you doing here.")
        break
    if name == 'Lucien':
        print("Ho Lucien you are too old for playing child game.")
        break
    if name == 'Mikhail':
        print("The Artnewspaper is the place where I will finish my career Hooo Noooo.")
        break
    if name == 'Pierrette':
        print("Good jod Kingston mum")
        break
# rstrip delete all blank space and enter click
    if not bool(name.rstrip()):
        print("You must enter your first name to validate this step.")
    else:
        print("\"Good bye %s your name is not stored in our Database contact our Administrator\"" % name)
        break
