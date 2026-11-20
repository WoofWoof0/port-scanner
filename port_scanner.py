import socket

#A function that scan the given port on that specific address and check weather it is open.
def scan_port(host, port):
    #AF_INET = uses IPv4 addresses
    #SOCK_STREAM = use TCP (the reliable protocol)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) 
    #set 1 second so the dead port won't let the program hang too long.

    result = s.connect_ex((host, port))
    #close down the socket.
    s.close()

    if result == 0:
        return "Open"
    else:
        return "Closed"

#A function that scan the whole range of ports of the host from start to end.
def scan_range(host, start, end):
    open_list = []

    for i in range(start,end+1):
        result = scan_port(host,i)
        if result == "Open":
            open_list.append(i)

    return open_list

print(scan_range("127.0.0.1",8000,8000))