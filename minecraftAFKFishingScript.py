import pyaudio as audio
import pyautogui as gui
import numpy as np
import audioop
import time

# Debug mode to test script

DEBUG = True

# Volume threshold

THRESHOLD = 70

# Set up audio input stream
CHUNK = 1024
FORMAT = audio.paInt16
CHANNELS = 1
RATE = 4000

pa = audio.PyAudio()
stream = pa.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK)

def main():
    print("Running...")

    while True:
        data = stream.read(CHUNK)
        
        rms = audioop.rms(data, 2)

        if DEBUG:
            print(round(rms))

        if rms >= THRESHOLD:
            rightClick()

def rightClick():
    gui.rightClick()
    time.sleep(0.1)
    gui.rightClick()
    
main()
