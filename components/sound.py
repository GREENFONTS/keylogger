import sounddevice as sd
from scipy.io.wavfile import write

# recording audio
def sound(count):
    fs = 48000
    sd.default.samplerate = fs
    sd.default.channels = 2
    duration = count
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
    write("soundrecord.wav", fs, myrecording)
