import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

#global service dictionary
service = {21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 3389: "RDP"}

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
            check = service.get(i,"unknown")
            open_list.append((i,check))

    return open_list

#A function that print out the result into more cleaner and more readable text.
def print_result(host, start, end, open_list):
    print(f"Scanning {host} (port {start}-{end})...\n")

    if open_list:
        print("PORT\tSTATE\tSERVICE")
        for port, svc in open_list:
            print(f"{port}\tOpen\t{svc}")
        
        print(f"\nScan complete: {len(open_list)} open port(s) found.")
    else:
        print("No open port found.")

#A function that package one port's work into a tiny "job" function.
def scan_one(host, port):
    if scan_port(host,port) == "Open":
        return (port, service.get(port, "unknown"))

def scan_range(host, start, end):
    open_list = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        #hand one job per port to the pool.
        futures = [executor.submit(scan_one, host, port) for port in range(start, end+1)]

        #collect the answers, keep the open ones
        for f in futures:
            result = f.result()
            if result is not None:
                open_list.append(result)

    return open_list

host, start, end = "127.0.0.1", 1, 9000

# print(scan_range(host,start,end))
# print_result(host, start, end, scan_range(host, start, end))
# print(scan_range(host, start, end))

parser = argparse.ArgumentParser(description="A Simple TCP port scanner.")
parser.add_argument("host", help="Host or IP to scan.")
parser.add_argument("start", type=int, help="Start port")
parser.add_argument("end", type=int, help="End port")
args = parser.parse_args()

results = scan_range(args.host, args.start, args.end)
print_result(args.host, args.start, args.end, results)