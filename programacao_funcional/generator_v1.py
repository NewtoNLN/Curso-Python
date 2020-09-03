def cores_arco_iris():
    yield 'vermelho'
    yield 'amarelo'
    yield 'laranja'
    yield 'verde'
    yield 'azul'
    yield 'violeta'
    yield 'indigo'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))
