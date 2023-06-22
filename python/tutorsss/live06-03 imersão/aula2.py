import yfinance as yf
import pyautogui as pag
import time
import pyperclip as pyper
from fcts2 import tspac, endCode


petr4 = yf.Ticker("PETR4.SA").history("1mo") #1y, 1mo, 1d?
cotacoes = petr4.Close
print(cotacoes)
tspac()

atual = cotacoes[-1]
print(atual)

class Cot():
    def __init__(self, min, max):
        self.min, self.max = min, max 

tspac()
minmax_1month = Cot(cotacoes.min(), cotacoes.max())
print(minmax_1month.max, "foi a maior cotacao do ultimo mes")

#send to email---------------------------------
time.sleep(1)
pag.click(x=70, y=750)
time.sleep(1)
pag.typewrite("opera")
pag.hotkey("enter")
time.sleep(1)
pag.hotkey('ctrl' + 'e')
pag.typewrite('gmail.com')
pag.hotkey('enter')
time.sleep(7)

pag.click(x=116, y=201)
time.sleep(1)
corpoText = f"Cotacoes do ultimo mes da PETR4(Petrobras):\n A atual: {atual};\n A maior: {minmax_1month.max} e a menor: {minmax_1month.max}\n\n By Atila Lima"
emai = "atilalimade@gmail.com"
assun = "pyautogui programmed"
pag.typewrite(emai)
pag.hotkey('enter')
pag.hotkey('tab')
time.sleep(1)
pag.typewrite(assun)
pag.hotkey('tab')
time.sleep(1)
pag.typewrite(corpoText)
time.sleep(2)

pag.click(x=838, y=692)
time.sleep(4)

pag.click(x=1342, y=11)
print('email sended')
endCode()