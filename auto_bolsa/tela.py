
import PySimpleGUI as sg
from buca_web import busca

fc = [
    [sg.Text('Cosultor de bolsa')],
    [sg.InputText('seu ativo')],
    [sg.Button('Buscar'), sg.Button('Sair')]
]
tl = sg.Window('Mercado de Açoes', fc)
while True:
    ev, vl = tl.Read()
    if ev == sg.WINDOW_CLOSED:
        break
    if ev == 'Buscar':
        busca(vl[0])

    if ev == "Sair":
        break

