# RandIP 0.9.4
RandIP is a python scripts that generates random IP address's and uses sockets to test whether the connection is valid or not with the additional test of logging in to Telnet and SSH with the default logins.

<b>:Features:</b>
<br>
$Random IP generation testing
<br>
$telnet login attempt
<br>
$ssh login attempt
<br>
  CVE: 2016-6210
<br>
$HTML Screenshot of active hosts
<br>
$Easy to read logging
<br>
$Additional logging for HTML Screenshots
<br>
$Zip creation for logs and hosts.
<br>
$Tor socket connection

Added functionality is common and the script may change from day to day depending on development.
<br>

#Changelog
Empty
<br>
#Planned Features
Features for 1.0
<br>
Adding GUI.

<br>
![alt tag](http://i.imgur.com/LuPjuDf.png)

<br>

Error Handling Informtion:
Socket.timeout and Socket.error usually means the samething(That the host is unreachable) while Socket.herror allows us to test for common false-positives in which most cases on a false-positive succesfully running through both exceptions would indicate other functionality than http/https. At which you could use Nmap to define the server found(Not implemented into the script due to time constraints of detecting active ssh and telnet connections with default logins).
<br>

By default the timeout is 1.8 seconds, this can be modified based on your connection speed and latency but for most connections this should be an acceptable time to determine false and true connections.
<br>

Dependencies(paramiko, requests, stem)
<br>

(Linux, Unix, OS X)sudo pip install paramiko or (Windows)python -m pip install paramiko
<br>

<br>

This script runs universally on all platforms that support Python 2.7 and Paramiko module(for SSH).
