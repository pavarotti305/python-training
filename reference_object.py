import copy
# Share reference save memory of duplicate unused object
a = 3
b = a
c = 'Take the last reference'
a = c
print(a)
print('How to create a shadow copy of list')
d = [1, 2, "copy"]
print("[:] list shadow copy for 2 variable referenced on the same list")
e = d[:]
d[2] = 'shallow'
print("The result of list d will replace element 2 by shadow")
print(d)
print('Advantage of shallow copy list e will stay the same as first created lis d')
print(e)
print("The deepcopy create first full copy of object is if we use a list inside with another sublist")
f = [0, ['copy']]
print('This code mean h have a static full copy of variable f ')
h = copy.deepcopy(f)
f[1][0] = "test"
print(f)
print(h)
