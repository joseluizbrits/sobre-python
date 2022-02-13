# Situação de um carro

class Carro:
    nome = ''
    velMax = 0
    ligado = False
    cor = ''

    def __init__(self, n, v, l, c):
        self.nome = n
        self.velMax = v
        self.ligado = l
        self.cor = c

    def mostrar(self):
        print(f'Carro............: {self.nome}')
        print(f'Velocidade Máxima: {self.velMax}')
        print(f'Cor..............: {self.cor}')
        estado = 'Sim' if c.ligado else 'Não'
        print(f'Ligado...........: {estado}')
        print('-' * 30)


carros = [Carro('Civic', 200, False, 'Azul'),
          Carro('Astra', 120, False, 'Preto'),
          Carro('McLaren', 350, False, 'Roxão')]

print('-' * 30)
for c in carros:
    c.mostrar()
