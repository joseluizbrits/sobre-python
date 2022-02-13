import pyautogui

print('-' * 50)
print('{:^50}'.format('DELETAR E-MAILS'))
print('-' * 50)
print()

numero_de_emails = int(input('Digite o número de e-mails a serem excluídos -> '))
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.15
pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(1185, 235)
contador = 0
while contador < numero_de_emails:
    pyautogui.leftClick()
    contador += 1
pyautogui.hotkey('alt', 'tab')
pyautogui.alert('Pronto! Código finalizado.')
