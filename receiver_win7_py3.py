#-*-coding:utf-8-*-
'''
while True:
   with open('/dev/tty.EV3-SerialPort', 'w+', 0) as bt:
      incoming = bt.read()
      print incoming
'''
import serial
import time
import sys
import binascii
import logging

#reload(sys) 
#sys.setdefaultencoding('utf-8')
#
# 创建一个logger 
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG) 
   
# 创建一个handler，用于写入日志文件 
fh = logging.FileHandler('test.log') 
fh.setLevel(logging.DEBUG) 
   
# 再创建一个handler，用于输出到控制台 
ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG) 
   
# 定义handler的输出格式 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
fh.setFormatter(formatter) 
ch.setFormatter(formatter) 
   
# 给logger添加handler 
logger.addHandler(fh) 
#logger.addHandler(ch)
   
# 记录一条日志 
logger.info('foorbar') 
#该代码片段来自于: http://www.sharejs.com/codes/python/6248

#EV3 = serial.Serial('/dev/tty.EV3-SerialPort')
EV3 = serial.Serial('COM3')
print("Listening for EV3 Bluetooth messages, press CTRL C to quit.")
try:
   while 1:
      n = EV3.inWaiting()
      if(n != 0):
         s = EV3.read(n)
         str = ""
         for n in s:
            #print("%02X" % ord(n)),
            #logger.info(n),
            #print(n)
            #ord("a")->97
            #print(ord(n)),
            #print("-------")
         
            #str = str +" "+"%02X" % ord(n)
            str = str +" "+"%02X" % n
         #str = n
         if "00 04 00 00 00 80 3F" in str:
            print("a")
         elif "00 04 00 00 00 00 40" in str:
            print("b")
         elif "00 04 00 00 00 40 40" in str:
            print("c")
         elif "00 04 00 00 00 80 40" in str:
            print("d")
         print(str)
         print()
      else:
         # No data is ready to be processed
         time.sleep(0.5)
except KeyboardInterrupt:
   pass
EV3.close()
