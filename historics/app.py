import streamlit as st
import requests
import json

# Lien vers ton fichier JSON partagé publiquement
json_url = "https://drive.google.com/uc?export=download&id=1of6LdvllA0jhtk_su7-doO2I4D-FoKOw"

response = requests.get(json_url)

st.title("🖼️ Mon Portfolio")
columns = st.columns(3, gap="small")

if response.status_code == 200:
    try:
        # Lecture du JSON
        data = response.json()  
        # Cas 1 : juste une liste d'IDs
        if isinstance(data, list) and isinstance(data[0], str):
            for file_id in data:
                img_url = f"https://lh3.googleusercontent.com/d/{file_id}"
                st.image(img_url, use_column_width=False)

        # Cas 2 : liste de dicts avec id, title, desc
        elif isinstance(data, list) and isinstance(data[0], dict):
            i = 0
            for item in data:
                with columns[i % 3]:
                    file_id = item["file_id"]
                    title = item.get("title", "")
                    desc = item.get("desc", "")
                    img_url = f"https://lh3.googleusercontent.com/d/{file_id}"
                    st.image(img_url, caption=f"{title} - {desc}", use_container_width=False)
                    i += 1
    
    except Exception as e:
        st.error(f"Erreur lors de la lecture du JSON : {e}")

else:
    st.error("Impossible de lire le fichier JSON.")

# with open("images.json", "r") as json_file:
#     data = json_file.readlines()
#     file_ids = [line.split('"')[3] for line in data if '"file_id"' in line]


# for i in range(0, len(file_ids)):
#     with columns[i % 3]:
#         st.image(f"https://lh3.googleusercontent.com/d/{file_ids[i]}", use_container_width=True)
