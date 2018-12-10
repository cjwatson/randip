# RandIP 1.2.9-snap (Python)
RandIP is a python scripts that generates random IP address's and uses sockets to test whether the connection is valid or not with the additional test of logging in to Telnet and SSH with the default logins.
<br>
[![Snap Status](https://build.snapcraft.io/badge/blmvxer/randip.svg)](https://build.snapcraft.io/user/blmvxer/randip)
<br>
<b>:Installation:</b>
<br>
snap install randip
<br>
<b>Running nim version from snap</b>
<br>
randip -nim
<br>
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
  CVE: 2018-15473
<br>
$HTML Screenshot of active hosts
<br>
Service detector for SSH and Telnet.
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

<b>#Changelog</b>
<br>
10/8/2018:RandIP 1.2.4
<br>
Bug fixes within SSH enumeration exploits
<br>
added false-positive tests on requests.ConnectionError
<br>
<br>
10/7/18:RandIP 1.2.3
<br>
Added SSH and Telnet Timeouts to prevent blocking
<br>
removed ShellShock exploit(no longer valid)
<br>
<br>
10/6/18:RandIP 1.2.1
<br>
SSH Enumerations now work in tandem
<br>
Typos fixed
<br>
Telnet crash fixed
<br>
AttrubuteError and TypeError on socket.herror fixed.
<br>
<br>
10/6/18:RandIP 1.2
<br>
added CVE: 2018-15473
<br>
added testing telnet and ssh on socket.herror
<br>

<br>

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
<br>
<br>
<br>
The Nim port is a basic port which may be implemented for standard binary releases...This is not part of the major roadmap
