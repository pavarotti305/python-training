model_list = ['diamond_ring', 'home', 'screen', 'shoes', 'vuitton', 'gucci']
some_numbers = [1, 2, 5, 10, 20]
some_str = ['is', 'not', "rocket", 'science']


def liste(l):
    for i in l:
        print(i)
    return 'Well done'


def function_test(my_name, my_address, wife):
    print('''My name is %s I live at %s and
my wife %s love: see list below %s''' % (my_name, my_address, wife, liste(model_list)))
    return 'Thank you'


name1 = 'Lucien NTUMBA MUAMBA'
location1 = '22A Bathurst walk Iver SL0 9AZ'
epouse = "Pierrette NTUMBA"

function_test(name1, location1, epouse)



