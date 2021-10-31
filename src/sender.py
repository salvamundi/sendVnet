import choice
import handle_args as ha

def sender(r_ip, r_pt, file_name, role):
    opt_s = ha.handle_args()
    r_ip = opt_s.receiver_ip
    r_pt = opt_s.receiver_pt
    file_name = opt_s.file_name
    fole = opt_s.role

