import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from PIL import Image

def GenWavF():
    spf = wave.open("./output/combined_signal.wav", "r")

    # Extract Raw Audio from Wav File
    signal = spf.readframes(1000)
    signal = np.fromstring(signal, "int16")

    plt.clf()

    # If Stereo
    if spf.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)

    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(signal)

    plt.savefig("./assets/graph1.png", 
                transparent = True,
                facecolor ="#5e17eb",
                edgecolor ='#FFFF',
                bbox_inches = 0,
                pad_inches = 0)

    img = Image.open('./assets/graph1.png')
    box = (101, 73, 552, 412)
    img2 = img.crop(box)
    img2.save('./assets/graphc.png')
