from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    base_path = os.path.join(app.static_folder, "images")
    categories = {}

    for category in os.listdir(base_path):
        category_path = os.path.join(base_path, category)
        if os.path.isdir(category_path):
            images = []
            for file in os.listdir(category_path):
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    relative_path = os.path.relpath(os.path.join("images", category, file))
                    images.append(url_for("static", filename=relative_path.replace("\\", "/")))
            categories[category] = images

    return render_template("index.html", categories=categories)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
