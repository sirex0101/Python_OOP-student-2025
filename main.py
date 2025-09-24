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

# Задание 1
user_num = int(input("Введите число: "))
for i in range(1, 9 + 1):
    print(f"{user_num} * {i} = {user_num * i}")

# Задание 2
while True:
    user_input = int(input("Введите значение в рублях: "))
    if user_input == 0:
        break
    print("1. Перевести в Доллары \n"
          "2. Перевести в Юани \n"
          "3. Перевести в Тенге \n"
          "4. Перевести в Бел. Рубль \n"
          "0. Выход")
    user_choice = int(input("Введите выбор: "))
    if user_choice == 0:
        break
    elif user_choice == 1: print(user_input*0.012)
    elif user_choice == 2: print(user_input*0.085)
    elif user_choice == 3: print(user_input*6.48)
    elif user_choice == 4: print(user_input*0.041)

# Задание 3
user_min = int(input("Введите левую границу диапазона: "))
user_max = int(input("Введите правую границу диапазона: "))

while True:
    user_value = int(input("Введите число для поиска: "))
    if user_value >= user_min and user_value <= user_max:
        break
while user_min <= user_max:
    if user_min == user_value:
        print(f"!{user_min}!", end=" ")
    else:
        print(user_min, end=" ")
    user_min += 1
print("\n")

# Задание 4
from random import randint
from time import time
value_randint = randint(1, 500)
user_attempt = 1
print("Добро пожаловать в игру \"угадай число\"\n"
      "Ваша задача - угадать число в диапозоне от 1 до 500\n"
      "0 - выход из игры\n"
      "Время пошло, удачи!")
start_time = time()
while True:
    user_input = int(input(f"Попытка номер {user_attempt}, Введите число: "))
    if user_input == 0: break
    elif user_input > 500 or user_input < 0: 
        print("Вне диапазона, загаданное число от 1 до 500, попытка не засчитывается")
        user_attempt += -1
    elif user_input > value_randint: print("Загаданное число меньше")
    elif user_input < value_randint: print("Загаданное число больше")
    else:
        end_time = time()
        print(f"Абсолютно верно!\n"
              f"число угадано спустя {user_attempt} попыток, это заняло {int(end_time - start_time)} секунд")
        break
    user_attempt += 1
