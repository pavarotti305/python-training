import sys

introduction = "Module Sys allow interaction with user with special object stdin (standard input) and readline"
print(introduction)
introduction = sys.stdin.readline(18)
print(introduction)
print('')


def old_joke():
    sys.stdout.write('What this your name ?\n')
    print('Please enter you name below:')
    name = input()
    print('How old are you ?')
    print('Please enter you old below:')
    old = int(sys.stdin.readline())
    # old between 10 and 13
    if 10 <= old <= 13:
        print('%s That give 13 + 49 ? The migraine !' % name)
    elif 0 <= old <= 9:
        print("%s you are too young for this experience." % name)
    elif 14 <= old <= 17:
        print("%s You are not major you'll have to wait your 18 years." % name)
    else:
        print('%s Sorry your old is outside our preferences !' % name)


old_joke()

print(sys.version)
