import sendVnet
import handle_args as ha
import os #to get file  size
import tqdm

def sender(r_ip, r_pt, file_name, role):
    opt_s = ha.handle_args()
    r_ip = opt_s.receiver_ip
    r_pt = opt_s.receiver_pt
    file_name = opt_s.file_name
    role = opt_s.role

    file_name_size = os.path.getsize(file_name) #gets file size in bytes, thanks to that we can make nice looking progress bars
