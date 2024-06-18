# import subprocess
# import pyautogui
# import time
# import shutil
# import os
# from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

# # Path to the directory containing all main.dart files
# main_dart_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/test_answer/'

# # Path to the template Flutter project directory
# template_project_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/flutter_template'

# # Path to the main.dart file in the template project
# template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

# # Path to save the screenshots
# screenshot_save_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/test_ss/'

# # Full path to the Flutter executable
# flutter_executable = '/Users/soethandara/Desktop/Flutter/flutter/bin/flutter'  # Update this path

# # Ensure the screenshot save directory exists
# os.makedirs(screenshot_save_dir, exist_ok=True)

# def find_chrome_window(title):
#     options = kCGWindowListOptionOnScreenOnly
#     window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
#     for window in window_list:
#         window_title = window.get('kCGWindowName', '')
#         if title in window_title:
#             return window
#     return None

# def run_flutter_and_screenshot(main_dart_file, screenshot_base_path):
#     try:
#         # Copy the main.dart file to the template project
#         shutil.copy(main_dart_file, template_main_dart_path)
#         print(f"Copied {main_dart_file} to {template_main_dart_path}")

#         # Run the Flutter project using the terminal command, specifying Chrome as the target device
#         flutter_process = subprocess.Popen([flutter_executable, 'run', '-d', 'chrome'], cwd=template_project_dir)
#         print("Started Flutter process")

#         # Wait for the app to start
#         time.sleep(30)

#         # Find the Chrome window with the specific title
#         window = None
#         for _ in range(10):
#             window = find_chrome_window("Exercise 4")
#             if window:
#                 print(f"Found Chrome window with title 'Exercise 4': {window}")
#                 break
#             time.sleep(1)

#         if window is None:
#             raise Exception("Chrome tab with the title 'Exercise 4' is not found.")

#         # Maximize the window
#         subprocess.call(['osascript', '-e', f'tell application "Google Chrome" to set bounds of (first window whose name contains "Exercise 4") to {{0, 22, 1440, 900}}'])
#         time.sleep(2)

#         # Update the window bounds after resizing
#         window = find_chrome_window("Exercise 4")
#         if window:
#             window_bounds = window['kCGWindowBounds']
#             x, y, width, height = window_bounds['X'], window_bounds['Y'], window_bounds['Width'], window_bounds['Height']
#             print(f"Updated window bounds: x={x}, y={y}, width={width}, height={height}")

#             # Take initial screenshot
#             screenshot1 = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))
#             screenshot1.save(f"{screenshot_base_path}_1.png")
#             print(f"Screenshot 1 taken and saved to {screenshot_base_path}_1.png")

#             # Simulate user actions and take additional screenshots
#             # Example: click a button to change the UI
#             pyautogui.click(x + button_x_offset, y + button_y_offset)
#             time.sleep(5)  # Wait for the UI to update
#             screenshot2 = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))
#             screenshot2.save(f"{screenshot_base_path}_2.png")
#             print(f"Screenshot 2 taken and saved to {screenshot_base_path}_2.png")

#             # More actions and screenshots as needed
#             # pyautogui.click(...)  # Another action
#             # time.sleep(5)
#             # screenshot3 = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))
#             # screenshot3.save(f"{screenshot_base_path}_3.png")
#             # print(f"Screenshot 3 taken and saved to {screenshot_base_path}_3.png")

#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#         if flutter_process.poll() is None:
#             flutter_process.terminate()
#             print("Terminated Flutter process")

# # Get all main.dart files from the specified directory
# main_dart_files = [os.path.join(main_dart_dir, file) for file in os.listdir(main_dart_dir) if file.endswith('_main.dart')]

# for main_dart_file in main_dart_files:
#     student_id = os.path.basename(main_dart_file).split('_')[0]
#     screenshot_base_path = os.path.join(screenshot_save_dir, f'{student_id}_ss')

#     run_flutter_and_screenshot(main_dart_file, screenshot_base_path)


import subprocess
import pyautogui
import time
import shutil
import os
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

# Path to the directory containing all main.dart files
main_dart_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/test_answer/'

# Path to the template Flutter project directory
template_project_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/flutter_template'

# Path to the main.dart file in the template project
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

# Path to save the screenshots
screenshot_save_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/test_ss/'

# Full path to the Flutter executable
flutter_executable = '/Users/soethandara/Desktop/Flutter/flutter/bin/flutter'  # Update this path

# Ensure the screenshot save directory exists
os.makedirs(screenshot_save_dir, exist_ok=True)

def find_chrome_window(title):
    options = kCGWindowListOptionOnScreenOnly
    window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    for window in window_list:
        window_title = window.get('kCGWindowName', '')
        print(f"Found window: {window_title}")  # Print all found window titles for debugging
        if title.lower() in window_title.lower():  # Case-insensitive match
            return window
    return None

def run_flutter_and_screenshot(main_dart_file, screenshot_base_path):
    try:
        # Copy the main.dart file to the template project
        shutil.copy(main_dart_file, template_main_dart_path)
        print(f"Copied {main_dart_file} to {template_main_dart_path}")

        # Run the Flutter project using the terminal command, specifying Chrome as the target device
        flutter_process = subprocess.Popen([flutter_executable, 'run', '-d', 'chrome'], cwd=template_project_dir)
        print("Started Flutter process")

        # Wait for the app to start
        time.sleep(40)  # Increase wait time to ensure app is fully loaded

        # Find the Chrome window with the specific title
        window = None
        for _ in range(15):  # Increase the number of attempts
            window = find_chrome_window("localhost")
            if window:
                print(f"Found Chrome window with title 'Exercise 3': {window}")
                break
            time.sleep(2)  # Increase the interval between attempts

        if window is None:
            raise Exception("Chrome tab with the title 'Exercise 4' is not found.")

        # Maximize the window
        subprocess.call(['osascript', '-e', f'tell application "Google Chrome" to set bounds of (first window whose name contains "Exercise 4") to {{0, 22, 1440, 900}}'])
        time.sleep(2)

        # Update the window bounds after resizing
        window = find_chrome_window("localhost")
        if window:
            window_bounds = window['kCGWindowBounds']
            x, y, width, height = window_bounds['X'], window_bounds['Y'], window_bounds['Width'], window_bounds['Height']
            print(f"Updated window bounds: x={x}, y={y}, width={width}, height={height}")

            # Define button offsets (example values)
            button_x_offset = 100  # Update with the actual X offset of the button
            button_y_offset = 200  # Update with the actual Y offset of the button

            # Take initial screenshot
            screenshot1 = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))
            screenshot1.save(f"{screenshot_base_path}_1.png")
            print(f"Screenshot 1 taken and saved to {screenshot_base_path}_1.png")

            # Simulate user actions and take additional screenshots
            # Example: click a button to change the UI
            pyautogui.click(x + button_x_offset, y + button_y_offset)
            time.sleep(5)  # Wait for the UI to update
            screenshot2 = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))
            screenshot2.save(f"{screenshot_base_path}_2.png")
            print(f"Screenshot 2 taken and saved to {screenshot_base_path}_2.png")

            # More actions and screenshots as needed
            # pyautogui.click(...)  # Another action
            # time.sleep(5)
            # screenshot3 = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))
            # screenshot3.save(f"{screenshot_base_path}_3.png")
            # print(f"Screenshot 3 taken and saved to {screenshot_base_path}_3.png")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if flutter_process.poll() is None:
            flutter_process.terminate()
            print("Terminated Flutter process")

# Get all main.dart files from the specified directory
main_dart_files = [os.path.join(main_dart_dir, file) for file in os.listdir(main_dart_dir) if file.endswith('_main.dart')]

for main_dart_file in main_dart_files:
    student_id = os.path.basename(main_dart_file).split('_')[0]
    screenshot_base_path = os.path.join(screenshot_save_dir, f'{student_id}_ss')

    run_flutter_and_screenshot(main_dart_file, screenshot_base_path)
