import requests
import os
import random
import subprocess

base_url = 'https://wallhaven.cc/api/v1/search'   #if you don't have a api key
# base_url = f"https://wallhaven.cc/api/v1/search?apikey=<{Api_key}>"    # if you have api key
q_input = input('Search a tag like anime, cgi etc : ')

if q_input == '':
    param = {
    'apikey': 'qSTxQe3509ZwHsLoLnEYoTIxnfy0Bc3w',
    #'q': q_input,                  # add search tag here like anime. sci-fi etc
    'categories': '101',
    'purity': '100,110',
    'sorting': 'toplist',
    'resolutions': '1920x1080',
    #'colors': '000000,ff6600,993399,66cccc,660000,424153,663300'
}
else:
    param = {
    'apikey': 'qSTxQe3509ZwHsLoLnEYoTIxnfy0Bc3w',
    'q': q_input,                  # add search tag here like anime. sci-fi etc
    'categories': '101',
    'purity': '100,110',
    'sorting': 'toplist',
    'resolutions': '1920x1080',
    #'colors': '000000,ff6600,993399,66cccc,660000,424153,663300'
}


# i = 0
# for i in range(3):
#     count = random.randint(0, len(q_list) - 1)
#     para = q_list[count]
#     param['q'] += " " + para
#     i += 1



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
    print('here')
else:
    index = random.randint(1, total-1)        #fixing index

# print(index)

image = data['data'][index]['path']         # getting path from the api response
image_get = requests.get(image)
image_name = f"{data['data'][index]['id']}_{index}.jpg"
with open(f"/home/x-xenon/Desktop/Wallpaper/{image_name}", 'wb') as f:      #writing file
    f.write(image_get.content)



p1 = subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', f"'file:///home/x-xenon/Desktop/Wallpaper/{image_name}'"], capture_output=True, text=True) #command set and execute

if p1.returncode == 0:
    print(f"Done.{image_name} is set as your wallpaper")
else:
    print("You got problem")

print(f"There are only {total} Wallpaper/s")

# print(p1.stderr)