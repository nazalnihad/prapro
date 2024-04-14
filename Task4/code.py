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
import psutil

file_path = "C:/Users/nazal/Downloads/links.parquet"
urls = pq.read_table(file_path,columns=["URL"]).to_pandas()
# r = requests.get('https://drive.google.com/file/d/1ym_RbsjN41cwXZLeB3NibN7h7Vbz1AgP/view?usp=sharing')
# print(r.encoding)
# for i in range(5):
#     print(urls.iloc[i].URL)

def download_images(urls,count=100):
    i=0
    path = 'C:/Users/nazal/Downloads/images'
    os.makedirs(path,exist_ok=True)

    while i<=count:
        link = urls.iloc[i].URL
        try:
            response = requests.get(link)
            if response.status_code==200:

                # extension = os.path.splitext(link)
                # extension = os.path.splitext(link)[1]
                # if extension.startswith('.'):
                #     not in [".png",".jpg",".jpeg"]:
                extension = link.split("/")[-1]
                extension = extension.split("?")[0]
                extension = extension.split(".")[-1]
                if extension=="":
                    extension="jpg"

                # img = BytesIO(response.content)
                # img = Image.open(img)
                # img.save(f"{path}/img_{i}.{extension}")
                # print(extension)
                img_path = f"{path}/img_{i}.{extension}"
                with open(img_path,"wb") as f:
                    f.write(response.content)
                    print(f"img_{i} downloaded")

                print("=== cpu and network usage ===")
                print(f"cpu usage - {psutil.cpu_percent()}")
                network = psutil.net_io_counters()
                print(f"bytes sent - {network.bytes_sent}")
                print(f"bytes recieved - {network.bytes_recv}")
                print("=============================")
                
            else:
                print("failed to donwload ")

        except Exception as e:
            print(e)
        i+=1
        
    # img.close()

download_images(urls,500)


