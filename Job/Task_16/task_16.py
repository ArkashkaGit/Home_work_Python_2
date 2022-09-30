# Задача 16
# Задайте список из n чисел последовательности (1+1/n)^n  
# и выведите на экран их сумму.

n = int(input("Введите число:\n"))

def list_order(number):
    list=[]
    for i in range(1,number+1):
        list.append((1+1/i)**i)
    return list

print(list_order(n))