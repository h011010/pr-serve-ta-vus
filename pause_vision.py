import argparse
import time
import os
import platform

# Configuration du parser d'arguments
parser = argparse.ArgumentParser()
parser.add_argument("--session", help="le nombre de session", type=int)
parser.add_argument("--durée", "-d", help="durée de session en minutes", type=int)
parser.add_argument("--pause", "-p", help="durée de pause en minutes", type=int)

args = parser.parse_args()

# Vérification que l'argument 'session' a été passé
if args.session is None:
    print("Erreur: Le nombre de sessions (--session) doit être spécifié.")
    exit(1)

# Fonction de session avec pause
def session(durée, pause):
    time.sleep(durée * 60)  # Attente pendant la durée de la session (en minutes)
    time.sleep(pause * 60)  # Attente pendant la durée de la pause (en minutes)
   

# Fonction pour mettre l'ordinateur en veille selon le système d'exploitation
def mettre_en_veille():
    systeme = platform.system()
    if systeme == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Commande pour Windows
    elif systeme == "Darwin":  # "Darwin" pour MacOS
        os.system("pmset sleepnow")  # Commande pour MacOS
    else:
        print("La mise en veille automatique n'est pas prise en charge pour ce système.")

# Lancer les sessions
for i in range(args.session):
    print(f"Session {i + 1} a commencé")
    session(args.durée, args.pause)  # Lancer une session suivie d'une pause
    print(f"Session {i + 1} terminée. Mise en veille de l'ordinateur.")
    mettre_en_veille()  # Met l'ordinateur en veille après chaque session
