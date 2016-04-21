#!--coding:utf8--
import redis

#创建后就把它发送到聊天室
r = redis.Redis(host='localhost', port=6379, db=0,password='db2016')
count = 0
while(count<10):
	count += 1
	r.publish('chat', 'message...'+str(count))