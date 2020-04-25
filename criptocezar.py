
# Linha que pede uma entrada do tipo string #
entr = input(str('Entre algo para criptografar: '))

# Converte a string de entrada em uma lista #
entr2 = list(str(entr))

# Lista previamente criada, vazia #
ll = []

# Loop que pega cada letrinha daquela em entr2 e converte para decimal #
for i in entr2:

  # Mesma explicação do comentário acima, mas aqui soma mais um, assim deslocando a letra uma casa a frente # 
  ii = ord(i) + 1

  # Se o decimal convertido e somado for igual a 91 que fica uma casa depois de 'Z' ou 123, uma casa depois de 'z', pega o valor e tira 26, que aí fica 'a' ou 'A' #
  if (ii == 91) or (ii == 123):

    ll += [(ii - 26)]

  # Se não, prossegue normalmente, adicionando mais um decimal a lista #
  else:

    ll += [(ii)]

# Variável que converte e junta todos os itens da lista que criamos vazia e depois com o for "povoamos" #
junt = ''.join(map(chr,ll))

# Aqui mostra todo o trabalho da galera anterior #
print ('\nCriptografia:', junt)

# Opcionais, e com certeza irrelevantes #

print ('\nObrigado por usar esse sistema de criptografia, Cezar agradece ^-^ ')


