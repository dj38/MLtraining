# import d'un module avec un alias
#import math as m

# danger : a n'utiliser que sur les petits codes si je redefinis la fonction tanh son fonctionnement est change
from math import tanh

# essais lies au slides Yield
# generateur = (x*x for x in range(3))
# for i in generateur :
#     print(i)
#
# lst = [x*x for x in range(3)]
# for i in lst :
#     print(i)

def add(i,j=0):
    return i + j

def tanh():
    return "x"

print(add(i = 2, j = 3))

print("Hello World!")

i = 1
print(type(i))

def isPrime(x):
    if x < 2:
        return False
    else:
        # note : range s'arrete a l'argument -1
        for div in range(2, int(x ** 0.5 + 1)):
            if x % div == 0:
                return False
        return True

print(isPrime(6113))
print(isPrime(6114))
l = [2,4,5,-2,0,12]
# min, max, sum, len
print(len(l))
print(sum(l)/len(l))
for val in l:
    print(val)
    # imprime la valeur et non l'index

# les type simples sont manipules par valeur (int, float)
i = 3
j = i
j += 1
print(i,j)

# les types complexes sont tous des pointeurs (exemple sur une liste)
i = [1,2,3]
j = i
j.append(4)
print(i,j)
#copie par valeur /!\ utilise de la ressource
j = list(i)
j.append(5)
print(i,j)
