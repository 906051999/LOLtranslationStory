import urllib.request
import os

img_url = "https://shp.qpic.cn/cfwebcap/0/29517b595c6e8aa814cfdddd24c29ea6/0/?width=1035&height=641"
img_path = "image.jpg"  # 替换为您想要保存图片的路径

img_name = img_url.split('/')[+3] + ".jpg"
print(img_name)

img_path = os.path.join("./", img_name)
urllib.request.urlretrieve(img_url, img_path)