import requests
import os
import random
import subprocess

base_url = 'https://wallhaven.cc/api/v1/search'
wall_id = '6lpdjl'
param = {
    'q': 'anime',
    'categories': '101',
    'purity': '100',
    'sorting': 'toplist',
    'resolutions': '1920x1080'
}

r = requests.get(f"{base_url}/", params=param)
#print(r.url)
index = random.randint(0, 10)
data = r.json()
image = data['data'][index]['path']
image_get = requests.get(image)
image_name = f"url_{index}.jpg"
with open(f"/home/x-xenon/Desktop/Wallpaper/{image_name}", 'wb') as f:
    f.write(image_get.content)
 


# p1 = subprocess.run(['gsettings get org.cinnamon.desktop.background picture-uri'
# ], shell=True, capture_output=True, text=True)


