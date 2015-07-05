# RandIP 0.5
RandIP series of python scripts that generates random IP address and uses sockets to test whether the connection is valid or not with the additional test of logging in to telnet with the default logins.

Added functionality is common and the script may change from day to day depending on development.



Error Handling Informtion:Socket.timeout and Socket.error usually means the samething(That the host is unreachable) while Socket.herror means that the host is reachable but doesn't contain an active website(404 errors etc)

By default the timeout is 1.8 seconds, this can be modified based on your connection speed and latency but for most connections this should be an acceptable time to determine false and true connections.

Dependencies(paramiko)
<br>
(Linux, Unix, OS X)sudo pip install paramiko or (Windows)python -m pip install paramiko
