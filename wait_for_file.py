import os
import subprocess
import time
 
# Path to the specific file
file_path = '/C/Path/a.dat'
 
# Path to the script to be triggered
script_to_run = 'path/to/b.py'
 
# Function to check if the file exists
def check_file_exists(file_path):
    return os.path.isfile(file_path)
 
# Function to trigger another Python script
def trigger_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
        print(f"Successfully triggered {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {script_path}: {e}")
 
# Main function
def main():
    while True:
        if check_file_exists(file_path):
            print(f"File {file_path} found.")
            trigger_script(script_to_run)
            break
        else:
            print(f"File {file_path} not found. Retrying in 10 minutes...")
            time.sleep(600)  # Sleep for 10 minutes (600 seconds)
 
if __name__ == "__main__":
    main()