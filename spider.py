import requests
import json
res = requests.session()
def spider(url):
    response = res.get(url=url)
    print(response.json())


import gevent
gevent.joinall([
    gevent.spawn(spider(http://hq.sinajs.cn/list=sh601002))
    gevent.spawn(spider(http://hq.sinajs.cn/list=sh601003))
    gevent.spawn(spider(http://hq.sinajs.cn/list=sh601004))
    gevent.spawn(spider(http://hq.sinajs.cn/list=sh601005))
    gevent.spawn(spider(http://hq.sinajs.cn/list=sh601006))
])
