from PIL import Image
import os

BASE_DIR = '/home/ubuntu/fichiers/photos/portfolio'
THUMB_DIR = '/home/ubuntu/fichiers/photos/thumbnails'

categories = ['Photographie', 'Designs']


for category in categories:
    src_folder = os.path.join(BASE_DIR, category)
    thumb_folder = os.path.join(THUMB_DIR, category)
    os.makedirs(thumb_folder, exist_ok=True)

    for filename in os.listdir(src_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            src_path = os.path.join(src_folder, filename)
            thumb_path = os.path.join(thumb_folder, filename)
            # if not os.path.exists(thumb_path):  # Avoid regenerating
            img = Image.open(src_path)
            img.thumbnail((500, 500))
            img.save(thumb_path, "JPEG", quality=50)
            print(f"Generated thumbnail for {filename} in {category}")
