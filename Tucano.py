import time

import PySimpleGUI as sg
import keyboard
import pyautogui
import win32api
import win32con

minBlueTargetColor = 168
maxBlueTargetColor = 255
minGreenTargetColor = 145
maxGreenTargetColor = 245
minRedTargetColor = 4
maxRedTargetColor = 35


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


layout = [
    [sg.T("")],
    [sg.T("               "), sg.Button('Start', size=(20, 2))],
    [sg.T("")],
    [sg.T('                         Press "Q" to pause.')]
]


window = sg.Window('Toucan V-0.1', layout, size=(350, 150))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    else:
        # code for the TriggerBot:
        while not keyboard.is_pressed('q'):
            pixel_color = pyautogui.pixel(960, 540)
            if (
                    (minBlueTargetColor <= pixel_color[2] <= maxBlueTargetColor)
                    and
                    (minGreenTargetColor <= pixel_color[1] <= maxGreenTargetColor)
                    and
                    (minRedTargetColor <= pixel_color[0] <= maxRedTargetColor)
            ):
                click()
                time.sleep(0.05)

window.close()
