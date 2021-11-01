#Handling values from users for arguments

import optparse

#returns options (values from users) for arguments
def handle_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ipaddress", dest="receiver_ip", help="Set the IP Address for the sender/receiver")
    parser.add_option("-p", "--port", dest="receiver_port", help="Set the port for the sender/receiver")
    parser.add_option("-f", "--fname", dest="file_name", help="Provide full Path or filename if in the same folder where you have installed this app")
    parser.add_option("-r", "--role", dest="role", help="Describe if you are sending or receiving file (sender/receiver)")
    parser.add_option("-d", "--dir", dest="ddir", help="Specify the path. This option isn't necessary")
    options, arguments = parser.parse_args() #ta funkcja zwraca wartosci ktore wpisal user dla -i, -p itd.

    if options.receiver_ip is None:
        parser.error("[!] Set the IP Address for the sender/receiver!")
    elif options.receiver_port is None:
        parser.error("[!] Set the port for the sender/receiver!")
    elif options.file_name is None:
        if options.role == "receiver":
            pass
        else:
            parser.error("[!] Don't forget about file name!")  # if role is sender*, only sender & receiver are meaningful values for this (roll) argument
    elif options.role is None:
        parser.error("[!] Don't forget about specifying if you are sending the file or receiving it")
    elif options.ddir is None:
        pass

    return options
