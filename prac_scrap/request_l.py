import requests
url = "https://xkcd.com/353/"
image = "https://imgs.xkcd.com/comics/python.png"
image_r = requests.get(image)
# print(image_r.content)
# with open('/home/x-xenon/Desktop/comic.png', "wb") as f:
#     f.write(image_r.content)

# print(image_r.status_code)
# print(image_r.ok)

# print(image_r.headers)

# print(requests.get("https://httpbin.org/").headers)

payload = {'username': 'taneem', 'password': 'testing'}
test = "https://httpbun.com/basic-auth/taneem/testing"
r = requests.get(test, auth=('taneem', 'testig'))
print(r)