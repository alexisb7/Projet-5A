# Projet-5A

Ouvrir un terminal/shell depuis un dossier prédéfini.

Cloner le répertoire github dans ce dossier, taper : git clone https://github.com/alexisb7/Projet-5A.git

Se placer dans le dossier 'Projet-5A' et créer un environnement virtuel python : cd 'Projet-5A' puis python -m venv webapp ou python3 -m venv webapp

Activer l'environnement virtuel python : 
- Windows Powershell: webapp\Scripts\activate
- Terminal Linux (MacOS) : source webapp/bin/activate

Télécharger les librairies python suivantes: pip3 install qrcode, pillow, pandas, matplotlib, dataframe_image, flask, openpyxl

Pour exécuter l'application web, se placer dans le dossier 'Projet: cd 'Projet'
1. Indiquer à flask l'application web à exécuter :
   - Windows Powershell: set FLASK_APP=app.py
   - Terminal Linux (MacOS) : export FLASK_APP=app.py
2. Démarrer l'application : commande 'flask run'

Pour quitter l'application: control^C

Pour désactiver l'environnement virtuel python: deactivate
