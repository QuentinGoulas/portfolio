import streamlit as st
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

# Authentification avec Google (OAuth)
def auth_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Ouvre une fenêtre pour autoriser
    return GoogleDrive(gauth)

drive = auth_drive()

# ID du dossier Google Drive (copié depuis l’URL du dossier)
folder_id = "1SXgeLKhPRFW8ur6eQBqrpHNpBYxApi8u"

# Récupérer les fichiers du dossier
file_list = drive.ListFile({
    'q': f"'{folder_id}' in parents and trashed=false"
}).GetList()

st.title("🖼️ Mon Portfolio")

for file in file_list:
    if file['title'].lower().endswith(('.jpg', '.jpeg', '.png')):
        file_id = file['id']
        with open("images.json", "a") as json_file:
            json_file.write(f'{{"file_id": "{file_id}"}},\n')
        url = f"https://lh3.googleusercontent.com/d/{file_id}"
        print(url)
        st.image(url, caption=file['title'], use_container_width=True)
