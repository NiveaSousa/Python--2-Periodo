def reverter(num):
    reversed_num = 0
    while num != 0:  
        digit = num % 10  #O que sobra
        reversed_num = reversed_num * 10 + digit #Joga uma casa para frente
        num //= 10 #Diminui uma casa decimal no numero inicial
    return(reversed_num)

num = int(input('Digite'))
print(reverter(num))