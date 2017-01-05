a = "kingston is my first son."


def string_list(liste) -> str:
    print(liste.split())

string_list(a)


chaine_list = ['kingston', 'is', 'my', 'first', 'son.']
chaine_list.index(0, 'Jerome')


def list_string(string):
    print(" ".join(string))
    return "Well Done"

list_string(chaine_list)