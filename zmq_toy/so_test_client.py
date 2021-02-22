import zmq
from zmq import ssh
import time
# import json
import struct

context = zmq.Context()
socket = context.socket(zmq.REQ)
ssh.tunnel_connection(socket, "tcp://127.0.0.1:5563", "psiori@192.168.50.31")
#socket.bind("tcp://127.0.0.1:5563")

requesId = 0
while True:
    request = "Message %d" %requesId
    print("Sending '%s'.." %request)
    socket.send_string(request)
    
    response = socket.recv()
    # decode bytes to string
    # data_string = response.decode('utf8')
    data_received = struct.unpack('dddd', response)
    # data_json = json.loads(data_string)
    print("Response data:", data_received)
    
    requesId += 1
    time.sleep(1)
