import random

simbols = "@!#$%&*()_+}{`^?;:>/-+.,'"
numbers = "0123456789"
lower = "abcdefghijklmnopqrstuwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

all = list(simbols+numbers+lower+upper)


def build(l):

    senha = ''
    v = 0
    while l:

        v += 1
        if v <= l:
            s = random.choice(all)
            if v >= 2 and s in senha:
                v = v
            else:
                senha += s
        else:
            break
    return senha


def main():
    l = input('Digite o tamanho de senha que deseja: ')
    # t = int(input('\nDigite o número de senhas que deseja criar: '))
    print('Senha:', build(int(l)))


if __name__ == '__main__':
    main()
