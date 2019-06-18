import paramiko
from paramiko import SSHClient
from scp import SCPClient
k = paramiko.RSAKey.from_private_key_file("/throwAway.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "connecting"
c.connect( hostname = "ec2-18-233-150-46.compute-1.amazonaws.com", username = "ubuntu", pkey = k )
print "connected"
with SCPClient(c.get_transport()) as scp:
        scp.put('my_file.txt', '/home/ubuntu/my_file.txt') # Copy my_file.txt to the server
