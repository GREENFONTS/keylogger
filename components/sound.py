import sys
import sounddevice as sd

# recording audio
def sound(count):
    fs = 48000
    sd.default.samplerate = fs
    sd.default.channels = 2
    duration = count
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
    write("soundrecord.wav", fs, myrecording)

sys.modules[__name__] = sound