from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

IMAGE_DIR = "/home/user/fichiers"

@app.route("/")
def index():
    categories = {}
    for category in os.listdir(IMAGE_DIR):
        category_path = os.path.join(IMAGE_DIR, category)
        if os.path.isdir(category_path):
            images = [
                f"/images/{category}/{img}"
                for img in os.listdir(category_path)
                if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
            ]
            categories[category] = images
    return render_template("index.html", categories=categories)

@app.route("/images/<category>/<filename>")
def serve_image(category, filename):
    return send_from_directory(os.path.join(IMAGE_DIR, category), filename)
