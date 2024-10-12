import subprocess
import os

# paths to the executables of the programs you want to launch
apps_to_open = [
    r"C:\C Drive - Downloads and Installations\Capture2Text\Capture2Text\Capture2Text.exe",      # Update with the actual path
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",  # Path to Chrome
    r"C:\C Drive - Downloads and Installations\ClipAngel - Copy Clipboard\ClipAngel.exe",         # Update with the actual path
    r"C:\Users\Siris\AppData\Local\electron\Rize.exe",              # Update with the actual path
    r"C:\Users\Siris\AppData\Local\Programs\Notion\Notion.exe"             # Update with the actual path
]

# function to launch each application
def launch_applications(apps):
    for app in apps:
        try:
            subprocess.Popen(app)
            print(f"Started {app}")
        except Exception as e:
            print(f"Error starting {app}: {e}")

# launch the apps
launch_applications(apps_to_open)
