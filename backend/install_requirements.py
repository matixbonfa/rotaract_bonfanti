import os
import sys
import subprocess

# Librerie necessarie
packages = [
    "flask",
    "flask-cors",
    "sqlite3-binary",  # fallback, sqlite è già built-in ma serve in alcuni ambienti
    "requests",
    "python-dotenv"
]

print("🔧 Installazione librerie per il progetto Rotaract Trento...\n")

for package in packages:
    try:
        print(f"➡️  Installo {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"❌ Errore nell’installazione di {package}. Controlla la connessione o i permessi.")

print("\n✅ Tutte le librerie dovrebbero essere installate correttamente!")
print("Puoi ora avviare il tuo server Flask con: python app.py")
