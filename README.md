# port-scanner
A simple multithreaded TCP port scanner built from scratch in Python. It scans the open port(s) of the given host, identify the services, and the print out the result.

## ⚠️DISCLAMER⚠️
This program is written for educational purpose and authorized testing only. Reminder : Only scan the system you have premission to scna or test. (E.g. your own machine "127.0.0.1", or dedicated practice target like "scanme.nmap.org"). Unauthorized scanning is illegal.

## WHAT DOES IT DO?
It first check for open TCP port within the given range of the given host, and then it maps out the service of that specific port and saves the details into a dictionary, it print out the results in a clean and readable table once the scanning is done. Scanning is fast because it scan every port concurrently.

## EXAMPLE

```
$ python port_scanner.py 127.0.0.1 4999 7001

Scanning 127.0.0.1 (port 4999-7001)...

PORT    STATE   SERVICE
5000    Open    unknown
7000    Open    unknown

Scan complete: 2 open port(s) found.
```

## FEATURES

-   TCP connect scanning by using Python sockets.
-   Concurrent scanning with 'ThreadPoolExecutor' (fast).
-   Common-service identification (port -> service name).
-   Clean tabular output.
-   Command-line interface via 'argparse' (with auto-generated '--help').

## HOW IT WORKS

-   Each port is tested with a socket's "connect_ex()" - if the function return a value '0', it means that the handshake succeed and port is open.
-   A short timeout stops dead ports for hanging too long.
-   A "ThreadPoolExecutor" runs many checks at once, so the time out overlap instead of stacking up, it's provide efficiency.
-   Open ports are matched with the well-known ports to label he likely service.

## WHY I BUILT IT THIS WAY

-   **From scratch, no nmap:** Implemented the socket logic and service loopup myself to understand how scanning actually work.
-   **Threading:** A sequential scan of 1000 ports could take pretty long time to finish due to connection timeout; but running them concurrently drops the time down to seconds.
-   **Hand-built service table:** tied to the well-known ports so the tool stay self-contained.

## HOW TO RUN IT

requiremnet(s):
-   Python 3 (Standard)

```
$ python port_scanner.py <host> <start_port> <end_port>
```

example:
```
$ python port_scanner.py 127.0.0.1 4999 7001
```

## WHAT I LEARNED

-   how TCP connections and the handshake work in code (socket, 'connect_ex').
-   concurrency can dramatically speeds up I/O-bound work like scanning.
-   What 'argparse' is, and how to build a command-line interface with it.

## LICENSE

MIT
