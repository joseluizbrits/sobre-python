class NPC:  # Base, Pai, Super
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print(f'Nome...: {self.nome}')
        print(f'Time...: {self.time}')
        print(f'Força..: {self.forca}')
        print(f'Munição: {self.municao}')
        print(f'Vivo...: {"Sim" if self.vivo else "Não"}')
        print(f'Energia: {self.energia}')
        print('-' * 30)


class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)


class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)


class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)


players = [
    Guarda('Olho Vivo', 'Caveira Negra'),
    Soldado('Bala na Agulha', 'Caveira Negra'),
    Elite('Ninja', 'Caveira Negra'),
    Guarda('Super Atento', 'Combate Brutal'),
    Soldado('Tiro Certo', 'Combate Brutal'),
    Elite('Muito Perigoso', 'Combate Brutal')
]

print('-' * 30)
for p in players:
    p.info()
