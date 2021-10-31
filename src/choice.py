import handle_args as ha

args = ha.handle_args()
if args.role == "sender":
    x = 1
elif args.role == "receiver":
    x = 1
else:
    print("[!] Invalid argument value")
    exit()

