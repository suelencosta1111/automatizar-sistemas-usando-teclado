# Como usar botões e atalhos do teclado
import pyautogui
from time import sleep
# Navegar e clicar no campo email
pyautogui.click(2307,97, duration=2)
sleep(1)
# Digitar o email
pyautogui.typewrite("admin@hotmail.com")
sleep(1)
# Apertar enter
pyautogui.press("enter")
sleep(1)
# Digitar minha senha
pyautogui.typewrite("123456789")
sleep(1)
# Apertar enter
pyautogui.press("enter")
sleep(1)
# Apertar enter
pyautogui.press("enter")
