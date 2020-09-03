class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Nearderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Nearderthalensis', 'Sapiens')
        return ('Australopiteco', ) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    grokn = Neanderthal('Grokn')
    print(
        f'Evolucao (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolucao (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens Evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal Evoluido? {Neanderthal.is_evoluido()}')
