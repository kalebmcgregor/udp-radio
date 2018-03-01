import pyaudio
import time
import socket


class sender:
    def __init__(self, **kwargs):
        if not 'width' in kwargs:
            width = 2
        if not 'channels' in kwargs:
            channels = 2
        if not 'rate' in kwargs:
            rate = 44100
        if not 'udp_ip' in kwargs:
            udp_ip = "127.0.0.1"
        if not 'udp_port' in kwargs:
            udp_port = 5005
        
        self.width = width
        self.channels = channels
        self.rate = rate
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.p = pyaudio.PyAudio()
        stream = self.p.open(format=self.p.get_format_from_width(self.width), 
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
    
    def start():
        sock.bind((UDP_IP, UDP_PORT))
        stream.start_stream()
        while stream.is_active():
            time.sleep(0.1)

    def stop():
        stream.stop_stream()
        stream.close()
        p.terminate()
 

class receiver:
    def __init__(self, **kwargs):
        if not 'width' in kwargs:
            width = 2
        if not 'channels' in kwargs:
            channels = 2
        if not 'rate' in kwargs:
            rate = 44100
        if not 'udp_ip' in kwargs:
            udp_ip = "127.0.0.1"
        if not 'udp_port' in kwargs:
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
                        input=True,
                        output=False,
                        stream_callback=callback)
        
        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
    
    def callback(in_data, frame_count, time_info, flag):
        sock.sendto(in_data, (UDP_IP, UDP_PORT))
        return in_data, pyaudio.paContinue

    def start():
        stream.start_stream()
        while stream.is_active():
            time.sleep(0.1)

    def stop():
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
     walkie_sender = sender()
     walkie_receiver = receiver()
     sender.start
     sender.stop
     receiver.start
     receiver.stop
