import subprocess
import sys
import os

# Path to the folder where all the scripts are stored
SCRIPT_DIR = "C:\\Users\\carra\\Prova PCB\\scripts"

# List of scripts to run in order
scripts = [
    "data_handler.py",
    "train_val_test.py",
    "data_yaml.py",
    "training_yolo.py",
    "test_yolo.py"
]

def run_script(script_name):
    script_path = os.path.join(SCRIPT_DIR, script_name)
    print(f"\n Execute the script {script_name} ...")
    result = subprocess.run([sys.executable, script_path], text=True)
    
    if result.returncode == 0:
        print(f"{script_name} Completed!")
        print(result.stdout)   # Print any outputs
    else:
        print(f" Error in {script_name}")
        print(result.stderr)
        sys.exit(1)  # Stop the pipeline in case of an error

if __name__ == "__main__":
    for script in scripts:
        run_script(script)

    print("\n Pipeline completed successfully!")
