import os #to get file  size
import tqdm
from connect import *

opt_s = ha.handle_args()

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

#sends the file to the specified receiver
def sender(r_ip, r_pt, file_name):

    r_ip = opt_s.receiver_ip
    r_pt = opt_s.receiver_port
    file_name = opt_s.file_name

    connect_to(r_ip, int(r_pt))

    file_name_size = os.path.getsize(file_name) #gets file size in bytes, thanks to that we can make nice looking progress bars

    socket.send(f"{file_name}{SEPARATOR}{file_name_size}".encode()) #encode default by utf-8

    try:
        opened_file = open(file_name, "rb") #rb stands for read binary, we open the file as a bin to read chunks of 4KB data, send them using sendall() and update progress bar and close socket until it gets done
    except OSError as OE_msg:
        print(f"[-] Could not open neither read the file: {OE_msg}")
        exit()
    else:
        progressBar = tqdm.tqdm(range(file_name_size), f"[*] Sending {file_name}", unit="B", unit_scale=True,
                                unit_divisor=1024)

        with opened_file:
            try:
                while True:
                    read_bytes = opened_file.read(BUFFER_SIZE) #constantly reads chunk of data from file
                    if not read_bytes: #checking if the bytes haven't ended up
                        break #if so, file transmitting is done, no more need to read
                    socket.sendall(read_bytes)
                    progressBar.update(len(read_bytes))
            except InterruptedError as IE_msg:
                print(f"[-] Unable to send a file: {IE_msg}")
            else:
                print("[+] File sent successfully")

        socket.close()

