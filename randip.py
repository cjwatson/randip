#RandIP 0.5#
#Random IP Generator with Socket, SSH, and Telnet support.#
import socket, os, time, telnetlib, datetime, paramiko
from random import randint

a = []
b = []
c = []
d = []
e = []
f = []
g = []
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
	fp.write('\n')
	fp.write('Failed Telnet Conncections(')
	fp.write(str(e))
	fp.write(')')
	fp.write('\n')
	fp.write('SSH Information(')
	fp.write(str(f))
	fp.write(')')
	fp.write('\n')
	fp.write('Failed SSH(')
	fp.write(str(g))
	fp.write(')')
	fp.close()
	s.close()
		
def randip():
	while True:
		yield ".".join(str(randint(1, 255)) for i in range(int(4)))

log = datetime.datetime.now()
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
			except socket.error:
				print(socket.error, 'Error Signing in or Telnet not accesable', address)
				print '\n'
				e.append(address)
				pass
			except EOFError:
				print(EOFError, address)
				pass
			except KeyboardInterrupt:
				WriteLog()
				break
			try:
				print('Starting SSH Attempt on %s' % address)
				SSH = paramiko.SSHClient()
				SSH.connect(address, username='admin', password='admin')
				stdin, stdout, stderr = client.exec_command('ls')
				for line in stdout:
					print '... ' + line.strip('\n')
				client.close()
				f.append(address)
			except paramiko.ssh_exception.SSHException:
				print(paramiko.ssh_exception.SSHException, 'SSH Could not connect', address)
				g.append(address)
				pass
			except paramiko.ssh_exception.AuthenticationException:
				print(paramiko.ssh_exception.AuthenticationException, 'Error logging into SSH' ,  address)
				g.append(address)
				pass
			except KeyboardInterrupt:
				WriteLog()
				break
		except socket.timeout:
			print(socket.timeout, '%s timeout' % address)
			print '\n'
			a.append(address)
			pass
		except socket.herror:
			print(socket.herror, 'Error getting host by address on %s' % address)
			print '\n'
			a.append(address)
			pass
		except socket.error:
			print(socket.error, 'Failed to connect to %s' % address)
			print '\n'
			a.append(address)
			pass
	except KeyboardInterrupt:
		WriteLog()
		break
