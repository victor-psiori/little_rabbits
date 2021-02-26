import zmq
from zmq import ssh
import time
import struct

context = zmq.Context()
socket = context.socket(zmq.SUB)
ssh.tunnel_connection(socket, "tcp://127.0.0.1:5563", "psiori@192.168.50.31")
# socket.connect("tcp://127.0.0.1:5563")

topic_filter = "crane_status"
socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)
while True:
	resp = socket.recv()
	incoming = None
	try:
		incoming = struct.unpack('dddd', resp)
	except struct.error as err:
		# this is the topic received; ignore
		pass
	if incoming:
		print(f"data received: {incoming}")
	time.sleep(0.1)