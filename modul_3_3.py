def print_params(a=64, b='Возраст', c=True):
    print(a, b, c)


print_params(28)
print_params(b=25)
print_params()
print_params(c=[1, 2, 3])
values_list = [63.5, 'Точнее', 3]
values_dict = {'a': 5, 'b': 'Учение', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['Окончание', 19.47]
print_params(*values_list_2, 42)