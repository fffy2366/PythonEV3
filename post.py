#!--coding:utf8--
import urllib2
import urllib
import json
import sys

reload(sys) 
sys.setdefaultencoding('utf-8')

#定义一个要提交的数据数组(字典)
data = {}
data['param1'] = 'xx'
data['param2'] = 'xx'

#定义post的地址
url = 'http://api.vastrek.cn/sys/getsliderimg'
post_data = urllib.urlencode(data)

#提交，发送数据
req = urllib2.urlopen(url, post_data)

#获取提交后返回的信息
content = req.read()
c = json.loads(content,encoding='utf-8')
print content
print c[0].keys()
print c[0]["title"]