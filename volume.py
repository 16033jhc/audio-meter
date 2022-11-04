# Import libraries
import pyaudio
import audioop
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

def main():
    for i in range(0, int(samplerate / buffer_size)):
        data = stream.read(buffer_size)
        vol = audioop.rms(data, 1)
        time.sleep(2)

        print(f"Volume (in relative DB): {vol}")

while True:
    main()
    
