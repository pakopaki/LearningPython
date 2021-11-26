# Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def seven_check(numero):

    numero = numero%7

    if(numero == 0):
        #print("É divisivel por 7")

        return True
    else:
        #print("Não é divisivel por 7")

        return False

def five_check(numero):
    
    if(numero%5 == 0):
        #print("É Multiplo de 5")

        return True
    else:
        #print("Não é Multiplo de 5")

        return False

numero = range(2000,3201)
lista = []

for n in numero:

    if(seven_check(n) == True and five_check(n) == True):
        lista.append(n)   

print(lista)

# Solution:
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))

# print ','.join(l)