import pyautogui
pyautogui.alert('O código vai começar! Apenas assista...')
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('winleft', 'up')
pyautogui.write('https://www5.uva.br/PortalAluno/Default.aspx')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write('20191102919')
pyautogui.press('tab')
pyautogui.write('2195992705', interval=0.05)
pyautogui.press('enter')
