def mapear(funcao, lista):
    for elemento in lista:
        print('Passando por aqui')
        yield funcao(elemento)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(list(resultado))
