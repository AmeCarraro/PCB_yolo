import subprocess
import sys
import os

# Percorso alla cartella dove tieni tutti gli script
SCRIPT_DIR = "C:\\Users\\carra\\Prova PCB\\scripts"

# Lista degli script da eseguire in ordine
scripts = [
    "data_handler.py",
    "train_val_test.py",
    "data_yaml.py",
    "training_yolo.py",
    "test_yolo.py"
]

def run_script(script_name):
    script_path = os.path.join(SCRIPT_DIR, script_name)
    print(f"\n🚀 Lancio {script_name} ...")
    result = subprocess.run([sys.executable, script_path], text=True)
    
    if result.returncode == 0:
        print(f"✅ {script_name} completato!")
        print(result.stdout)   # stampa eventuali output
    else:
        print(f"❌ Errore in {script_name}")
        print(result.stderr)
        sys.exit(1)  # ferma la pipeline in caso di errore

if __name__ == "__main__":
    for script in scripts:
        run_script(script)

    print("\n🎉 Pipeline completata con successo!")
