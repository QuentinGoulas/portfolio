from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/photos")
def photos():
    images = []
    # Path to the images in the static folder
    static_folder = os.path.join(app.static_folder, 'Photos Portfolio/Photographie')
    
    # Get all image files from the static/photos directory
    if os.path.exists(static_folder):
        for file in os.listdir(static_folder):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Create the URL for the image using url_for
                image_path = url_for('static', filename=f'Photos Portfolio/Photographie/{file}')
                images.append(image_path)
    
    return render_template("photos.html", images=images)

@app.route("/designs")
def designs():
    images = []
    # Path to the images in the static folder
    static_folder = os.path.join(app.static_folder, 'Photos Portfolio/Design')
    
    # Get all image files from the static/photos directory
    if os.path.exists(static_folder):
        for file in os.listdir(static_folder):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Create the URL for the image using url_for
                image_path = url_for('static', filename=f'Photos Portfolio/Design/{file}')
                images.append(image_path)
    
    return render_template("designs.html", images=images)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)