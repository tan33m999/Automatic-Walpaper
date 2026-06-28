import requests
import os
import random
import subprocess

base_url = 'https://wallhaven.cc/api/v1/search'   #if you don't have a api key
# base_url = f"https://wallhaven.cc/api/v1/search?apikey=<{Api_key}>"    # if you have api key

param = {
    'apikey': 'qSTxQe3509ZwHsLoLnEYoTIxnfy0Bc3w',
    'q': 'girl, black, cgi',
    'categories': '101',
    'purity': '100,110',
    'sorting': 'toplist',
    'resolutions': '1920x1080',
    #'colors': '000000,ff6600,993399,66cccc,660000,424153,663300'
}


r = requests.get(f"{base_url}/", params=param)
# print(r.text)
data = r.json()
meta = data['meta']
# print(meta)
last_page = meta['last_page']
if last_page == 0:
    pass
else:
    param['page'] = random.randint(1, last_page)


r = requests.get(f"{base_url}/", params=param)
print(data)
total = len(data['data'])
if total == 1:
    index = total
elif total == 0:
    pass
else:
    index = random.randint(1, total)


image = data['data'][index]['path']         # getting path from the api response
image_get = requests.get(image)
image_name = f"{data['data'][index]['id']}_{index}.jpg"
with open(f"/home/x-xenon/Desktop/Wallpaper/{image_name}", 'wb') as f:
    f.write(image_get.content)



p1 = subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', f"'file:///home/x-xenon/Desktop/Wallpaper/{image_name}'"], capture_output=True, text=True)

if p1.returncode == 0:
    print(f"Done.{image_name} is set as your wallpaper")
else:
    print("You got problem")

print(f"There are only {total} Wallpaper/s")

# print(p1.stderr)