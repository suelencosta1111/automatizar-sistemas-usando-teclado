# # Como usar botões e atalhos do teclado
import pyautogui

# Como usar combinações de teclas
pyautogui.click(2330,94, duration=2)
# Simular "segurar uma tecla"
pyautogui.keyDown("command")
pyautogui.keyDown("a")
pyautogui.keyUp("command")
pyautogui.keyUp("a")

# Como agilizar o processo acima:
pyautogui.click(2330,94, duration=2)
# Simular "segurar uma tecla"
pyautogui.hotkey("command", "a")

# Selecionar o e-mail e simular "segurar uma tecla"
pyautogui.click(2330,94, duration=2)
pyautogui.hotkey("command", "a")
# Copiar
pyautogui.hotkey("command", "c")
# Movimentar para outro campo
pyautogui.click(2273,277, duration=2)
# Colar
pyautogui.hotkey("command", "v")