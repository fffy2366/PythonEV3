#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# python serial 获取所有的串口名称
# http://blog.csdn.net/qq61394323/article/details/44619511
import serial
import serial.tools.list_ports
import thread
import time

port_list = list(serial.tools.list_ports.comports())


def receiver(p):
    print "port:" + p+"\n"

    try:
        EV3 = serial.Serial(p)
        print "Listening for EV3 Bluetooth(" + p + ") messages, press CTRL C to quit."
        while 1:
            n = EV3.inWaiting()
            if n <> 0:
                s = EV3.read(n)
                str = ""
                for n in s:
                    str = str + " " + "%02X" % ord(n)
                if "00 04 00 00 00 80 3F" in str:
                    print "a"
                elif "00 04 00 00 00 00 40" in str:
                    print "b"
                elif "00 04 00 00 00 40 40" in str:
                    print "c"
                elif "00 04 00 00 00 80 40" in str:
                    print "d"
                print str
                print
            else:
                # No data is ready to be processed
                time.sleep(0.5)
        EV3.close()
    except Exception, e:
    # except KeyboardInterrupt,e:
        pass



if len(port_list) <= 0:
    print "The Serial port can't find!"

else:
    # print len(port_list)
    for ps in port_list:
        p = list(ps)[0]
        # print p
        try:
            # ser = serial.Serial(p,9600,timeout = 60)
            # print "check which port was really used >",ser.name
            # receiver(p)
            thread.start_new_thread(receiver, (p,))
        except Exception, e:
            pass

try:
    while 1:
        time.sleep(5)
        pass
except KeyboardInterrupt,e:
    pass