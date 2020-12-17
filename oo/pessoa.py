class Pessoa:

    def __init__(self,*filhos,nome=None,idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)



    def comprimentar(self):
        return 'ola'


if __name__ == '__main__':
    pedro =Pessoa(nome='pedro')
    lucas = Pessoa(pedro,nome='lucas')
    for filho in lucas.filhos:
        print(filho.nome)


    lucas.sobrenome = 'lol'

    print(lucas.sobrenome)

    del lucas.filhos

    print(lucas.__dict__)
    print(pedro.__dict__)
