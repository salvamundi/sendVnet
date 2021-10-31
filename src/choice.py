import handle_args as ha
import sender

opt = ha.handle_args()
if opt.role == "sender":
    sender(opt.receiver_ip, opt.receiver_port, opt.file_name, opt.role)
elif opt.role == "receiver":
    pass
else:
    print("[!] Invalid argument value")
    exit()
