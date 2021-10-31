###Shotouts to the author of the source code on this site: https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
#I'm the author of the sender() function but I used his algorithm for sending/receiving files in Python
#which this function contains. I decided to add a little more functionality to this such as parsing arguments,
#handling with those values and showing list of availables ip's, showing yours either so you can see it all clearer.

import handle_args as ha
import sender
import sys_help as sh

sh.clear()

opt = ha.handle_args()
if opt.role == "sender":
    sender(opt.receiver_ip, opt.receiver_port, opt.file_name, opt.role)
elif opt.role == "receiver":
    pass
else:
    print("[!] Invalid argument value (sender/receiver)")
