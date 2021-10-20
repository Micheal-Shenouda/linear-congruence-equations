#!/bin/python3
from Crypto.Util.number import inverse

file = open('data.txt', 'r')
eqn_array = file.readlines()
file.close()

eqn_array = eqn_array[:-1]  #Remove the last line (not equation)

for element in eqn_array:
    element = element.split()
    ##############################################
    #          The form of equation is:          #
    #               ax (mod m) = c               #
    #   element[0] =  a                          #
    #   element[1] = '*'                         #
    #   element[2] =  x                          #
    #   element[3] = 'mod'                       #
    #   element[4] =  m                          #
    #   element[5] = '='                         #
    #   element[6] =  c                          #
    #                Solution is:                #
    #            x = c * a**-1 (mod m)           #
    #          x = c * inverse(a, m) % m         #
    #    where, a**-1 (mod m) = inverse(a, m)    # 
    ##############################################
    x = inverse(int(element[0]), int(element[4])) * int(element[6]) % int(element[4])
    print(chr(x % 256), end='')