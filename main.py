# print("print(\"helloworld\")")
# name = input("Введите ваше имя: ")
# #Переменная которая хранит в себе
# age =  int(input("Введите ваш возраст: "))
# #Переменная которая хранит в себе целочисленное число
# water = 4.5
# #Переменная которая хранит в себе дробь
# print(type(age), type(name))
# '''
# Функция type - нужна для для определения
# типа данных наших переменных
# '''
# print("Привет,", name,"тебе", age, "лет")
# print("Я пью ", water,"литра воды")
# print("Ты умрёшь через", 80-age, "лет")
#
# answer = int(input("Реши пример 5*8/10 = "))
# if answer==5*8/10:
#     print("Верно, ответ:", 5*8/10)
# else: print("Неверно")
#
# print("СЕГОДНЯ 5 СЕНТЯБРЯ","Я ИЗМУЧЕННЫЙ ПРИШЕЛ НА ПЕРВУЮ ПАРУ","К 8:15",
#       sep='\t', end=' '
#       )
# #\t - текстовая табуляция(3 пробела)
# #\n - перенос на новую строку
# #sep - отступы между параметрами print
# #end - завершение строки
# print("Желаю \"всем\" продуктивного дня☻")
# #\ - открытие ввода символа
# name=input("Введите имя:")
# s_name=input("Введите фамилию:")
# age=int(input("Введите ваш возраст:"))
# date=int(input("Ввежите ваш год рождения:"))
# print(f"Ваше имя: {name} \n"
#       f"Ваша фамиолия: {s_name} \n"
#       f"Ваш возраст: {age} \n"
#       f"Ваша Дата рождения: {date} \n")
# #Обращение f'' f"" f`` нужно для форматирования
# #текста и вставки переменных в строку
#
# '''
# Арифмитические операции в python
# + - / * ( )
# ** - оператор возведения в степень
# print(2**2) #4
# // - целочисленное деление
# print(6.31 // 3) # 2
# % - деление по остатку
# print(6 % 2) # 0
# Что делать не нужно:
# 1.Делить на 0 нельзя!
# 2.Делить целое число на ноль!
# 3.Находить остаток деления на ноль!
# Функция суммы: sum(1,2,3) #6
# Функция минимума:min(1,2,3) #1
# Функция максимума:max(1,2,3) #3
# '''
#
# #Практика
# '''
# Задание 1
# Пользователь вводит с клавиатуры 3 числа. Необходимо найти сумму чисел,
# Найти произведение чисел, найти разность чисел, найти деление чисел.
# Результат вычислений операций вевести на экран.
# Задание 2
# Пользователье вводит с клавиатуры три числа.
# Первое число - зарплата за месяц,
# Второе число - сумма месячного платежа по кредиту в банке,
# Третье число - задолженность за коммунальные услуги.
# Необходимо вывести на экран сумму,
# которая останется у пользователя после всех выплат.
# Задание 3
# Напишите программу, вычисляющую площадь ромба.
# Задание 4
# Введите на экран надпись To be or not to be на разных строках.
# Задание 5
# Введите на экран надпись "Life is what happens when you're busy making other plans" Jonn Lennon.
# '''
#
# #Задание 1
# a = int(input("Введите первое значение: "))
# b = int(input("Введите второе значение: "))
# c = int(input("Введите третье значение: "))
# print("Сумма чисел:", a+b+c, "Разность чисел:", a-b-c, "Произведение чисел:", a*b*c, "Деление чисел:", a/b/c)
#
# #Задание 2
# salary=int(input("Введите зарплату за месяц: "))
# payment=int(input("Введите сумма месячного платежа по кредиту в банке: "))
# debt=int(input("Введите задолженность за коммунальные услуги: "))
# print("Остаток:", salary-payment-debt)
#
# #Задание 3
# a=int(input("Введите первую диагональ ромба: "))
# b=int(input("Введите вторую диагональ ромба: "))
# print("Площадь ромба равна:",0.5*a*b)
#
# #Задание 4
# print("To be\nor not\nto be")
#
# #Задание 5
# print("\"Life is what happen", "when", "\t\tyou're busy making other plans\"", "\t\t\t\t\t\t\t\t\t\tJonn Lennon.", sep='\n\t\t\t\t')
#
# '''
# Практика 1
# Задание 1
# Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.
# Задание 2
# Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднее
# арифметическое трёх чисел.
# Задание 3
# Пользователь вводит с клавиатуры количество метров.
# В зависимости от выбора пользователя программа переводит
# метры в мили, дюймы или ярды.
# '''
#
# print("========================")
#
# #Задание 1
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# print("Выберите операцию\n1. Сложить\n2. Умножить")
# choice = int(input("Введите выбор (1-2): "))
# while choice!=1 and choice!=2:
#     print("Неверный ввод, попробуйте ещё раз")
#     choice = int(input("Введите выбор (1-2): "))
# print("Результат: ", end="")
# if choice==1: print(a+b+c)
# if choice==2: print(a*b*c)
#
# print("========================")
#
# #Задание 2
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# print("Выберите операцию\n1. Вычислить максимум\n2. Вычислить минимум\n3. Вычислить среднее арифметическое")
# choice = int(input("Введите выбор (1-3): "))
# while choice!=1 and choice!=2 and choice!=3:
#     print("Неверный ввод, попробуйте ещё раз")
#     choice = int(input("Введите выбор (1-3): "))
# print("Результат: ", end="")
# if choice==1: print(max(a,b,c))
# if choice==2: print(min(a,b,c))
# if choice==3: print(sum([a,b,c])/3)
#
# print("========================")
#
# #Задание 3
# length = int(input("Введите длину в метрах: "))
# print("Выберите операцию\n1. Перевести метры в мили\n2. Перевести метры в дюймы\n3. Перевести метры в ярды")
# choice = int(input("Введите выбор (1-3): "))
# while choice!=1 and choice!=2 and choice!=3:
#     print("Неверный ввод, попробуйте ещё раз")
#     choice = int(input("Введите выбор (1-3): "))
# print("Результат: ", end="")
# if choice==1: print(length/1609)
# if choice==2: print(length*39.37)
# if choice==3: print(length*1.094)

# n = int(input("Введите число от 1 до 100: "))
# if n>=1 and n<=100:
#     if n%3==0:
#         print("Fizz", end=" ")
#     if n%5==0:
#         print("Buzz")
#     elif n%5!=0: print(n)
# else: print("\"Сообщение об ошибке\"")

# n = int(input("Введите число: "))
# nn = 0
# for i in range(0, 7 + 1):
#     print(n**nn)
#     nn = nn+1

# x = int(input("Введите стоимость разговора оператора x: "))
# y = int(input("Введите стоимость разговора оператора y: "))
# print("Выберите исходящего оператора\n1. Оператор X\n2. Оператор Y")
# choice_a = int(input("Введите выбор (1-2): "))
# print("Выберите входящего оператора\n1. Оператор X\n2. Оператор Y")
# choice_b = int(input("Введите выбор (1-2): "))
# if choice_a == choice_b:
#     print("Бесплатно")
# elif choice_a==1: print(x)
# elif choice_a==2: print(y)

# a = int(input("Введите уровень продаж первого менеджера: "))
# b = int(input("Введите уровень продаж второго менеджера: "))
# c = int(input("Введите уровень продаж третьего менеджера: "))
# if a > 1000: a_pct = 0.08
# elif a >= 500: a_pct = 0.05
# else: a_pct = 0.03
# if b > 1000: b_pct = 0.08
# elif b >= 500: b_pct = 0.05
# else: b_pct = 0.03
# if c > 1000: c_pct = 0.08
# elif c >= 500: c_pct = 0.05
# else: c_pct = 0.03
# a_salary = 200+a*a_pct
# b_salary = 200+b*b_pct
# c_salary = 200+c*c_pct
# if a > b and a > c:
#     a_salary + 200
#     print("Премия достаётся первому менеджеру!")
# elif b > c and b > a:
#     a_salary + 200
#     print("Премия достаётся второму менеджеру!")
# elif c > a and c > b:
#     a_salary + 200
#     print("Премия достаётся третьему менеджеру!")
# else: print("Премия никому не досталась!")
# print(f"Зарплата первого менеджера: {a_salary}")
# print(f"Зарплата второго менеджера: {b_salary}")
# print(f"Зарплата третьего менеджера: {c_salary}")

# num1 = "" #Первое слагаемое
# num2 = "" #Второе слагаемое
# operation = "" #Знак операции
# letter_num = 0 #Индекс знака операции
# user_str = input("Введите выражение: ")
# #Поиск знака и его индекса
# for i in range(0, len(user_str) ):
#     if user_str[i] in "+-*/":
#         letter_num = i
#         operation = user_str[i]
# #Поиск 1 числа
# for i in range(0, letter_num):
#     num1 += user_str[i]
# num1 = int(num1)
# #Поиск 2 числа
# for i in range(letter_num + 1, len(user_str) ):
#     num2 += user_str[i]
# num2 = int(num2)
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = (num1 / num2)
# print(user_str, "=", result, sep="")
#
# str_reverse = ""
# user_str = input("Введите строку: ")
# for i in range(len(user_str)-1, -1, -1):
#     str_reverse += user_str[i]
# print(str_reverse)
#
# result = 0
# user_str = input("Введите строку: ")
# user_search = input("Введите символ для поиска: ")
# for i in range(0, len(user_str)):
#     if user_str[i] == user_search:
#         result += 1
# print(result)

# # Задание 1
# start_range = int(input("Начало диапазона: "))
# end_range = int(input("Конец диапазона: "))
# for i in range(start_range, end_range + 1):
#     if  i % 7 == 0:
#         print(i, end=" ")
# print("\n")

# # Задание 2
# start_range = int(input("Начало диапазона: "))
# end_range = int(input("Конец диапазона: "))
# num_5 = 0
# for i in range(start_range, end_range + 1):
#     print(i, end=" ")
# print("\n")
# for i in range(end_range, start_range - 1, -1):
#     print(i, end=" ")
# print("\n")
# for i in range(start_range, end_range + 1):
#     if  i % 7 == 0:
#         print(i, end=" ")
# print("\n")
# for i in range(start_range, end_range + 1):
#     if  i % 5 == 0:
#         num_5 += 1
# print(num_5)

# # Задание 3
# start_range = int(input("Начало диапазона: "))
# end_range = int(input("Конец диапазона: "))
# for i in range(start_range, end_range + 1):
#     if i%3==0 and i%5==0:
#         print("Fizz Buzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else: print(i)

# # Задание 1
# user_num = int(input("Введите число: "))
# for i in range(1, 9 + 1):
#     print(f"{user_num} * {i} = {user_num * i}")

# # Задание 2
# while True:
#     user_input = int(input("Введите значение в рублях: "))
#     if user_input == 0:
#         break
#     print("1. Перевести в Доллары \n"
#           "2. Перевести в Юани \n"
#           "3. Перевести в Тенге \n"
#           "4. Перевести в Бел. Рубль \n"
#           "0. Выход")
#     user_choice = int(input("Введите выбор: "))
#     if user_choice == 0:
#         break
#     elif user_choice == 1: print(user_input*0.012)
#     elif user_choice == 2: print(user_input*0.085)
#     elif user_choice == 3: print(user_input*6.48)
#     elif user_choice == 4: print(user_input*0.041)

# # Задание 3
# user_min = int(input("Введите левую границу диапазона: "))
# user_max = int(input("Введите правую границу диапазона: "))
# while True:
#     user_value = int(input("Введите число для поиска: "))
#     if user_value >= user_min and user_value <= user_max:
#         break
# while user_min <= user_max:
#     if user_min == user_value:
#         print(f"!{user_min}!", end=" ")
#     else:
#         print(user_min, end=" ")
#     user_min += 1
# print("\n")

# # Задание 4
# from random import randint
# from time import time
# value_randint = randint(1, 500)
# user_attempt = 1
# print("Добро пожаловать в игру \"угадай число\"\n"
#       "Ваша задача - угадать число в диапозоне от 1 до 500\n"
#       "0 - выход из игры\n"
#       "Время пошло, удачи!")
# start_time = time()
# while True:
#     user_input = int(input(f"Попытка номер {user_attempt}, Введите число: "))
#     if user_input == 0: break
#     elif user_input > 500 or user_input < 1: 
#         print("Вне диапазона, загаданное число от 1 до 500, попытка не засчитывается")
#         user_attempt += -1
#     elif user_input > value_randint: print("Загаданное число меньше")
#     elif user_input < value_randint: print("Загаданное число больше")
#     else:
#         stop_time = time()
#         print(f"Абсолютно верно!\n"
#               f"число угадано спустя {user_attempt} попыток, это заняло {int(end_time - start_time)} секунд")
#         break
#     user_attempt += 1

# list_u = []
# for i in range(10):
#     list_u.append(randint(0,10))
# summ = 0
# for i in list_u:
#     summ += i
# print(f"Список: {list_u}\nСумма элементов: {summ}")

# from random import randint

# # Задание 1
# list_u = [randint(0, 9) for _ in range(10)]
# multiply = 1
# for i in list_u:
#     multiply = multiply * i
# print(f"Список: {list_u} Произведение элементов: {multiply}")

# # Задание 2
# list_u = [randint(0, 9) for _ in range(10)]
# list_min = list_u[0]
# for i in list_u:
#     if list_min > i:
#         list_min = i
# print(f"Список: {list_u} Минимальный элемент: {list_min}")

# # Задание 3
# list_u = [randint(0, 9) for _ in range(10)]
# def count_primes(list_u):
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
#     count_prime = 0
#     for i in list_u:
#         if is_prime(i):
#             count_prime += 1
#     return count_prime
# print(f"Список: {list_u} Количество простых чисел: {count_primes(list_u)}")

# # Задание 4
# list_u = [randint(0, 9) for _ in range(10)]
# del_count = 0
# while True:
#     print(list_u)
#     user_del = input("Удалить число(00 - выход): ")
#     if user_del == "00": break
#     list_u.pop(list_u.index(int(user_del)))
#     del_count += 1
# print(f"Список: {list_u} Кол-во удалённых элементов: {del_count}")

# # Задание 5
# list_a = [randint(0, 9) for _ in range(10)]
# list_b = [randint(0, 9) for _ in range(10)]
# def list_u(list_a, list_b):
#     return list_a + list_b
# print(list_u(list_a, list_b))

# # Задание 6
# list_u = [randint(0, 9) for _ in range(10)]
# print(list_u)
# uu = int(input("Введите степень: "))
# def list_uu(list_u, uu):
#     return([i ** uu for i in list_u])
# print(list_uu(list_u, uu))

# from random import randint
# from time import time

# list_sort_buble = [randint(0, 100) for _ in range(10)]
# print(f"Начальный список: {list_sort_buble}")
# N = len(list_sort_buble)

# start = time()
# for i in range(N):
#     for j in range(N - 1 - i):
#         if list_sort_buble[j] > list_sort_buble[j+1]:
#             list_sort_buble[j], list_sort_buble[j+1] = list_sort_buble[j+1], list_sort_buble[j]
# stop = time()
# print(f"Отсортированный список: {list_sort_buble}\n"
#       f"Сортировка buble заняло: {stop - start} секунд")


# # Задание 1
# N = 20
# list_sort_buble = [randint(-10, 10) for _ in range(N)]
# print(f"Начальный список: {list_sort_buble}")
# start = time()
# for i in range(N//2):
#     for j in range(N//2 - 1 - i):
#         if list_sort_buble[j] > list_sort_buble[j+1]:
#             list_sort_buble[j], list_sort_buble[j+1] = list_sort_buble[j+1], list_sort_buble[j]
# for i in range(N//2):
#     for j in range(N//2, N - 1 - i):
#         if list_sort_buble[j] < list_sort_buble[j+1]:
#             list_sort_buble[j], list_sort_buble[j+1] = list_sort_buble[j+1], list_sort_buble[j]
# stop = time()
# list_sort_buble.insert(10, "!!")
# print(f"Отсортированный список: {list_sort_buble}\n"
#       f"Сортировка buble заняло: {stop - start} секунд")


# # Задание 2
# N = 45
# list_a = [randint(-20, 20) for _ in range(N)]
# print(f"Начальный список: {list_a}")
# list_result = [num for num in list_a if num % 2 == 0]
# list_result += [num for num in list_a if num % 2 != 0]
# for i in range(N//3, N - N//3 + 1, 2):
#     list_result[i] = max(list_result)
#     list_result[i + 1] = min(list_result)
# print(f"Результат: {list_result}")

'''
Сортировка вставками
Основная задача сортировки - создать два сегмента нашего списка:
1 - отсортированный
2 - несортированный
В процессе работы алгоритма, мы каждый раз удалем самый маленький элемент
из несортированного списка и добавляем его в отсортированный список.
==>Алторитм с минимальным кол-вом перестановок.
Сам алгоритм является:
1) нерекурсивным,
2) может быть устойчивым, так и неустойчевым,
3) преобразует входные данные без использования вспомогательных структур
4) имеет сложность O(n2).
'''

# from random import randint

# N = 10
# mylist = [randint(1, 99) for _ in range(N)]
# print(f"Неотсортированный список: {mylist}")
# i = 0 # Первая ячейка
# while i < N - 1: # Пока i меньше последнего элемента
#     m = i # Индекс ячейки с мин значением
#     j = i + 1 # Поиск осуществлется со след ячейки
#     while j < N:
#         if mylist[j] < mylist[m]:
#             m = j # Сохраняет в m номер найденого минимума
#         j += 1
#     mylist[i], mylist[m] = mylist[m], mylist[i]
#     i += 1
# print(f"Отсортированный список: {mylist}")

# # Задание 3
# N = 15
# mylist = [randint(1, 100) for _ in range(N)]
# print(f"Неотсортированный список: {mylist}")
# i = 0
# while i < N - 1:
#     m = i
#     j = i + 1
#     while j < N:
#         if mylist[j] > mylist[m]:
#             m = j
#         j += 1
#     mylist[i], mylist[m] = mylist[m], mylist[i]
#     i += 1
#     print(f"Итерация номер {i}: {mylist}")
# print(f"Отсортированный список: {mylist}")

# # Задание 4
# words = ["apple", "banana", "cherry", "date", "apricot"]
# print(f"Неотсортированный список: {words}")
# N = len(words)
# for i in range(N):
#     key = words[i]
#     j = i - 1
#     while j >= 0 and words[j] > key:
#         words[j + 1] = words[j]
#         j += -1
#     words[j + 1] = key
# print(f"Отсортированный список: {words}")

# # Задание 5
# N = 10
# myarr = [randint(1, 100) for _ in range(N)]
# print(f"Неотсортированный массив: {myarr}")
# K = randint(0, N - 1)
# print(f"Индекс: {K}")
# num_K = myarr.pop(K)
# N += -1
# i = 0
# while i < N - 1:
#     m = i
#     j = i + 1
#     while j < N:
#         if myarr[j] < myarr[m]:
#             m = j
#         j += 1
#         myarr[i], myarr[m] = myarr[m], myarr[i]
#     i += 1
# myarr.insert(K, num_K)
# print(f"Отсортированный массив: {myarr}")

# # Кортежи, множества, словари

# my_list = [1, 2, 3, 4]
# print(my_list, type(my_list)) # class list
# a = (1, 2, 3, 4)
# print(a, type(a)) # class tuple
# dictionary = {"персона": "человек", "марафон": "гонка бегунов", "бежать": "двигаться со скоростью"}
# print(dictionary, type(dictionary)) # class dict
# story_count = {"Сто": 100,
#                "Двести": 200,
#                "Девяносто": 90,
#                "Двенадцать": 100,
#                "Десять": 100,}
# d = {(1, 2, 3):"Кортежи могут быть ключами",
#      1:"Целые тоже",
#      "строки":"тоже"}
# #   Списки не могут
# # int(1) = float(1.0) = True

# # Функции для работы со словарём
# d = {"dict_key":1, "dictionary":2}
# d = dict(short="dict", long="dictionary")
# d = dict([(1,1),(2,2)])
# d = dict.fromkeys(["a","b"], 100)
# key_list = ["marvel", "dc"]
# value_list = ["Spiderman", "Flash"]
# superhero_list = dict(zip(key_list, value_list))
# d = {a: a**2 for a in range(7)}
# # Получение, добаление, обновление, обновление
# story_count["Hello"] = "world"

# # d.clear()
# del d
# '''
#     dict.copy() - копирование словаря
#     dict.get() - получить значение из словаря
#     dict.update() - изменить значение по ключу
#     dict.pop() - удалить последний добавленный элемент
#     dict.setdefault() - поиск по ключу, если элемента нет, то создаёт его
#     dict.keys() - возвращает список ключей
#     dict.values() - возвращает список значений
#     dict.items() - возвращает пару ключ+значение
# Итерация
# '''

# for key in story_count:
#     print(key)

# for value in story_count.values():
#     print(value)

# for key,value in story_count.items():
#     print(key,value)

# # Множества(set)
# a = set()
# a = set("hello") # {"h", "e", "l", "o"}

# #Методы множества
# '''
#     len(a)
#     a.isdisjoint(other) - Проверка обших элементов 2х множества
#     a.issybset(other) - является ли элементы в множестве подмножеством
#     a.issuperset() - аналогично
#     a.union(other) - объединение множества
#     a.intersection(other) - пересечение множества 
#     a.difference(other) - уникальные элементы
#     a.symmetric_difference() - есть в 1, но нет во 2 множестве
#     а.сору() - копирование множества
#     a.update() - изменение элемента
#     a.intersection_update()
#     a.difference_update()
#     a.symmetric_difference()
#     a.add() - добавление элемента
#     a.remove() - удаление злемента, если его нет - будет ошибка
#     a.discard() - удаление элемента, если он есть
#     a.clear() - очистка множества
# '''

# def calculate_score(word, language='ru'):
#     SCORE_RU = {
#         'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'С': 1, 'Т': 1,
#         'Д': 2, 'К': 2, 'М': 2, 'П': 2, 'У': 2, 'Г': 2,
#         'Б': 3, 'Ь': 3, 'Я': 3,
#         'Й': 4, 'Ы': 4,
#         'Ж': 5, 'З': 5, 'Ц': 5, 'Ч': 5,
#         'Ш': 8, 'Э': 8, 'Ю': 8,
#         'Ф': 10, 'Щ': 10, 'Ъ': 10
#     }
#     SCORE_EN = {
#         'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#         'D': 2, 'G': 2,
#         'B': 3, 'C': 3, 'M': 3, 'P': 3,
#         'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#         'K': 5,
#         'J': 8, 'X': 8,
#         'Q': 10, 'Z': 10
#     }

#     if language == 'ru':
#         scores = SCORE_RU
#     elif language == 'en':
#         scores = SCORE_EN
#     else:
#         print("Неверный выбор языка.")
#         return 0

#     total_score = 0
#     for letter in word.upper():
#         total_score += scores.get(letter, 0)
#     return total_score

# if __name__ == "__main__":
#     while True:
#         language_choice = input("Выберите язык ('ru' для русского, 'en' для английского, '0' - выход): ").lower()
#         if language_choice == '0':
#             break
#         if language_choice not in ['ru', 'en']:
#             print("Неверный выбор. Пожалуйста, выберите 'ru' или 'en'.")
#             continue
#         players = {}
#         num_players = int(input("Cколько человек будет играть?:"))
#         for i in range(num_players):
#             name = input(f"Введите имя игрока {i + 1}: ")
#             players[name]= 0
#         print(f"Список игроков: {list(players.keys())}")
#         for round in range(10):
#             print(f"\n--- Раунд {round} ---")
#             for player in list(players.keys()):
#                 print(f"Ходит игрок {player}")
#                 user_word = input("Введите слово: ").strip()
#                 score = calculate_score(user_word, language_choice)
#                 print(f"Слово '{user_word}' приносит {score} очков.\n")
#                 players[player] += score
#         print("Игра закончена! \nTaблица очков:")
#         for player, total_score in players.items():
#                     print(f"{player}: {total_score} очка")
#         break



# backpack ={'Зажигалка':20,
#            'Компас':100,
#            'Фрукты':500,
#            'рубашка':300,
#            'Термос':1000,
#            'Аптечка':200,
#            'Куртка':600,
#            'Биноколь':400,
#            'Удочка':1300,
#            'Салфетки':40,
#            'Спальник':2500,
#            'Изолента':250,
#            'Котел':3000,}
# massa = int(input("Введите допустимый вес рюкзака: "))*1000
# print("Могу взять:")
# for key, value in backpack.items():
#     if value < massa:
#         print(key, value ,end=' ')
# print()
# print("Не Могу взять:")
# for key, value in backpack.items():
#     if value > massa:
#         print(key, value ,end=' ')
# print()


# note_book = {
#     "Маша": {
#         'tel': '+7922123561',
#         'vk': 'vk.com/masha321',
#         'youtube': 'youtube.com/masha321',
#         'telegram': 't.me/masha321'},
#     "Петя": {
#         'tel': '+7923123571',
#         'vk': 'vk.com/petya321',
#         'youtube': 'youtube.com/petya321',
#         'telegram': 't.me/petya321'},
# }
# while True:
#     name = input("Введите имя контакта (0 - выход): ").strip()
#     if name == '0':
#         break
#     contact = note_book.get(name)
#     if contact:
#         print(f"\nДанные для контакта '{name}':")
#         print(f"Телефон: {contact['tel']}")
#         print(f"ВКонтакте: {contact['vk']}")
#         print(f"YouTube: {contact['youtube']}")
#         print(f"Telegram: {contact['telegram']}\n")
#     else:
#         print(f"Контакт '{name}' не найден.\n")


# XY = "XY"
# abcd = "ABCDEFGH"
# num = "12345678"

#         #первая строка
# for i in range(8):
#     if i == 0:
#         print("@", abcd[i], sep=' ', end =' ')
#     elif i == 7:
#         print("", abcd[i], sep=' ', end =' @')
#     else:
#         print("", abcd[i], sep=' ', end =' ')
# print()


# words = [ ]
# for i in range(8):
#     tr_list = []
#     for j in range(8):
#         if j % 2 == 0:
#             tr_list.append(XY[0])
#         else:
#             tr_list.append(XY[1])
#     words.append(tr_list)

# for j in range(8):
#     for i in range(8):
#         if i == 0:
#             print(num[j], words[i][j], sep='  ', end=' ')
#         elif i == 7:
#             print( words[i][j], sep='  ', end=f' {num[7-j]}')
#         else:
#             print(words[i][j], sep=' ', end=' ')
#     print()


# #Последния строка
# for i in range(8):
#     if i == 0:
#         print("@", abcd[i], sep=' ', end =' ')
#     elif i == 7:
#         print("", abcd[i], sep=' ', end =' @')
#     else:
#         print("", abcd[i], sep=' ', end =' ')

# from calcut import menu
# if __name__ == "__main__":
#     menu()

# def quote_print():
#     print('“Don\'t compare yourself with anyone in this world...if you do so, you are insulting\nyourself.”\nBill Gates')

# def even_between(num1, num2):
#     list_even = []
#     for i in range(num1 + 1, num2):
#         if i % 2 == 0:
#             list_even.append(i)
#     return list_even

# def square_print(xy, symbol, fill):
#     symbol += " "
#     for i in range(xy):
#         if fill:
#             print(symbol * xy)
#         else:
#             if i == 0 or i == xy - 1:
#                 print(symbol * xy)
#             else:
#                 print(symbol + "  " * (xy - 2) + symbol)

# Эксеперимент Монте-Карло

from datetime import datetime, timedelta
from random import randint

def getBirthdays(numberOfBirthdays):
    birthdays = [] # Список дней рождения
    for i in range(numberOfBirthdays):
        # Год в нашей имитации роли не играет, лишь бы в объектах дней рождения он был одинаков
        startOfYear = datetime(2000, 1, 1)
        # Случайный день года
        randomNumbersOfDays = timedelta(randint(0, 364))
        birthday = startOfYear + randomNumbersOfDays
        birthdays.append(birthday)
    return birthdays
# Принимает спимок дней рождения. обрабатывает его и возвращает совпадения в датах, уоторые встречаются несколько раз
def getMatch(birthdays):
    if len(list(birthdays)) == len(set(birthdays)):
        return None # Даты не совпадают, выходим из программы
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 : ]):
            if birthdayA == birthdayB:
                return birthdayA # Даты совпали
def main():
    # Кортеж месяцев в году
    MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    print("Добро пожаловать в приложение для симуляции совпадения дат рождения")
    while True:
        print("Сколько симуляций вы хотите сделать?(max=100)")
        response = input()
        if response.isdecimal() and 0 < int(response) <= 100:
            numBDays = int(response)
            break
    print()
    # Генерируем и отображем дни рождения
    birthdays = getBirthdays(numBDays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(",", end=" ")
        month = MONTHS[birthday.month - 1]
        dateText = "{} {}".format(month, birthday.day)
        print(dateText, end="")
    print()
    print()
    print(f"Генерация {numBDays} Случайных симуляций")
    input("Для продолжения введите Enter...")
    print("Запуск 100.000 симуляций")
    simMatch = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, "Запущена симуляция...")
        birthdays = getMatch(birthdays)
        if getMatch(birthdays) != None:
            simMatch += 1
    print("-" * 12)
    print("Было выполнено 100.000 симуляций")
    probability = round(simMatch/100_000 * 100, 2)
    print(f"Процент совпадения {probability}%")
    print("Кол-во дат исследования:", numBDays)
    print("Кол-во циклов симуляции:", simMatch)

if __name__ == "__main__":
    main()