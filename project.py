# # import time
# # import pyautogui

# # # Open Arduino IDE
# # pyautogui.hotkey('winleft', 's')  # Opens Windows search
# # pyautogui.write('Arduino IDE')
# # pyautogui.press('enter')
# # time.sleep(9)  # Wait for the IDE to open (adjust as needed)

# # # Open Arduino Sketch (Replace 'YourSketch' with your actual sketch name)
# # pyautogui.hotkey('ctrl', 'o')
# # # pyautogui.write('test.ino')
# # pyautogui.press('enter')
# # time.sleep(2)  # Wait for the sketch to open (adjust as needed)

# # # Compile and Upload
# # pyautogui.hotkey('ctrl', 'r')  # Compile sketch
# # time.sleep(5)  # Wait for compilation to finish (adjust as needed)

# # pyautogui.hotkey('ctrl', 'u')  # Upload sketch
# # time.sleep(10)  # Wait for upload to finish (adjust as needed)

# # # Save and Close
# # pyautogui.hotkey('ctrl', 's')  # Save changes
# # # pyautogui.hotkey('alt', 'f4')  # Close Arduino IDE


import time
import pyautogui

# Open Arduino IDE
pyautogui.hotkey('winleft', 's')  # Opens Windows search
pyautogui.write('Arduino IDE')
pyautogui.press('enter')
time.sleep(20)  # Wait for the IDE to open (adjust as needed)

# Open Arduino Sketch (Replace 'YourSketch' with your actual sketch name and path)
# sketch_path = 'Blink.ino'
# pyautogui.hotkey('ctrl', 'o')
# pyautogui.write(sketch_path)
# pyautogui.press('enter')
# time.sleep(10)  # Wait for the sketch to open (adjust as needed)

# Compile and Upload
pyautogui.hotkey('ctrl', 'r')  # Compile sketch
time.sleep(10)  # Wait for compilation to finish (adjust as needed)

pyautogui.hotkey('ctrl', 'u')  # Upload sketch
time.sleep(10)  # Wait for upload to finish (adjust as needed)

# Save and Close
pyautogui.hotkey('ctrl', 's')  # Save changes
pyautogui.hotkey('alt', 'f4')  # Close Arduino IDE




# import time
# import pyautogui

# # Open File Explorer (Windows + E)
# pyautogui.hotkey('winleft', 'e')
# time.sleep(2)  # Wait for File Explorer to open (adjust as needed)

# # Navigate to the Desktop (assuming Desktop is in Quick access)
# pyautogui.write('Desktop')
# pyautogui.press('enter')
# time.sleep(2)  # Wait for the Desktop to open (adjust as needed)

# # Specify the sketch file name
# sketch_file_name = 'Blink.ino'

# # Double-click on the sketch file
# pyautogui.doubleClick(sketch_file_name)
# time.sleep(2)  # Wait for the file to open (adjust as needed)

# # Continue with the rest of your script...


# import time
# import pyautogui

# # Specify the path to the Arduino IDE executable
# # arduino_ide_path = 'C:\\Path\\To\\Arduino\\arduino.exe'C:\Program Files\Arduino IDE

# arduino_ide_path = 'C:\Program Files\Arduino IDE'

# # Open Arduino IDEC:\Program Files\Arduino IDE

# pyautogui.write(arduino_ide_path)
# pyautogui.press('enter')
# time.sleep(5)  # Wait for the IDE to open (adjust as needed)

# # Click on the "File" button in Arduino IDE
# file_button_location = pyautogui.locateOnScreen('file_button.png', confidence=0.8)
# if file_button_location:
#     file_button_center = pyautogui.center(file_button_location)
#     pyautogui.click(file_button_center)
# else:
#     print("File button not found on the screen.")

# # Wait for the menu to appear (adjust as needed)
# time.sleep(2)

# # Select "Open" from the menu
# pyautogui.hotkey('o')

# # Wait for the file dialog to aC:\Program Files\Arduino IDE

# time.sleep(2)

# # Specify the path to the folder you want to open
# folder_path = 'C:\\Users\\vaibh\\OneDrive\\Desktop\\Blink.ino'

# # Type the folder path and press Enter
# pyautogui.write(folder_path)
# pyautogui.press('enter')

# # Continue with the rest of your script...
