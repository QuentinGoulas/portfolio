from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json

# Authentification (ouvre une fenêtre de navigateur la 1ère fois)
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Auth via navigateur
drive = GoogleDrive(gauth)

# 📂 Lister les fichiers images dans un dossier
def list_images_in_folder(folder_id):
    query = f"'{folder_id}' in parents and mimeType contains 'image/' and trashed=false"
    file_list = drive.ListFile({'q': query}).GetList()
    return [f"https://lh3.googleusercontent.com/d/{f['id']}" for f in file_list]

# 🔍 Récupérer le dossier principal
portfolio_id = "1SXgeLKhPRFW8ur6eQBqrpHNpBYxApi8u"  # ID du dossier portfolio

# 🔍 Récupérer les sous-dossiers
query = f"'{portfolio_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
categories = drive.ListFile({'q': query}).GetList()

# 📦 Construire la structure du JSON
data = {}
for folder in categories:
    name = folder['title']
    id_ = folder['id']
    data[name] = list_images_in_folder(id_)

# 💾 Sauvegarder le JSON en local
with open("images.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
print("✅ Fichier images.json généré")

# 🚀 Écrire sur le fichier existant sur Google Drive en remplaçant tout
query = f"'{portfolio_id}' in parents and title='images.json' and trashed=false"
existing_files = drive.ListFile({'q': query}).GetList()

if existing_files:
    file = existing_files[0]  # Prendre le premier fichier correspondant
    file.SetContentFile('images.json')
    file.Upload()
    print("📤 Contenu de images.json mis à jour sur Google Drive")
else:
    # Si le fichier n'existe pas, le créer
    file = drive.CreateFile({'title': 'images.json', 'parents': [{'id': portfolio_id}]})
    file.SetContentFile('images.json')
    file.Upload()
    print("📤 Nouveau fichier images.json créé et uploadé sur Google Drive")
