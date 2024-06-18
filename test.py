import subprocess
import pyautogui
import time
import shutil
import os
import Quartz
import AppKit

# Path to the directory containing all main.dart files
main_dart_dir = '/path/to/answer'

# Path to the template Flutter project directory
template_project_dir = '/path/to/flutter_template'

# Path to the main.dart file in the template project
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

# Path to save the screenshots
screenshot_save_dir = '/path/to/save/screenshots'

# Full path to the Flutter executable
flutter_executable = '/Users/yourusername/flutter/bin/flutter'  # Update this path

# Ensure the screenshot save directory exists
os.makedirs(screenshot_save_dir, exist_ok=True)

def get_window_by_title(title):
    windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
    for window in windows:
        window_title = window.get('kCGWindowName', u'Unknown')
        if window_title == title:
            return window
    return None

def capture_window(window, screenshot_path):
    pid = window['kCGWindowOwnerPID']
    window_id = window['kCGWindowNumber']
    app = AppKit.NSRunningApplication.runningApplicationWithProcessIdentifier_(pid)
    options = Quartz.kCGWindowImageBoundsIgnoreFraming | Quartz.kCGWindowImageNominalResolution
    window_image = Quartz.CGWindowListCreateImage(Quartz.kCGWindowImageDefault, Quartz.kCGWindowListOptionIncludingWindow, window_id, options)
    bitmap_rep = AppKit.NSBitmapImageRep.alloc().initWithCGImage_(window_image)
    png_data = bitmap_rep.representationUsingType_properties_(AppKit.NSPNGFileType, None)
    png_data.writeToFile_atomically_(screenshot_path, True)

def run_flutter_and_screenshot(main_dart_file, screenshot_path):
    # Copy the main.dart file to the template project
    shutil.copy(main_dart_file, template_main_dart_path)

    # Run the Flutter app using the terminal command
    process = subprocess.Popen([flutter_executable, 'run'], cwd=template_project_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the app to start (adjust the sleep time if necessary)
    time.sleep(20)

    # Locate the Flutter app window (assuming the title contains 'Flutter')
    window = get_window_by_title('Flutter')
    if window:
        capture_window(window, screenshot_path)
    else:
        print(f"Flutter app window not found for {main_dart_file}")

    # Terminate the Flutter run process
    process.terminate()

    # Give some time to ensure the process is terminated
    time.sleep(5)

    print(f"Screenshot for {main_dart_file} taken and saved to {screenshot_path}.")

# Get all main.dart files from the specified directory
main_dart_files = [os.path.join(main_dart_dir, file) for file in os.listdir(main_dart_dir) if file.endswith('_main.dart')]

for main_dart_file in main_dart_files:
    # Extract student ID from the filename
    student_id = os.path.basename(main_dart_file).split('_')[0]

    # Define the path to save the screenshot
    screenshot_path = os.path.join(screenshot_save_dir, f'screenshot_{student_id}.png')

    # Run the Flutter app with the given main.dart and take a screenshot
    run_flutter_and_screenshot(main_dart_file, screenshot_path)
