#Создать список и заполнить его элементами различных типов данных.
#Реализовать скрипт проверки типа данных каждого элемента.
#Использовать функцию type() для проверки типа.
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

hw_list = [22, 16, 'summer', None, -7.5, 'True', 88.65, True]
def hw_type(args):
    for args in range(len(hw_list)):
        print(type(hw_list[args]))
    return
hw_type(hw_list)