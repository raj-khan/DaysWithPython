import sounddevice
from scipy.io.wavfile import write

fps = 44100
duration = 10
print("Recording Start, Say Something....")
recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels=2)
sounddevice.wait()
print("Recorded!")

write("audio-.wav", fps, recording)