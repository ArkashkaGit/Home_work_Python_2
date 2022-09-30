# Задача 14	
# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = int(input("Введите целое число:\n"))
# сумма цыфр цулого числа
def summa (number):
    sum = 0
    while number!=0:
        b = number % 10
        sum += b
        number //= 10
    return sum

num_2 = input("Введите целое или дробное число:\n")
# сумма цифр целого или дробного числа
def summa_2(number):
    number = str(number)
    list_number=[]
    for i in number:
        if i != ".":
            list_number.append(int(i))
    summa = 0
    for i in list_number:
        summa += i
    return summa

print(summa(num))
print(summa_2(num_2))