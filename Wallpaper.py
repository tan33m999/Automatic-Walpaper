import requests
import os
import random
import subprocess

base_url = 'https://wallhaven.cc/api/v1/search'   #if you don't have a api key
q_input = input('Search a tag like anime, cgi etc or just press "Enter": ')

if q_input == '':
    param = {
    'apikey': 'qSTxQe3509ZwHsLoLnEYoTIxnfy0Bc3w',
    #'q': q_input,                  # add search tag here like anime. sci-fi etc
    'categories': '111',
    'purity': '111',
    'sorting': 'toplist',
    'resolutions': '1920x1080',
    #'colors': '000000,ff6600,993399,66cccc,660000,424153,663300'
}
else:
    param = {
    'apikey': 'qSTxQe3509ZwHsLoLnEYoTIxnfy0Bc3w',
    'q': q_input,                  # add search tag here like anime. sci-fi etc
    'categories': '110',
    'purity': '111',
    'sorting': 'toplist',
    'resolutions': '1920x1080',
    #'colors': '000000,ff6600,993399,66cccc,660000,424153,663300'
}


r = requests.get(f"{base_url}/", params=param)
# scifprint(r.url)
# print(r.text)
data = r.json()
meta = data['meta']
# print(meta)
last_page = meta['last_page']
if last_page == 0:
    pass
else:
    param['page'] = random.randint(1, last_page)            # checking pages


r = requests.get(f"{base_url}/", params=param)  #updated the params
# print(data)
total = len(data['data'])
if total == 1:
    index = total
elif total == 0:
    pass
else:
    index = random.randint(1, total-1)        #fixing index

# print(index)
try:

    image = data['data'][index]['path']         # getting path from the api response
    image_get = requests.get(image)
    image_name = f"{data['data'][index]['id']}_{index}.jpg"
    with open(f"/home/x-xenon/Desktop/Wallpaper/{image_name}", 'wb') as f:      #writing file
        f.write(image_get.content)

    actual_path = f"/home/x-xenon/Desktop/Wallpaper/{image_name}"
    shortcut_path = "/home/x-xenon/Desktop/Wallpaper/current_wall.jpg"

    if os.path.exists(shortcut_path):
        os.remove(shortcut_path)
    else:
        pass
    
    os.symlink(actual_path, shortcut_path)



    p1 = subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', f'file://{actual_path}'], capture_output=True, text=True) #command set and execute
    p2 = subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', f'file://{shortcut_path}'], capture_output=True, text=True) #command create a shortcut path

    if p1.returncode == 0:
        print(f"Done.{image_name} is set as your wallpaper")
    else:
        print("You got problem")
except:
    print(f"There are only {total} Wallpaper/s")

#print(p1.stderr)