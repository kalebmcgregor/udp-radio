import pyaudio
import time
import socket


class Sender:
    def __init__(self, **kwargs):
        if not 'width' in kwargs:
            self.width = 2
        if not 'channels' in kwargs:
            self.channels = 2
        if not 'rate' in kwargs:
            self.rate = 44100
        if not 'udp_ip' in kwargs:
            self.udp_ip = "127.0.0.1"
        if not 'udp_port' in kwargs:
            self.udp_port = 5005

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.width),
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=False,
                                  output=True,
                                  stream_callback=self.callback)
        
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
    
    def callback(self, in_data, frame_count, time_info, flag):
        data, addr = self.sock.recvfrom(10000)
        return data, pyaudio.paContinue
    
    def start(self):
        self.sock.bind((self.udp_ip, self.udp_port))
        self.stream.start_stream()
        while self.stream.is_active():
            time.sleep(0.1)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
 

class Receiver:
    def __init__(self, **kwargs):
        if not 'width' in kwargs:
            self.width = 2
        if not 'channels' in kwargs:
            self.channels = 2
        if not 'rate' in kwargs:
            self.rate = 44100
        if not 'udp_ip' in kwargs:
            self.udp_ip = "127.0.0.1"
        if not 'udp_port' in kwargs:
            self.udp_port = 5005

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.width),
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  output=False,
                                  stream_callback=self.callback)
        
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
    
    def callback(self, in_data, frame_count, time_info, flag):
        self.sock.sendto(in_data, (self.udp_ip, self.udp_port))
        return in_data, pyaudio.paContinue

    def start(self):
        self.stream.start_stream()
        while self.stream.is_active():
            print("In loop!")
            time.sleep(0.1)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

if __name__ == "__main__":
    walkie_sender = Sender()
    walkie_receiver = Receiver()
    walkie_sender.start()
    walkie_receiver.start()
