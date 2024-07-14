import pyaudio
import numpy as np
from time import sleep

def start_voice_client():
    print("Starting voice client")
    while True:
        CHUNK = 8192
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        volume = np.abs(data).mean()
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        with open("mic_volume.txt", "w") as f:
            if volume == '':
                f.write("0")
            else:
                f.write(str(int(volume)))
            f.close()
        
        sleep(0.01)