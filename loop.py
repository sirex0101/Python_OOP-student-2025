#Циклы
# n = 1
# for i in range(0,100000):
#     print(n, end=" ")
#     n = n+1
# print()

deposit = int(input("Введите начальный взнос: "))
annual_pct = int(input("Введите процент годовых: "))
years = int(input("Введите срок в годах: "))
while years > 0:
    deposit = deposit*(1 + annual_pct/100)
    years += -1
print(deposit)