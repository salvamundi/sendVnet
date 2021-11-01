###Shotouts to the author of the source code on this site: https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
#I'm the author of the sender() and receiver() function but I used his algorithm for sending/receiving files in Python
#which this functions contain. I decided to add a little more functionality to this such as parsing arguments,
#handling with those values and showing list of availables ip's, showing yours either so you can see it all clearer.

import handle_args as ha
import sender
import receiver
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
                                                                               





""")

opt = ha.handle_args()
if opt.role == "sender":
    sender(opt.receiver_ip, opt.receiver_port, opt.file_name)
elif opt.role == "receiver":
    receiver()
else:
    print("[!] Invalid argument value (sender/receiver)")
