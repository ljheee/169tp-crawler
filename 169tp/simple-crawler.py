import os
import requests
from pyquery import PyQuery as pq

#构造请求头
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}

def The_URL(page):
    url = 'https://www.169tp.com/shoujibizhi/list_6_' + str(page) + '.html';
    request_data = requests.get(url, headers).content.decode('gbk');

    doc = pq(request_data);#构造pyquery
    product = doc('.pic').items()# class类选择器 找到所有项

    for i in product:
        pic_name = i.text()
        pic_url = i.attr('href')
        print('pic_name={},pic_url={}'.format(pic_name,pic_url))
        download_pic(pic_name, pic_url)


def download_pic(file, url):
    count = 1;
    second_request = requests.get(url, headers).content.decode('gbk')

    doc2 = pq(second_request);
    big_img = doc2('.big_img p img').items();
    for i in big_img:
        save = i.attr('src')
        response = requests.get(save)
        the_name = 'images/list6'
        save_address = str(the_name)

        if not os.path.exists(save_address):
            os.makedirs(save_address)
        else:
            #w 表示不存在就创建
            #b 二进制读写
            with open(save_address + '/{}.jpg'.format(file), "wb") as f:
                f.write(response.content)
                f.flush()
                print('downloaded {}'.format(count))
            count += 1;


The_URL(1)  # 下载第一页
