import socket

from vidstream import AudioReceiver

from vidstream import AudioSender

import threading

my_ip = socket.gethostbyname(socket.gethostname())

receiver_port = '9999'

sender_port = '5555'

receiver = AudioReceiver(my_ip, receiver_port)

sender = AudioSender(my_ip, receiver_port)

receiver_thread = threading.Thread(target=receiver.start_server)

sender_thread = threading.Thread(target=sender.start_stream)

receiver_thread.start()

sender_thread.start()