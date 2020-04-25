def msg_and_key():
    msg = input("Insira mensagem: ").upper()
    key = input("Insira chave: ").upper()
    # variavel para armazenar a chave mapeada
    key_map = ""
    j=0
    for i in range(len(msg)):
        if ord(msg[i]) == 32:
            # ignorando o espaco
            key_map += " "
        else:
            if j < len(key):
                key_map += key[j]
                j += 1
            else:
                j = 0
                key_map += key[j]
                j += 1
    # print (mapa_chave)
    return msg, key_map
def create_vigenere_table():
    table = []
    for i in range(26):
        table.append([])
    for row in range(26):
        for column in range(26):
            if (row + 65) + column > 90:
                # voltando para A depois de Z
                # apos a primeira linha, cada letra sera deslocada para a esquerda uma posição em comparação à linha acima dela
                table[row].append(chr((row+65) + column - 26))
            else:
                # apos a primeira linha, cada letra sera deslocada para a esquerda uma posição em comparação à linha acima dela
                table[row].append(chr((row+65)+column))
    # impressão da mesa
     # para linha na tabela:
     # para coluna na linha:
      # print (coluna, final = "")
      # print (fim = "\ n")
    return table
def cipher_encryption(message, mapped_key):
    table = create_vigenere_table()
    encrypted_text = ""
    for i in range(len(message)):
        if message[i] == chr(32):
            # ignorando espaço
            encrypted_text += " "
        else:
            # obtendo elemento no índice específico da tabela
            row = ord(message[i])-65
            column = ord(mapped_key[i]) - 65
            encrypted_text += table[row][column]
    print("Mensagem criptografada: {}".format(encrypted_text))
def itr_count(mapped_key, message):
    counter = 0
    result = ""
    # alfabetos iniciais a partir da letra-chave _ mapeada e terminando todas as 26 letras a partir dela (depois de z passamos para a)
    for i in range(26):
        if mapped_key + i > 90:
            result += chr(mapped_key+(i-26))
        else:
            result += chr(mapped_key+i)
    # contando o número de iterações necessárias da letra chave mapeada para a letra do texto cifrado
    for i in range(len(result)):
        if result[i] == chr(message):
            break
        else:
            counter += 1
    return counter
def cipher_decryption(message, mapped_key):
    table = create_vigenere_table()
    decrypted_text = ""
    for i in range(len(message)):
        if message[i] == chr(32):
            # ignorando espaço
            decrypted_text += " "
        else:
            #adicionando número de iterações, leva para chegar de carta-chave mapeada para letra cifrada em 65
            #fazendo isso, temos cabeçalho de coluna de letra de texto cifrada, que passa a ser letra descriptografada
            decrypted_text += chr(65 + itr_count(ord(mapped_key[i]), ord(message[i])))
    print("Mensagem descriptografada: {}".format(decrypted_text))
def main():
    print("Chave e Mensagem só podem ser alfabéticas")
    choice = int(input("1. Criptografia \n2. Decodificação\nEscolha(1,2): "))
    if choice == 1:
        print("---Criptografia---")
        message, mapped_key = msg_and_key()
        cipher_encryption(message, mapped_key)
    elif choice == 2:
        print("---Descriptografia---")
        message, mapped_key = msg_and_key()
        cipher_decryption(message, mapped_key)
    else:
        print("Escolha errada")
if __name__ == "__main__":
    main()