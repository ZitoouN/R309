import time
import concurrent.futures
import requests
import multiprocessing

img_urls = ['https://cdn.pixabay.com/photo/2017/10/13/14/15/fantasy-2847724_960_720.jpg']

def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")