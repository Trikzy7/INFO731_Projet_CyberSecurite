import os
import time
from pathlib import Path

def process_new_data():
    # Mettez ici le code que vous voulez exécuter à chaque fois qu'il y a de nouvelles données
    print("Nouvelles données détectées !")

def monitor_pcap_file(file_path):
    # Obtenez le chemin complet du fichier pcap
    file_path = Path(file_path).resolve()

    # Vérifiez si le fichier existe
    if not file_path.is_file():
        print(f"Le fichier {file_path} n'existe pas.")
        return

    # Obtenez la taille initiale du fichier
    initial_size = file_path.stat().st_size

    # Surveillez le fichier en continu
    while True:
        # Vérifiez la taille actuelle du fichier
        current_size = file_path.stat().st_size

        # Si la taille a changé, traitez les nouvelles données
        if current_size > initial_size:
            process_new_data()

            # Mettez à jour la taille initiale du fichier
            initial_size = current_size

        # Pause pour éviter une utilisation excessive du processeur
        time.sleep(1)

if __name__ == "__main__":
    # Spécifiez le chemin du fichier pcap à surveiller
    pcap_file_path = "/usr/local/dns_traffic.pcap"

    # Lancez la surveillance du fichier pcap
    monitor_pcap_file(pcap_file_path)
