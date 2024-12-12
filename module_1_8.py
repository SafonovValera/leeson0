my_dict = {'Valera':1972, 'Ola':1992, 'Vika':1989, 'Dima':2001}
print(my_dict)
print(my_dict['Valera'])
print(my_dict.get('Kati'))
my_dict['Max']=2006
my_dict['Gena']=1999
print(my_dict)
a = my_dict.pop('Valera')
print(a)
print(my_dict)


my_set= {1, 2, 3, 1, 2, 3, (1, 2, 3), True}
print(my_set)
my_set.add(4)
my_set.add((2, 3, 4))
my_set.discard(1)
print(my_set)