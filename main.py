from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Emplacement des images, à adapter selon ton VPS
BASE_IMAGE_PATH = "/home/ubuntu/fichiers/photos/portfolio"

@app.route("/")
def index():
    categories = {}
    for category in os.listdir(BASE_IMAGE_PATH):
        category_path = os.path.join(BASE_IMAGE_PATH, category)
        if os.path.isdir(category_path):
            images = [
                f"/images/{category}/{img}"
                for img in os.listdir(category_path)
                if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
            ]
            categories[category] = images
    return render_template("index.html", categories=categories)

# Route spéciale pour servir les images
@app.route("/images/<category>/<filename>")
def serve_image(category, filename):
    image_folder = os.path.join(BASE_IMAGE_PATH, category)
    return send_from_directory(image_folder, filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)