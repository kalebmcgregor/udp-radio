import pyaudio
import time
import socket


class sender:
    def __init__(self, width, channels, rate, ip, port):
        
        if width is None:
            width = 2
        if channels is None:
            channels = 2
        if rate is None:
            rate = 44100
        if udp_ip is None:
            udp_ip = "127.0.0.1"
        if UDP_PORT is None:
            udp_port = 5005
        
        self.width = width
        self.channels = channels
        self.rate = rate
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.p = pyaudio.PyAudio()
	stream = p.open(format=self.p.get_format_from_width(self.width),
			channels=self.channels,
			rate=self.rate,
			input=False,
			output=True,
			stream_callback=callback)
	sock = socket.socket(socket.AF_INET,
			     socket.SOCK_DGRAM)
            
    def callback(in_data, frame_count, time_info, flag):
	data, addr = sock.recvfrom(10000)
	return data, pyaudio.paContinue
    

    sock.bind((UDP_IP, UDP_PORT))

    stream.start_stream()

    while stream.is_active():
	time.sleep(0.1)

    stream.stop_stream()
    stream.close()

    p.terminate()
 

class receiver:
    
    def callback(in_data, frame_count, time_info, flag):
	sock.sendto(in_data, (UDP_IP, UDP_PORT))
	return in_data, pyaudio.paContinue

    WIDTH = 2
    CHANNELS = 2
    RATE = 44100

    p = pyaudio.PyAudio()

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = "Hello, World!"

    print("UDP target IP:", UDP_IP)
    print("UDP target port:", UDP_PORT)
    print("message:", MESSAGE)

    sock = socket.socket(socket.AF_INET,
			 socket.SOCK_DGRAM)

    stream = p.open(format=p.get_format_from_width(WIDTH),
		    channels=CHANNELS,
		    rate=RATE,
		    input=True,
		    output=False,
		    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
	time.sleep(0.1)

    stream.stop_stream()
    stream.close()

    p.terminate()

