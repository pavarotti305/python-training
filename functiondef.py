print('')
toys = ['Batman', 'Superman', "Spiderman", 'Hulk']


def son_toys(name, surname, address, sonname):
    print('''My name is %s, my surname is %s I live at %s
my son %s like toys as listed below:''' % (name, surname, address, sonname))
    for x in toys:
        print(x)
    return "Good job Lucien"


nom = "Pierrette"
postnom = "Ntumba Muamba"
adresse = "22A Bathurst Walk Iver"
nomfils = "Kingston Ntumba Muamba"

son_toys(nom, postnom, adresse, nomfils)
