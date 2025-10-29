def calcut(num1, num2, znak):
    def summ():
        return num1 + num2
    def deff():
        return num1 - num2
    def diff(): 
        if num2 == 0:
            return 0
        else: 
            return num1 / num2
    def multi():
        return num1 * num2
    def prinf():
        print(f"{num1} {znak} {num2} = {result}")
    if znak == 1:
        znak = "+"
        result = summ()
    elif znak == 2:
        znak = "-"
        result = deff()
    elif znak == 3: 
        znak = "/"
        result = diff()
    elif znak == 4:
        znak = "*"
        result = multi()
    prinf()

def menu():
    while True:
        print("Калькулятор")
        a = int(input("Введите 1 переменную: "))
        b = int(input("Введите 2 переменную: "))
        print("Выберите операцию:\n"
        "1.Сумма\n"
        "2.Разность\n"
        "3.Деление\n"
        "4.Умножение\n" \
        "0.Выход")
        answer = int(input())
        if answer == 0:
            break
        calcut(a, b, answer)