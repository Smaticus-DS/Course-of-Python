# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def contacts(name, surname, year, city, email, phone):
     return ' '.join([name, surname, year, city, email, phone])
print(contacts(surname = 'Иванов', name = 'Иван', year = '1990', city = 'Москва', email = 'ivan_ivanov@mail.ru', telephone = '8-987-654-32-10'))

'''
НЕ СМОГ РЕАЛИЗОВАТЬ КОД, ЧТОБЫ ДАННЫЕ ВВОДИЛ ПОЛЬЗОВАТЕЛЬ...как это правильно сделать?

try:
        name = (input("Введите имя: "))
        surname = (input("Введите фамилию: "))
        year = int(input("Введите год рождения: "))
        city = (input("Введите город проиживания: "))
        email = (input("Введите email: "))
        phone = (input("Введите телефон: "))
    except ValueError:
        return 'Вы некорретно ввели данные!'
    return kwargs
)
'''
