#Циклы
# n = 1
# for i in range(0,100000):
#     print(n, end=" ")
#     n = n+1
# print()

# while True:
#     user_input = int(input("Введите значение в рублях: "))
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

# user_min = int(input("Введите левую границу диапазона: "))
# user_max = int(input("Введите правую границу диапазона: "))
# user_value = int(input("Введите число для поиска: "))
# while user_min < user_max:
#     if user_min == user_value:
#         print(f" !{user_min}!", end=" ")
#     else:
#         print(user_value, end=" ")
#     user_min + 1

from random import randint
value_randint = randint(1, 500)
user_attempt = 0
print(value_randint)
while True:
    user_input = int(input("Введите число: "))
    if user_input == 0: break
    elif user_input > value_randint: print("Загаданное число меньше"); user_attempt += 1
    elif user_input < value_randint: print("Загаданное число больше"); user_attempt += 1
    else:
        print("Абсолютно верно!\n"
               "число угадано спустя", user_attempt, "попыток")

deposit = int(input("Введите начальный взнос: "))
annual_pct = int(input("Введите процент годовых: "))
years = int(input("Введите срок в годах: "))
while years > 0:
    deposit = deposit*(1 + annual_pct/100)
    years += -1
print(deposit)