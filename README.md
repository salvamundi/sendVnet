# sendVnet

This app lets you share files over your network. You don't have to plug your USB devices to move files from one computer to another.
All you need to know is your target ip and port that it's listening on, file name you want to send and that's pretty much it.
It shares the files over TCP connection.

At this point I do not recommend using this to share files that contains fragile data because I did nothing to secure the information except using the encode() function.

Program recognizes two types of users; sender and receiver.
Sender needs to provide ip of the host, port the host is listening on and file name.
Receiver on the other hand needs to specify the ip and port to listening to only.

Syntax of the program if sender:   python3 sendVnet.py -i/--ipaddress <ip_address> -p/--port <port> -f/--fname <filename> -r/--role sender
  
Syntax of the program if receiver: python3 sendVnet.py -i/--ipaddress <ip_address> -p/--port <port> -r/--role receiver

This program uses tqdm, optparse, socket, os, platform libraries
I'd rather recommend to install those before using this. I did not include the requirements.txt file. I may do it later but I don't promise.
