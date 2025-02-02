from vosk import Model, KaldiRecognizer
import pyaudio

es = "models/vosk-model-small-es-0.42"

model = Model(es)
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text[14:-3])

