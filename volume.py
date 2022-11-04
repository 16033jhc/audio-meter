# Import libraries
import pyaudio
import audioop
import time
from tkinter import * 
from tkinter import messagebox

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

# Main function
def main():
    # Capture audio data
    for i in range(0, int(samplerate / buffer_size)):
        data = stream.read(buffer_size)
        vol = audioop.rms(data, 1)
        time.sleep(2)

        # Write captured data to text file
        f = open("sound_history.txt", "a")
        f.write(f"Volume (in relative DB): {vol}\n")
        f.close()

t_end = time.time() + 60 * 0.001

while time.time() < t_end:
    main()

# Create object 
root = Tk()

# Adjust size 
root.geometry("300x200")

messagebox.showinfo("Exiting...", "Thank you!")

# Kill PyAudio streams
stream.stop_stream()
stream.close()
p.terminate()

exit
