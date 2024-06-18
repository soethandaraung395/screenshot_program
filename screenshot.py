# import subprocess
# import pyautogui
# import time
# import shutil
# import os

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

# def run_flutter_and_screenshot(main_dart_file, screenshot_path):
#     # Copy the main.dart file to the template project
#     shutil.copy(main_dart_file, template_main_dart_path)

#     # Run the Flutter app using the terminal command
#     process = subprocess.Popen([flutter_executable, 'run'], cwd=template_project_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     # Wait for the app to start (adjust the sleep time if necessary)
#     time.sleep(60)

#     # Take a screenshot of the output UI
#     screenshot = pyautogui.screenshot()

#     # Save the screenshot
#     screenshot.save(screenshot_path)

#     # Terminate the Flutter run process
#     process.terminate()

#     # Give some time to ensure the process is terminated
#     time.sleep(5)

#     print(f"Screenshot for {main_dart_file} taken and saved to {screenshot_path}.")

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

# def run_flutter_and_screenshot(main_dart_file, screenshot_path):
#     try:
#         # Copy the main.dart file to the template project
#         shutil.copy(main_dart_file, template_main_dart_path)

#         # Open VS Code with the specified project directory
#         subprocess.Popen(['code', template_project_dir])

#         # Wait for VS Code to open (you may need to adjust the sleep duration)
#         time.sleep(5)

#         # Run the Flutter project using the terminal command
#         subprocess.Popen([flutter_executable, 'run'], cwd=template_project_dir)

#         # Wait for the app to start (adjust the sleep time if necessary)
#         time.sleep(20)

#         # Take a screenshot of the output UI
#         screenshot = pyautogui.screenshot()

#         # Save the screenshot
#         screenshot.save(screenshot_path)

#         print(f"Screenshot for {main_dart_file} taken and saved to {screenshot_path}.")
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


import subprocess
import pyautogui
import time
import shutil
import os

# Path to the directory containing all main.dart files
main_dart_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/answer'

# Path to the template Flutter project directory
template_project_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/flutter_template'

# Path to the main.dart file in the template project
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

# Path to save the screenshots
screenshot_save_dir = '/Users/soethandara/Desktop/FlutterClass2024_Answer_Analysis/screenshot_program/screenshots'

# Full path to the VS Code executable on macOS
vscode_executable = '/Users/soethandara/Downloads/Visual Studio Code.app/Contents/Resources/app/bin/code'  # For macOS

# Full path to the Flutter executable
flutter_executable = '/Users/soethandara/Desktop/Flutter/flutter/bin/flutter'  # Update this path

# Ensure the screenshot save directory exists
os.makedirs(screenshot_save_dir, exist_ok=True)

def run_flutter_and_screenshot(main_dart_file, screenshot_path):
    try:
        # Copy the main.dart file to the template project
        shutil.copy(main_dart_file, template_main_dart_path)

        # Open VS Code with the specified project directory
        subprocess.Popen([vscode_executable, template_project_dir])

        # Wait for VS Code to open (you may need to adjust the sleep duration)
        time.sleep(5)

        # Run the Flutter project using the terminal command
        subprocess.Popen([flutter_executable, 'run'], cwd=template_project_dir)

        # Wait for the app to start (adjust the sleep time if necessary)
        time.sleep(20)

        # Take a screenshot of the output UI
        screenshot = pyautogui.screenshot()

        # Save the screenshot
        screenshot.save(screenshot_path)

        print(f"Screenshot for {main_dart_file} taken and saved to {screenshot_path}.")
    except Exception as e:
        print(f"Error: {e}")

# Get all main.dart files from the specified directory
main_dart_files = [os.path.join(main_dart_dir, file) for file in os.listdir(main_dart_dir) if file.endswith('_main.dart')]

for main_dart_file in main_dart_files:
    # Extract student ID from the filename
    student_id = os.path.basename(main_dart_file).split('_')[0]

    # Define the path to save the screenshot
    screenshot_path = os.path.join(screenshot_save_dir, f'{student_id}.png')

    # Run the Flutter app with the given main.dart and take a screenshot
    run_flutter_and_screenshot(main_dart_file, screenshot_path)
