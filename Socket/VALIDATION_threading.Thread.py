import time
import requests
import threading

img_urls = ['https://cdn.pixabay.com/photo/2017/10/13/14/15/fantasy-2847724_960_720.jpg']

def download_image(img_url):
    print(f"Task starts for 1 second")
    time.sleep(1)
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
    print(f"Task ends")

if __name__ == '__main__':
    start = time.perf_counter()

    t1 = threading.Thread(target=download_image, args=[img_urls[0]])
    t1.start()
    t1.join()

    end = time.perf_counter()

    print(f"Tasks ended in {round(end - start, 2)} second(s)")