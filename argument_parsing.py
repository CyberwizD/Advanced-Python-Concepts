# Usage : python3 argument_parsing.py <FILENAME> <MESSAGE>

import sys
import getopt
import socket

'''
# sys.argv[0] # @index 0 - python <FILENAME>
filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as file:
    file.write(message)
'''

# Trial
def func(*args, **kwargs):
    print(args[0], args[1], kwargs['kw1'], kwargs['kw2'])


func('Ar', 'gu', kw1='me', kw2='nt')


# Usage: python3 argument_parsing.py -h localhost -p <PORT>

host = '127.0.0.1'
port = 234


def port_scan(host_, max_port):
    print(f"Scanning port 1-{max_port} on {host_}...")

    for port_ in range(1, int(max_port) + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Timeout for the connection attempt

        try:
            scan_result = sock.connect_ex((host, int(port_)))  # connect_ex() returns an error indicator
            if scan_result == 0:
                print(f"Port {port_} is open!")
            else:
                print(f"Port {port_} is closed.")

        except socket.error as err:
            print(f"Error scanning port {port_}: {err}")

        finally:
            sock.close()


try:
    opts, args = getopt.getopt(sys.argv[1:], "h:p:", ['host=', 'port='])

    for opt, arg in opts:
        if opt in ('-h', '--host'):
            host = arg
        elif opt in ('-p', '--port'):
            port = arg

    port_scan(host, port)

except getopt.GetoptError as e:
    print(str(e))
    print("Usage: python3 argument_parsing.py -h <HOST> -p <PORT>")
