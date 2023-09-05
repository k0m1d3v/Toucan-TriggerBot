# Toucan TriggerBot
**Toucan is a TriggerBot created for help the players in their AimLab routine**

# Requirements:
*For install all the necessaries dependencies use this command*
``` 
$ pip install PySimpleGUI, keyboard, pyautogui, win32api, win32con
```

# Pre-Setup:
**Here's a couple step to follow for a correct pre-setup of the software:**
- Find the color you want to shoot at, in the RGB format, (you can use the [PixelFinder Script](PixelFinder.py)).
- Insert the value into the following lines of code:
``` 
BlueValue = ...         #Here goes your blue value
GreenValue = ...        #Here goes your green value
RedValue = ...          #Here goes your red value
```
***Note: for the default configuration program is set to the cyan color***

# Game-Setup:
**Here's a couple step to follow for a correct setup of the ambient:**
- Set your target color to cyan (optional).
- Remove the shadow or other things that can change the target color from the settings.
- [**_Important_**] Remove your CrossHair or use one that don't cover the central pixel of your screen.

# PixelFinder Uses:
**The PixelFinder tool can be used to find the RGB value of the pixel your pointing at, here's how to use it:**
- Run the script after installing all the dependencies
- Press on the start button and point to your target with the cursor
- Press "q" for confirm the pixel 
- The result will be displayed under the start button
