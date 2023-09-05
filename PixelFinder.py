import time

import PySimpleGUI as sg
import keyboard
import pyautogui

layout = [
    [sg.T("PixelFinder V-0.1")],
    [sg.T("               "), sg.Button('Start', size=(20, 2))],
    [sg.T("", key='OUTPUT')],
    [sg.T('                    Press "Q" to pick the color.')]
]

window = sg.Window('PixelFinder V-0,1', layout, size=(350, 150))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    else:
        # code for the TriggerBot:
        while not keyboard.is_pressed('q'):
            x, y = pyautogui.position()
            r, g, b = pyautogui.pixel(x, y)
            printedInfo = r, g, b
            time.sleep(0.1)
            window['OUTPUT'].update(value=printedInfo)

window.close()
