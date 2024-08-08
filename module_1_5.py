immutable_var = "это строка", 25, 10.51, False, '28'
print(immutable_var)
#immutable_var[2]=8.2#-ошибка,переменная immutable_var является кортэжэм,неизменяемой, упорядоченой последовательностью
#print(immutable_var)#элементов.
mutable_list = ["это список", True, 3, 2.9]
mutable_list[1] = "изменилось"
print(mutable_list)
