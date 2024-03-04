# # import os
# # import time
# # import pyautogui
# # import subprocess
# # import pygetwindow as gw
# # import asyncio
# # import win32gui
# # import win32con

# # # Function to open Arduino IDE
# # def open_arduino_ide():
# #     pyautogui.press('win')  # Press Windows key to open Start menu
# #     time.sleep(4)
# #     pyautogui.typewrite('Desktop')  # Type Arduino IDE in the search bar
# #     time.sleep(4)
# #     pyautogui.press('enter')  # Press Enter to open Arduino IDE
# #     time.sleep(5)

# # # # Function to open .ino file in Arduino IDE
# # # def open_ino_file(file_path):
# # #     pyautogui.hotkey('ctrl', 'o')  # Press Ctrl + O to open file
# # #     time.sleep(10)
# # #     pyautogui.write(file_path)  # Type the file path
# # #     pyautogui.press('enter')  # Press Enter to open the file
# # #     time.sleep(6)


    
# # # # Function to compile and upload .ino file
# # # def compile_and_upload():
# # #     pyautogui.click(x=100, y=100)  # Click to focus on Arduino IDE (adjust coordinates if needed)
# # #     time.sleep(10)
# # #     pyautogui.hotkey('ctrl', 'r')  # Press Ctrl + R to compile
# # #     time.sleep(10)  # Wait for compilation to finish (adjust time if needed)
# # #     pyautogui.hotkey('ctrl', 'u')  # Press Ctrl + U to upload
# # #     time.sleep(10)  # Wait for upload to finish (adjust time if needed)




# # # # Function to close Arduino IDE
# # # async def close_arduino_ide():
# # #     await subprocess.run("TASKKILL /F /IM arduino.exe", shell=True)



# # # Main function
# # def main():
# #     # Replace 'file_path' with the path to your .ino file
# #     file_path = "C:\\Users\\vaibh\\OneDrive\\Desktop\\test\\Blink\\Blink.ino"
    
# #     open_arduino_ide()
# #     # # open_ino_file(file_path)
# #     # compile_and_upload()
# #     # close_arduino_ide()

# # # if __name__ == "__main__":
# # #  asyncio.run(main())



# import os
# import time
# import pyautogui
# import subprocess
# import asyncio
# import pygetwindow as gw

# # Function to open the folder containing .ino file and select the .ino file
# async def open_folder_and_select_ino():
#     # Replace "test.ino" with the name of your .ino file
#     ino_file_name = "test.ino"
    
#     # Replace "C:\\Users\\YourUserName\\Desktop" with the path to your desktop
#     desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

#     # Search for the folder containing the .ino file on the desktop
#     found_folder = False
#     for root, dirs, files in os.walk(desktop_path):
#         if ino_file_name in files:
#             folder_path = root
#             found_folder = True
#             break
    
#     if not found_folder:
#         print("Folder containing .ino file not found on desktop.")
#         return

#     # Open the folder
#     subprocess.Popen(["explorer", folder_path])
#     await asyncio.sleep(13)  # Adjust as needed

#     # Select the .ino file
#     pyautogui.click(500, 500)  # Adjust coordinates as needed
#     await asyncio.sleep(10)  # Adjust as needed

# # Function to open Arduino IDE
# async def open_arduino_ide():
#     subprocess.Popen(["arduino.exe"])
#     await asyncio.sleep(13)  # Adjust as needed

# # Function to compile and upload .ino file
# async def compile_and_upload():
#     await asyncio.sleep(10)  # Adjust as needed
#     pyautogui.click(x=100, y=100)  # Click to focus on Arduino IDE (adjust coordinates if needed)
#     await asyncio.sleep(1)
#     pyautogui.hotkey('ctrl', 'r')  # Press Ctrl + R to compile
#     await asyncio.sleep(10)  # Wait for compilation to finish (adjust time if needed)
#     pyautogui.hotkey('ctrl', 'u')  # Press Ctrl + U to upload
#     await asyncio.sleep(10)  # Wait for upload to finish (adjust time if needed)
    
#     # Get the handle of the new window
#     arduino_window = gw.getWindowsWithTitle("Arduino")[0]  # Adjust the title as needed
    
#     # Maximize the new window
#     arduino_window.maximize()

# # Function to close Arduino IDE
# async def close_arduino_ide():
#     subprocess.run("TASKKILL /F /IM arduino.exe", shell=True)

# # Main function
# async def main():
#     await open_folder_and_select_ino()
#     await open_arduino_ide()
#     await compile_and_upload()
#     await close_arduino_ide()

# if __name__ == "__main__":
#     asyncio.run(main())
import pyautogui
import time

def open_desktop():
    # Press Win key to open Start menu
    pyautogui.press('win')
    time.sleep(5)  # Wait for the Start menu to open

    # Type 'desktop' to search for Desktop folder
    pyautogui.write('manoj', interval=0.1)
    time.sleep(5)  # Wait for search results to appear

    # Press Enter to open the Desktop folder
    pyautogui.press('enter')
    time.sleep(5)  # Wait for the Desktop folder to open

def open_test_folder():
    # Type 'test' to search for the test folder
    pyautogui.write('Blink.ino', interval=0.1)

    time.sleep(5)  # Wait for search results to appear

    # Press Enter to open the test folder
    pyautogui.press('enter')

# Main function
def main():
    open_desktop()
    open_test_folder()

if __name__ == "__main__":
    main()
