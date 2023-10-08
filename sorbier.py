import requests
from colorama import Fore, Style
from pystyle import Colors, Colorate

# Clé API et ID de Recherche Personalisé
API_KEY = 'AIzaSyAa62JJDOZUvx_8izt2gfXUnYk_tec26Z0'
CX = 'c3aba39f3685f4fce'

# Bannière(s)
# Notez qu'il est possible qu'une Mise-à-Jour soit effectuée pour mettre un système changeant le style de la bannière à chaque démarrage 

banner = """
░██████╗░█████╗░██████╗░██████╗░██╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔══██╗
╚█████╗░██║░░██║██████╔╝██████╦╝██║█████╗░░██████╔╝
░╚═══██╗██║░░██║██╔══██╗██╔══██╗██║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░░██║██████╦╝██║███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚══════╝╚═╝░░╚═╝"""

print(Colorate.Horizontal(Colors.blue_to_green, banner, 1))

def recherche_google(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for i, item in enumerate(data.get('items', [])):
            title = item.get('title', '')
            link = item.get('link', '')
            
            # Titre bleu 
            print(Fore.BLUE + f"{i + 1}. {title}")
            
            # Lien vert
            print(Fore.GREEN + f"   {link}")
            
            # Réinitialisation de la couleur
            print(Style.RESET_ALL)
    else:
        print("\nOops, votre requête a échoué.")

query = input("\nVous cherchez ? : ")
recherche_google(query)
