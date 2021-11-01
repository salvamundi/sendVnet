import socket
import handle_args as ha

opt_s = ha.handle_args()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def connect_to(r_ip, r_pt):
    r_ip = opt_s.receiver_ip
    r_pt = opt_s.receiver_port
    try:
        print(f"[*] Connecting to: {r_ip}:{r_pt}")
        socket.connect((r_ip, r_pt))
    except socket.error as er_msg:
        print(f"[-] Unable to connect {er_msg}")

    print(f"[+] Connection established")