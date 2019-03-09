import os
import requests
import threading
import time
from pyquery import PyQuery as pq



headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}

class Pic:
    def __init__(self,name,url):
        self.name=name;
        self.url=url;

pics =[]

def get_url(page):
    # https://www.169tp.com/rentiyishu/list_8_3.html
    url = 'https://www.169tp.com/rentiyishu/list_8_' + str(page) + '.html';
    request_data = requests.get(url, headers).content.decode('gbk');
    doc = pq(request_data);
    product = doc('.pic').items()

    for i in product:
        pic_name = i.text()
        pic_url = i.attr('href')
        # download_pic(pic_name, pic_url)
        p = Pic(pic_name, pic_url)
        pics.append(p)

def download_pic(pic_name, pic_url):
    count = 1;
    second_request = requests.get(pic_url, headers).content.decode('gbk')

    doc2 = pq(second_request);
    big_img = doc2('.big_img p img').items();
    for i in big_img:
        save = i.attr('src')
        sponse = requests.get(save)
        the_name = 'images/list8'
        save_address = str(the_name)

        if not os.path.exists(save_address):
            os.makedirs(save_address)
        else:
            with open(save_address + '/{}.jpg'.format(pic_name), "wb") as f:
                f.write(sponse.content)
                print('downloaded {}'.format(count))
            count += 1;

for n in range(8):
    get_url(n)

print(len(pics))

for i in range(len(pics)):
    download_pic(pics[i].name,pics[i].url)

# if __name__ == '__main__':
#     t = threading.Thread(target=get_url(1,))
#     t.start()
#     t.join()



