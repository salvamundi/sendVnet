###Shotouts to the author of the source code on this site: https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
#I'm the author of the sender() and receiver() function but I used his algorithm for sending/receiving files in Python
#which this functions contain. I decided to add a little more functionality to this such as parsing arguments,
#handling with those values and showing list of availables ip's, showing yours either so you can see it all clearer.

from sender import *
from receiver import *
import sys_help as sh

sh.clear()
print("""
@@@@@@   @@@@@@@@  @@@  @@@  @@@@@@@   @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@  
@@@@@@@   @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@  @@@  @@@@ @@@  @@@@@@@@  @@@@@@@  
!@@       @@!       @@!@!@@@  @@!  @@@  @@!  @@@  @@!@!@@@  @@!         @@!    
!@!       !@!       !@!!@!@!  !@!  @!@  !@!  @!@  !@!!@!@!  !@!         !@!    
!!@@!!    @!!!:!    @!@ !!@!  @!@  !@!  @!@  !@!  @!@ !!@!  @!!!:!      @!!    
 !!@!!!   !!!!!:    !@!  !!!  !@!  !!!  !@!  !!!  !@!  !!!  !!!!!:      !!!    
     !:!  !!:       !!:  !!!  !!:  !!!  :!:  !!:  !!:  !!!  !!:         !!:    
    !:!   :!:       :!:  !:!  :!:  !:!   ::!!:!   :!:  !:!  :!:         :!:    
:::: ::    :: ::::   ::   ::   :::: ::    ::::     ::   ::   :: ::::     ::    
:: : :    : :: ::   ::    :   :: :  :      :      ::    :   : :: ::      :     
                                                                            v1.7.1
""")

opt = ha.handle_args()
if opt.role == "sender":
    if opt.ddir is not None:
        exit("[!] FUNC_ERR: Action not allowed!")
    sender(opt.receiver_ip, opt.receiver_port, opt.file_name)
elif opt.role == "receiver":
    receiver(opt.receiver_ip, opt.receiver_port)
else:
    print("[!] Invalid argument value (sender/receiver)")
