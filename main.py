from flask import Flask, render_template, send_from_directory, url_for, send_file, request
from PIL import Image
import io
import os

app = Flask(__name__)

# Define the path to your external images
IMAGES_FOLDER = os.path.expanduser("~/fichiers")

# Register the custom route to serve files from the external folder
@app.route('/fichiers/<path:filename>')
def custom_static(filename):
    # Paramètres de qualité depuis l'URL (par défaut: 100% qualité)
    quality = request.args.get('quality', default=100, type=int)
    width = request.args.get('width', default=None, type=int)

    # Chemin vers l'image originale
    image_path = os.path.join(IMAGES_FOLDER, filename)
    
    # Ouvrir l'image
    img = Image.open(image_path)
    
    # Redimensionner si nécessaire
    if width:
        # Calculer la hauteur proportionnellement
        ratio = width / img.width
        height = int(img.height * ratio)
        img = img.resize((width, height), Image.LANCZOS)
    
    # Préparer un buffer pour stocker l'image compressée
    buffer = io.BytesIO()
    
    # Sauvegarder avec la qualité réduite
    img.save(buffer, format='JPEG', quality=quality)
    buffer.seek(0)
    return send_file(buffer, mimetype='image/jpeg')
    # return send_from_directory(IMAGES_FOLDER, filename)

# @app.route('/image/<filename>')
# def serve_image(filename):
#     # Paramètres de qualité depuis l'URL (par défaut: 100% qualité)
#     quality = request.args.get('quality', default=100, type=int)
#     width = request.args.get('width', default=None, type=int)

#     # Chemin vers l'image originale
#     image_path = os.path.join(IMAGES_FOLDER, filename)
    
#     # Ouvrir l'image
#     img = Image.open(image_path)
    
#     # Redimensionner si nécessaire
#     if width:
#         # Calculer la hauteur proportionnellement
#         ratio = width / img.width
#         height = int(img.height * ratio)
#         img = img.resize((width, height), Image.LANCZOS)
    
#     # Préparer un buffer pour stocker l'image compressée
#     buffer = io.BytesIO()
    
#     # Sauvegarder avec la qualité réduite
#     img.save(buffer, format='JPEG', quality=quality)
#     buffer.seek(0)
#     return send_file(buffer, mimetype='image/jpeg')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/photos")
def photos():
    images = []
    # Path to the photography images in the external folder
    photos_folder = os.path.join(IMAGES_FOLDER, 'photos/portfolio/Photographie')
    
    # Get all image files from the directory
    if os.path.exists(photos_folder):
        for file in os.listdir(photos_folder):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Create URL for the images using the custom route
                image_path = f'/fichiers/photos/portfolio/Photographie{file}'
                images.append(image_path)
    
    return render_template("photos.html", images=images)

@app.route("/designs")
def designs():
    images = []
    # Path to the design images in the external folder
    designs_folder = os.path.join(IMAGES_FOLDER, 'photos/portfolio/Design')
    
    # Get all image files from the directory
    if os.path.exists(designs_folder):
        for file in os.listdir(designs_folder):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Create URL for the images using the custom route
                image_path = f'/fichiers/photos/portfolio/Design/{file}'
                images.append(image_path)
    
    return render_template("designs.html", images=images)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")