# Exemplo de tela simples
import PySimpleGUI as sg

class Tela:
    def __init__(self):
        sg.change_look_and_feel('BluePurple')
        # Layout
        layout = [
            [sg.Text('Nome'), sg.Input(key='nome')],
            [sg.Text('Idade '), sg.Input(key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0, 100), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(50, 10))]
        ]
        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo {aceita_yahoo}')
            print(f'aceita cartão: {aceita_cartao}')
            print(f'não aceita cartão: {nao_aceita_cartao}')


tela = Tela()
tela.Iniciar()
