import sys
import socket

print("CLI Application Started")
print(sys.argv)
print(len(sys.argv))

## Parameter Handling

args = sys.argv
numArgs = len(sys.argv)

if numArgs < 5:
    print("Invalid parameters. Make sure you specify all parameters in the following format. \n  ttweetcl  -u  <ServerIP>  <ServerPort> 'message'")
    exit()

params = {"ip": args[2], "port": args[3], "message": args[4]}

if len(params["message"]) > 150:
    print("Cannot proceed. Message exceeds 150 characters.") ## not allow empty msg
    exit()


## Open socket for communication

##conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##conn.connect((params["ip"], params["port"]))









