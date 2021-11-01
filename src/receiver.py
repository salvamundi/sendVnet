import socket
import os
import tqdm
from connect import *

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

opt_s = ha.handle_args()

def receiver(s_ip, s_pt):
    s_ip = opt_s.receiver_ip #ip could be 0.0.0.0 so that way if our machines is i.e 192.168.0.4 and 10.0.0.5 at the same time, we will be able to listen at all the IPv4 addresses, not only with the given one
    s_pt = opt_s.receiver_port

    socket.bind((s_ip, s_pt)) #bind server socket to listen at the specified ip:port
    socket.listen(5) #allow to listen at most 5 incoming unaccepted connections

    print(f"[*] Listening on: {s_ip}:{s_pt}")

    while True:
        #receive file info
        #use client_socket because data is sent from client since we are RECEIVING
        try:
            client_socket, address = socket.accept()
            print(f"[+] {address} connected!")
            received = client_socket.recv(BUFFER_SIZE).decode()
        except OSError as er_msg:
            print("[-] Unable to receive file")
        else:
            filename, filesize = received.split(SEPARATOR)
            filename = os.path.basename(filename) #removing absolute path if any
            filesize = int(filesize)

            progressBar = tqdm.tqdm(range(filesize), f"[*] Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

            with open(filename, "wb") as received_file:
                while True:
                    read_bytes = client_socket.recv(BUFFER_SIZE)
                    if not read_bytes:
                        print("[+] File received successfully")
                        break
                    received_file.write(read_bytes)
                    progressBar.update(len(read_bytes))

            client_socket.close()
            socket.close()