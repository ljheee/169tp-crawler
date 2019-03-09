from pyquery import PyQuery as pq

doc = pq('https://www.baidu.com/')
print(doc)


class Pic:
    def __init__(self,name,url):
        self.name=name;
        self.url=url;

pics =[]
p= Pic('a','uurl')
pics.append(p)
print(p.name)
print(len(pics))