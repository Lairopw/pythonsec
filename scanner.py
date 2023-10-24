import socket

clientudp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #AF_INT = ipv4 SOCK_DGRAM for udp
clientudp.settimeout(0.01)

host=socket.gethostname()

open_ports_tcp = []
open_ports_udp = []

def scan_tcp_ports(host, ports):
    clienttcp = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    clienttcp.settimeout(0.01)
    try:
        clienttcp.connect((host, ports))
        open_ports_tcp.append(port)
        print("port TCP {} : ouvert".format(ports))
        clienttcp.detach()
    except socket.timeout:
        pass
    except ConnectionError:
        pass

def scan_udp_ports(host, ports):
    open_ports_udp.clear()
    bonjour=b"message"
    try:
        clientudp.sendto(bonjour, (host, ports))
        data, addr = clientudp.recvfrom(1024)
        open_ports_udp.append(ports)
        print("port UDP {} : ouvert".format(ports))
    except :
        pass

print("Scanning des ports :")
for port in range(1,1025):
    scan_tcp_ports(host, port)
    scan_udp_ports(host, port)

