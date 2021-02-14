import zmq
from zmq import ssh

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)

# Define subscription and messages with prefix to accept.
#sock.setsockopt_string(zmq.SUBSCRIBE, "lidar_calibration")
sock.setsockopt_string(zmq.SUBSCRIBE, "")
#sock.connect("tcp://127.0.0.1:5685")
ssh.tunnel_connection(sock, "tcp://127.0.0.1:5685", "psiori@192.168.50.31")

while True:
    message= sock.recv()
    # decode = message.decode()
    # message= sock.recv_string()
    print (message)
