# Import libraries
import pyaudio
import audioop
import numpy as np
from math import log10
import time

# Initialise pyaudio and open audio input stream
p = pyaudio.PyAudio()
print(p.get_default_input_device_info())

buffer_size = 1024
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 44100

stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size)

while True:
    for i in range(0, int(samplerate / buffer_size)):
        data = stream.read(buffer_size)
        rms = audioop.rms(data, 2)

    print(rms)
    db = 20 * log10(rms)
    print(f"RMS: {rms} DB: {db}")

stream.stop_stream()
stream.close()
p.terminate()
