from flask import Flask, render_template
import requests
import json

app = Flask(__name__)



DRIVE_JSON_URL = "https://drive.google.com/uc?export=download&id=112zR5UMkO4aTAX3i9ZsnrzbosckATvan"  # remplace par ton vrai ID

def get_images():
    data = requests.get(DRIVE_JSON_URL).json()
    return data

@app.route('/')
def index():
    try:
        images_by_category = get_images()
        return render_template('index.html', images_by_category=images_by_category)
    except Exception as e:
        return f"<h1>Erreur lors du chargement des données : {e}</h1>"

# @app.route("/")
# def index():
#     try:
#         response = requests.get(DRIVE_JSON_URL)
#         images = response.json()  # auto conversion du JSON
#         list_url = []
#         for img in images:
#             list_url.append(f"https://lh3.googleusercontent.com/d/{img['file_id']}")

#         return render_template("index.html", images=list_url)

#     except Exception as e:
#         return f"<h1>Erreur lors du chargement des données : {e}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
