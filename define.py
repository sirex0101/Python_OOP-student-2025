import sys
from time import time
sys.setrecursionlimit(1_000_000)

def perimeter(length, width):
    return 2 * length + 2 * width

def num_to_even(number):
    if number % 2 == 0:
        return number
    else: return number - 1

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def seconds_to_hours(second):
    return second / 60 ** 2

def days_in_month(month_num): #эта фигня не совсем правильно считает
    if month_num == 2:
        return 28
    elif month_num <= 7:
        if month_num % 2 != 0: return 31
        if month_num % 2 == 0: return 30
    else:
        if month_num % 2 != 0: return 30
        if month_num % 2 == 0: return 31

# for i in range(1, 12 + 1):
#     print(days_in_month(i), i)

def factorial(num):
    if num == 1: return 1
    return num * factorial(num - 1)

def average(a, b, c):
    return (a+b+c) / 3

def minmax(a, b, c):
    if a >= b and a <= c: return a
    if b >= a and b <= c: return b
    if c >= b and c <= a: return c

def mode(a, b, c):
    if a == b or a == c: return a
    if b == a or b == c: return b
    if c == b or c == a: return c
    else: return a

def my_sum(num):
    result = 0
    for i in range(num + 1):
        result += i
    return result

def my_sum_rec(num):
    if num == 1: return 1
    return num + my_sum(num - 1)


N = 30_000
start = time()
print(my_sum(N))
stop = time()
print (f"Время: {stop - start}")

start = time()
print(my_sum_rec(N))
stop = time()
print (f"Время: {stop - start}")