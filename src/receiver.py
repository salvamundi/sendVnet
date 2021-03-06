import os
import tqdm
from connect import *

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

opt_s = ha.handle_args()

def receiver(s_ip, s_pt, s_ph):
    s_ip = opt_s.receiver_ip #ip could be 0.0.0.0 so that way if our machine is i.e 192.168.0.4 and 10.0.0.5 at the same time, we will be able to listen at all those addresses, not only with the given one
    s_pt = opt_s.receiver_port
    s_ph = opt_s.ddir

    socket.bind((s_ip, int(s_pt))) #bind server socket to listen at the specified ip:port
    socket.listen(5) #allow to listen at most 5 incoming unaccepted connections

    print(f"[*] Listening on: {s_ip}:{s_pt}")

    #receive file info
    #use client_socket because data is sent from client since we are RECEIVING
    try:
        client_socket, address = socket.accept()
        print(f"[+] {address[0]}:{address[1]} connected!")
        received = client_socket.recv(BUFFER_SIZE).decode()
    except OSError as OE_msg:
        print("[-] May be connected but unable to receive file")
        print(f"[*] Error: {OE_msg}")
    else:
        filename, filesize = received.split(SEPARATOR)
        #if s_ph is not None:
            #filename = os.path.basename(s_ph + filename)
        #else:
        #i decided to cut this off since it's not working properly
        #I'm checking now if this is the reason why receiver is getting file with full path provided by sender if he sends the file
        #not placed in the same directory as sendVnet.py
        filename = os.path.basename(filename) #removing absolute path if any

        filesize = int(filesize)
        progressBar = tqdm.tqdm(range(filesize), f"[*] Receiving {filename}", unit="B", unit_scale=True,
                                unit_divisor=1024) #filename doesn't work for some reason

        with open(filename, "wb") as received_file:
            try:
                while True:
                    read_bytes = client_socket.recv(BUFFER_SIZE)
                    if not read_bytes:
                        break
                    received_file.write(read_bytes)
                    progressBar.update(len(read_bytes))
            except InterruptedError as IE_msg:
                 print(f"[-] Failed to receive data: {IE_msg}")
            else:
                 print("[+] File received successfully")

        client_socket.close()
        socket.close()
