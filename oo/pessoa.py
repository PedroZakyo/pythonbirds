class Pessoa:

    def __init__(self,nome=None,idade=35):
        self.idade = idade
        self.nome = nome

    def comprimentar(self):
        return 'ola'


if __name__ == '__main__':
    p = Pessoa('lucas' ,25)
    print(p.comprimentar())
    print(p.idade)
    print(p.nome)