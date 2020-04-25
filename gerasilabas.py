
consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
vogais = ('a', 'e', 'i', 'o', 'u')

tupla = []

for consoante in consoantes:
    for vogal in vogais:
        silaba = consoante+vogal
        tupla.append(silaba.upper())
        print(silaba.upper())

        silaba = vogal+consoante
        tupla.append(silaba.upper())
        print(silaba.upper())

        if silaba == 'uz':
            print('\nTemos {} silabas' .format(len(tupla)))
            print(tupla)
            exit()


# tu = []
# for vogal in vogais:
#     for vogal1 in vogais:
#         com = vogal+vogal1
#         tu.append(com.upper())
#         print(com.upper())
#
#         if com == 'uu':
#             print('Temos {} combinações possíveis' .format(len(tu)))
#             print(tu)
