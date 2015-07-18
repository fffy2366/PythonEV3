import time
import struct
import sys
sys.path.append ('/Users/EthanBurrell/Documents/SummerCode/EV3Python')
from pylib import ports_to_int
from pylib import move_time
from pylib import motor_stop

# command to start motor on port A at speed 20
start_motor = move_time(ports='a', power=50, time=5)
stop_motor = motor_stop(ports='abcd')
##(12, 0, 0, 0, 128, 0, 0, 164, 0, 1,  15, 75, 166, 0, 1)
#move_time(ports='ac', power=30, time=2)
#print start_motor
#stop_motor = '\x09\x00\x0F\x00\x00\x00\x00\xA3\x00\x0F\x00'

# command to stop motor on port A

# send commands to EV3 via bluetooth
with open('/dev/tty.EV3-SerialPort', 'w+', 0) as bt:
	bt.write(start_motor[0])
	print "writing"
	time.sleep(start_motor[1]) 
	bt.write(stop_motor)
	n = 0
	incoming =[]
	while n < 10:
		incoming.append(bt.read())
		time.sleep(1)
		n = n+1
	print incoming
'''
# command to start motor on port A at speed 20
start_motor = '\x0C\x00\x00\x00\x80\x00\x00\xA4\x00\x0F\x4B\xA6\x00\x0F'

# command to stop motor on port A
stop_motor = '\x09\x00\x0F\x00\x80\x00\x00\xA3\x00\x0F\x00'
# send commands to EV3 via bluetooth
with open('/dev/tty.EV3-SerialPort', 'w+', 0) as bt:
	bt.write(start_motor)
	#print start_motor 
	time.sleep(5) 
	bt.write(stop_motor) 
	#print stop_motor 
    
    #start motor for infintiy
    #wait time 
    #stop motor
    
    #from input, go through each line and find the command
 
textbox = "move_time(ports='cb',power=75,time=2)" #Code that the user will input
#for loop searching each line will go here
posS = textbox.index('(') + 1
posE = textbox.index(')')
command = textbox[posS:posE]
command = command.split(',');
commandType = textbox[0:posS-1]
print command
print commandType
commandS= list(command)
cmd=["","",""]
target = open("ev3.py", 'w')
target.write("import time \n")
if (commandType == "move_time"):
	#mybrick.motor_start(ports = 'ad', power = 20)
	cmd[0] = "mybrick.motor_start("+command[0]+","+command[1]+")"
	cmd[1] = "time.sleep("+command[2][command[2].index('=')+1:len(command[2])] +")"
	cmd[2] = "mybrick.motor_stop("+command[0]+")"
	target.write(cmd[0]+'\n'+cmd[1]+'\n'+cmd[2]+'\n')
	target.close()
	print cmd
	
#def move_time(ports, power, time):
	#A power 20
#print '\x0D\x00\x00\x00\x80\x00\x00\xA4\x00\x01\x81\x14\xA6\x00\x01'

print struct.unpack('7B','\x1D\x00\x00\x00\x80\x00\x00')
#target.close()
'''
