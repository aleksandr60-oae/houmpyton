my_dict = {'Pety': 2010, 'Gosha': 2012, 'Luka': 2008}
print(my_dict)
print(my_dict.get('Gosha'))
print(my_dict.get('Duny'))
my_dict.update({'Misha': 2005, 'Mark': 2011})
a = my_dict.pop('Pety')
print(a)
print(my_dict)
my_set = {'Abram', 'Sara', 2, 18, 'Abram', True, 25, 18}
print(my_set)
my_set.update({58, (25, 6, 4)})
my_set.discard('Abram')
print(my_set)
