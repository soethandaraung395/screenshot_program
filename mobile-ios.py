# import subprocess
# import pyautogui
# import time
# import shutil
# import os
# from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
# from AppKit import NSWorkspace

# # Path to the directory containing all main.dart files
# main_dart_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/answer'

# # Path to the template Flutter project directory
# template_project_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/flutter_template'

# # Path to the main.dart file in the template project
# template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

# # Path to save the screenshots
# screenshot_save_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/screenshots'

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

# def run_flutter_and_screenshot(main_dart_file, screenshot_path):
#     try:
#         # Copy the main.dart file to the template project
#         shutil.copy(main_dart_file, template_main_dart_path)
#         print(f"Copied {main_dart_file} to {template_main_dart_path}")

#         # Run the Flutter project using the terminal command, specifying Chrome as the target device
#         flutter_process = subprocess.Popen([flutter_executable, 'run', '-d', 'chrome'], cwd=template_project_dir)
#         print("Started Flutter process")

#         # Wait for the app to start (adjust the sleep time if necessary)
#         time.sleep(30)

#         # Find the Chrome window with the specific title
#         window = None
#         for _ in range(10):
#             window = find_chrome_window("Container Example")
#             if window:
#                 print(f"Found Chrome window with title 'Container Example': {window}")
#                 break
#             time.sleep(1)

#         if window is None:
#             raise Exception("Chrome tab with the title 'Container Example' is not found.")

#         # Get the window bounds
#         window_bounds = window['kCGWindowBounds']
#         x, y, width, height = window_bounds['X'], window_bounds['Y'], window_bounds['Width'], window_bounds['Height']

#         # Resize the window to the desired size
#         # subprocess.call(['osascript', '-e', f'tell application "Google Chrome" to set the bounds of window id {window["kCGWindowNumber"]} to {{100, 100, 500, 750}}'])
#         subprocess.call(['osascript', '-e', f'tell application "Google Chrome" to set the bounds of window id {window["kCGWindowNumber"]} to {{100, 100, 1024, 1200}}'])

#         # Wait a bit for the window to be resized and positioned
#         time.sleep(2)

#         # Update the window bounds after resizing
#         window = find_chrome_window("Container Example")
#         if window:
#             window_bounds = window['kCGWindowBounds']
#             x, y, width, height = window_bounds['X'], window_bounds['Y'], window_bounds['Width'], window_bounds['Height']
#             print(f"Updated window bounds: x={x}, y={y}, width={width}, height={height}")

#         # Take a screenshot of the specific window area, excluding the PC wallpaper
#         screenshot = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))

#         # Save the screenshot
#         screenshot.save(screenshot_path)
#         print(f"Screenshot for {main_dart_file} taken and saved to {screenshot_path}.")

#         # Terminate the Flutter process
#         flutter_process.terminate()
#         print("Terminated Flutter process")
#     except Exception as e:
#         print(f"Error: {e}")

# # Get all main.dart files from the specified directory
# main_dart_files = [os.path.join(main_dart_dir, file) for file in os.listdir(main_dart_dir) if file.endswith('_main.dart')]

# for main_dart_file in main_dart_files:
#     # Extract student ID from the filename
#     student_id = os.path.basename(main_dart_file).split('_')[0]

#     # Define the path to save the screenshot
#     screenshot_path = os.path.join(screenshot_save_dir, f'{student_id}.png')

#     # Run the Flutter app with the given main.dart and take a screenshot
#     run_flutter_and_screenshot(main_dart_file, screenshot_path)



# import subprocess
# import pyautogui
# import time
# import shutil
# import os
# from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
# from AppKit import NSWorkspace

# # Path to the directory containing all main.dart files
# main_dart_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/answer/e2'

# # Path to the template Flutter project directory
# template_project_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/flutter_template'

# # Path to the main.dart file in the template project
# template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

# # Path to save the screenshots
# screenshot_save_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/screenshots/e2'

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

# def run_flutter_and_screenshot(main_dart_file, screenshot_path):
#     try:
#         # Copy the main.dart file to the template project
#         shutil.copy(main_dart_file, template_main_dart_path)
#         print(f"Copied {main_dart_file} to {template_main_dart_path}")

#         # Run the Flutter project using the terminal command, specifying Chrome as the target device
#         flutter_process = subprocess.Popen([flutter_executable, 'run', '-d', 'chrome'], cwd=template_project_dir)
#         print("Started Flutter process")

#         # Wait for the app to start (adjust the sleep time if necessary)
#         time.sleep(30)

#         # Find the Chrome window with the specific title
#         window = None
#         for _ in range(10):
#             window = find_chrome_window("Container Example")
#             if window:
#                 print(f"Found Chrome window with title 'Container Example': {window}")
#                 break
#             time.sleep(1)

#         if window is None:
#             raise Exception("Chrome tab with the title 'Container Example' is not found.")

#         # Maximize the window
#         subprocess.call(['osascript', '-e', f'tell application "Google Chrome" to set bounds of (first window whose name contains "Container Example") to {{0, 22, 1440, 900}}'])

#         # Wait a bit for the window to be resized and positioned
#         time.sleep(2)

#         # Update the window bounds after resizing
#         window = find_chrome_window("Container Example")
#         if window:
#             window_bounds = window['kCGWindowBounds']
#             x, y, width, height = window_bounds['X'], window_bounds['Y'], window_bounds['Width'], window_bounds['Height']
#             print(f"Updated window bounds: x={x}, y={y}, width={width}, height={height}")

#         # Take a screenshot of the specific window area
#         screenshot = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))

#         # Save the screenshot
#         screenshot.save(screenshot_path)
#         print(f"Screenshot for {main_dart_file} taken and saved to {screenshot_path}.")

#         # Terminate the Flutter process
#         flutter_process.terminate()
#         print("Terminated Flutter process")
#     except Exception as e:
#         print(f"Error: {e}")

# # Get all main.dart files from the specified directory
# main_dart_files = [os.path.join(main_dart_dir, file) for file in os.listdir(main_dart_dir) if file.endswith('_main.dart')]

# for main_dart_file in main_dart_files:
#     # Extract student ID from the filename
#     student_id = os.path.basename(main_dart_file).split('_')[0]

#     # Define the path to save the screenshot
#     # screenshot_path = os.path.join(screenshot_save_dir, f'{student_id}.png')
#     screenshot_path = os.path.join(screenshot_save_dir, f'{student_id}_ss.png')

#     # Run the Flutter app with the given main.dart and take a screenshot
#     run_flutter_and_screenshot(main_dart_file, screenshot_path)


import subprocess
import pyautogui
import time
import shutil
import os
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from AppKit import NSWorkspace

# Path to the directory containing all main.dart files
main_dart_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/answer/e4'

# Path to the template Flutter project directory
template_project_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/flutter_template'

# Path to the main.dart file in the template project
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

# Path to save the screenshots
screenshot_save_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/screenshots/e4'

# Full path to the Flutter executable
flutter_executable = '/Users/soethandara/Desktop/Flutter/flutter/bin/flutter'  # Update this path

# Ensure the screenshot save directory exists
os.makedirs(screenshot_save_dir, exist_ok=True)

def find_chrome_window(title):
    options = kCGWindowListOptionOnScreenOnly
    window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    for window in window_list:
        window_title = window.get('kCGWindowName', '')
        if title in window_title:
            return window
    return None

def run_flutter_and_screenshot(main_dart_file, screenshot_path):
    try:
        # Copy the main.dart file to the template project
        shutil.copy(main_dart_file, template_main_dart_path)
        print(f"Copied {main_dart_file} to {template_main_dart_path}")

        # Run the Flutter project using the terminal command, specifying Chrome as the target device
        flutter_process = subprocess.Popen([flutter_executable, 'run', '-d', 'chrome'], cwd=template_project_dir)
        print("Started Flutter process")

        # Wait for the app to start (adjust the sleep time if necessary)
        time.sleep(30)

        # Find the Chrome window with the specific title
        window = None
        for _ in range(10):
            window = find_chrome_window("localhost")
            if window:
                print(f"Found Chrome window with title 'localhost': {window}")
                break
            time.sleep(1)

        if window is None:
            raise Exception("Chrome tab with the title 'localhost' is not found.")

        # Maximize the window
        subprocess.call(['osascript', '-e', f'tell application "Google Chrome" to set bounds of (first window whose name contains "AlertDialog Example") to {{0, 22, 1440, 900}}'])

        # Wait a bit for the window to be resized and positioned
        time.sleep(2)

        # Update the window bounds after resizing
        window = find_chrome_window("localhost")
        if window:
            window_bounds = window['kCGWindowBounds']
            x, y, width, height = window_bounds['X'], window_bounds['Y'], window_bounds['Width'], window_bounds['Height']
            print(f"Updated window bounds: x={x}, y={y}, width={width}, height={height}")

        # Take a screenshot of the specific window area
        screenshot = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))

        # Save the screenshot
        screenshot.save(screenshot_path)
        print(f"Screenshot for {main_dart_file} taken and saved to {screenshot_path}.")

        # Terminate the Flutter process
        flutter_process.terminate()
        print("Terminated Flutter process")
    except Exception as e:
        print(f"Error: {e}")

# Get all main.dart files from the specified directory
main_dart_files = [os.path.join(main_dart_dir, file) for file in os.listdir(main_dart_dir) if file.endswith('_main.dart')]

for main_dart_file in main_dart_files:
    # Extract student ID from the filename
    student_id = os.path.basename(main_dart_file).split('_')[0]

    # Define the path to save the screenshot
    # screenshot_path = os.path.join(screenshot_save_dir, f'{student_id}.png')
    screenshot_path = os.path.join(screenshot_save_dir, f'{student_id}_ss.png')

    # Run the Flutter app with the given main.dart and take a screenshot
    run_flutter_and_screenshot(main_dart_file, screenshot_path)
