from faster_whisper import WhisperModel
import sounddevice
import scipy
import numpy as np


model = WhisperModel('base')

def record(duration=5, fs=16000):
    print("Listening.....")
    audio = sounddevice.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    
    sounddevice.wait()
    
    return audio, fs

def save_file(audio, fs, filename):
    audio = np.squeeze(audio)
    scipy.io.wavfile.write(filename, fs, audio)

def transcribe_audio():
    
    while True:
        audio, fs = record(duration=15)
        
        filename = "./new.wav"
        save_file(audio, fs, filename)
        segments, _ = model.transcribe(filename)
        print("📝 You said:", " ".join([segment.text for segment in segments]))
        # os.remove(filename)
        

if __name__ == "__main__":
    
    transcribe_audio()