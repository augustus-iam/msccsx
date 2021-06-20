import socket
import socket
import struct
import binascii

def main():
    site = input("Enter site url(q to quit): ")

    try:
        ip = socket.gethostbyname(site)
        print("IP address: %s" % ip)
    except socket.error as err_msg:
        print("%s: %s" % (site, err_msg))
    main()


if __name__ == '__main__':
    main()
