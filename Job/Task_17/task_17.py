# Задача 17	
# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

list = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
list_index=[]

with open('file.txt','r') as txt:
    text_str = str()
    for i in txt:
        text_str = i
        for i in text_str:
            if (i == '1' or i =='2' or i =='3' or i =='4' 
                         or i =='5' or i =='6' or i =='7'
                         or i =='8' or i =='9' or i =='0'):
                list_index.append(int(i))

multiplication_number = 1
for i in list_index:
    multiplication_number *= list[i]

print (multiplication_number)

