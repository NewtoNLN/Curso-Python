def aprovacao(n):
    return 'aprovado' if n >= 7 else 'reprovado'


if __name__ == '__main__':
    print(aprovacao(10))
    print(aprovacao(8))
    print(aprovacao(6))
    print(aprovacao(0))
    print(aprovacao(7))
