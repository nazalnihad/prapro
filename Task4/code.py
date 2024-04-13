"""
Task 4

Download links.parquet from https://drive.google.com/file/d/1ym_RbsjN41cwXZLeB3NibN7h7Vbz1AgP/view?usp=sharing

Download and save the first 10,000 images from the links in the parquet file.

- Monitor CPU and network usage during download.

References:
pyarrow package
requests package
"""
import requests
import pyarrow.parquet as pq
import os
from io import BytesIO
from PIL import Image

file_path = "C:/Users/nazal/Downloads/links.parquet"
urls = pq.read_table(file_path,columns=["URL"]).to_pandas()
# r = requests.get('https://drive.google.com/file/d/1ym_RbsjN41cwXZLeB3NibN7h7Vbz1AgP/view?usp=sharing')
# print(r.encoding)
# for i in range(5):
#     print(urls.iloc[i].URL)

def download_images(urls,count=10):
    i=0
    path = 'C:/Users/nazal/Downloads/images'
    os.makedirs(path,exist_ok=True)
    while i<=count:
        link = urls.iloc[i].URL
        try:
            response = requests.get(link)
            if response.status_code==200:
                # with open(f"{path}/img_{i}.png",'wb'):
                #     file.write(response.content)
                # filename, extension = os.path.splitext(link)
                extension = link.split("/")[-1]
                extension = extension.split("?")[0]
                extension = extension.split(".")[-1]
                if extension=="":
                    extension="jpg"
                img = BytesIO(response.content)
                img = Image.open(img)
                img.save(f"{path}/img_{i}.{extension}")
                print(extension)
        except Exception as e:
            print(e)
        i+=1
    # img.close()

download_images(urls)


