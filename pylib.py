#from pylib import ports_to_int
#ports_to_int('abcd')
import struct
import time
def ports_to_int(ports):
	sum = 0;
	for i in range(0, len(ports)):
		port = ports[i]
		if port == 'a':
			sum = sum + 1
		elif port == 'b':
			sum = sum + 2
		elif port == 'c':
			sum = sum + 4
		elif port == 'd':
			sum = sum + 8
		else:
			sum = sum
	return sum

# self.stops = {'brake': 1, 'coast': 0}
def move_time(ports, power, time):
#move_time(ports='cb', power=75, time=5)
	ports = ports_to_int(ports)
	print ports
	print power
	print time
	print chr(ports)
	powerH = struct.pack('1B',power)
	portsH= struct.pack('1B',ports)
	comm_0 = '\x0C\x00\x00\x00\x00\x00\x00'
	comm_1 = '\xA4\x00'+portsH+ powerH +'\xA6\x00'+portsH
	comm = comm_0  + comm_1
	#command = [comm,"time.sleep(",time,")",'\x09\x00\x0F\x00\x80\x00\x00\xA3\x00\x0F\x00']
	command = [comm,time]
	return command
	
def motor_stop(ports):
	port = ports_to_int(ports)
	portsH =struct.pack('1B',port)
	l0 = struct.pack('1B',0)
	l1 = struct.pack('1B',1)
	comm_0 = '\x09\x00\x01\x00\x00\x00\x00'
	comm_1 = '\xA3' + l0 + portsH + l1
	command = comm_0 + comm_1
	print struct.unpack('11B', command)
	return command
	
#def success_byte:
	
	'''
	varis = command
	print len(varis)
	varis = struct.unpack("15B", varis)
	print varis
	print struct.unpack('1B', chr(ports))
	print struct.unpack('3B', hex(ports))
	print struct.pack('B', 65)
	print len(struct.pack('B', ports))
	print len(chr(ports))
	print len('\x09')
	# command to stop motor on port A
	stop_motor = '\x09\x00\x0F\x00\x80\x00\x00\xA3\x00\x0F\x00'
'''
	#(12, 0, 0, 0, 128, 0, 0, 164, 0, 6, 120, 48, 70, 75, 166, 0, 6)  Mine
	#(12, 0, 0, 0, 128, 0, 0, 164, 0, 1,  15, 75, 166, 0, 1)   Updated
	#(13, 0, 0, 0, 128, 0, 0, 164, 0, 6, 129, 75, 166, 0, 6)   His

	#RETURN BYTES
	#03 00 00 00 02   Start Move
	#03 00 0F 00 02   End Move
	
'''
	def move_time(ports, power, time):
	ports_to_int(ports)
	comm_0 = '\x0C\x00\x00\x00\x80\x00\x00'
	comm_1 = '\xA4\x00\x0F\x4B\xA6\x00\x0F'

	# command to stop motor on port A
	stop_motor = '\x09\x00\x0F\x00\x80\x00\x00\xA3\x00\x0F\x00'
	'''
