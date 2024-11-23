import os
import requests
from PIL import Image
import json

def fetch_images(base_url, start, end, directory):
    os.makedirs(directory, exist_ok=True)
    data = []

    for i in range(start, end + 1):
        url = f"{base_url}/{i}_grand.jpg"
        response = requests.get(url)
        
        if response.status_code == 200:
            file_path = f"{directory}/{i}.jpg"
            with open(file_path, 'wb') as file:
                file.write(response.content)
            
            # Open the image to get dimensions
            with Image.open(file_path) as img:
                width, height = img.size
                aspect_ratio = width / height
                vertical = height > width
                
                data.append({
                    "file": f"{i}.jpg",
                    "width": width,
                    "height": height,
                    "aspect_ratio": aspect_ratio,
                    "vertical": vertical
                })
        else:
            print(f"Failed to download image {i}")

    # Save data to data.json
    with open(f'{directory}/data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Fetch images for crados1
fetch_images("https://www.lescrados.com/images/crados04", 1, 192, 'data/crados1')

# Fetch images for crados2
fetch_images("https://www.lescrados.com/images/crados2", 178, 386, 'data/crados2')