from pyquery import PyQuery as pq
import threading

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


def myPrint(s):
    print(str(s))
if __name__ == '__main__':
    t = threading.Thread(target=myPrint('hello thread',)) #使用进程 也是类似
    t.start()
    t.join()