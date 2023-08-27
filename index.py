import numpy as np
import scipy.io.wavfile as wavfile
import tkinter as tk
import pygame, sys
from mix import mix_audio
from graph import GenWavF
from PIL import Image, ImageTk

# Sampling rate y duración.

sampling_rate = 44100  # 44.1 kHz. (Frecuencia de muestreo)
duration = 5  # 5 segundos.

# Crear la función para generar la señal.

def generate_signal(equation_func, frequency):
    num_samples = sampling_rate * duration
    x = np.linspace(0, duration, num_samples)
    y = equation_func(x, frequency)
    scaling_factor = 0.2
    y_scaled = y * scaling_factor
    max_amplitude = 0.8
    y_clipped = np.clip(y_scaled, -max_amplitude, max_amplitude)
    y_normalized = y_clipped / np.max(np.abs(y_clipped))
    y_int = np.int16(y_normalized * 32767)
    return y_int

# Experimentando con el input de lambda (Funcionó, pero no fue necesario para el producto final.)

equation_input = 3 #input("Escribe la ecuación > ")

equation_func = lambda x, frequency: eval(equation_input) / (440 * np.pi)

# Ejemplo de ecuación: np.sin(x)

equation_1 = lambda x, frequency: np.sin(2 * np.pi * frequency * x)

# Ejemplo de ecuación: np.tan(t ** 2)
equation_2 = lambda x, frequency: np.tan(x * 2 * np.pi * frequency)

# Ejemplo de ecuación (No fue usado)

equation_3 = lambda x, frequency: np.sin(2 * np.pi * frequency * x**2)

# Función square

def equation_square(x, frequency):
    return np.sign(np.sin(2 * np.pi * frequency * x))

# Función triangle

def equation_triangle(x, frequency):
    return 2 * np.arcsin(np.sin(2 * np.pi * frequency * x)) / np.pi

# Función saw

def equation_saw(x, frequency):
    return (2 * frequency * x) % 2 - 1

# Ejemplo de ecuación para el bajo estilo "808"

def generate_808_sound(x, frequency):
    frequencies = [50, 100, 200, 400]  # Frecuencias de las componentes sinusoidales
    amplitudes = [0.5, 0.3, 0.2, 0.1]  # Amplitudes de las componentes sinusoidales
    y = np.sum([amplitude * np.sin(2 * np.pi * f * x) for f, amplitude in zip(frequencies, amplitudes)], axis=0)
    y /= np.max(np.abs(y))  # Escalar el resultado para que esté entre -1 y 1
    return y

# Función sine

equation_1 = lambda x, frequency: np.sin(2 * np.pi * frequency * x)

# Función tan

equation_tan = lambda x, frequency: np.tan(x * 2 * np.pi * frequency)

# Función square

def equation_square(x, frequency):
    return np.sign(np.sin(2 * np.pi * frequency * x))

# Función triangle

def equation_triangle(x, frequency):
    return 2 * np.arcsin(np.sin(2 * np.pi * frequency * x)) / np.pi

# Función saw

def equation_saw(x, frequency):
    return (2 * frequency * x) % 2 - 1

# Frecuencias de las notas A4 y A3.

frequency_a4 = 440  # Frecuencia de A4 en Hz
frequencies = [370,392,415.30,440,466,493.88,523.25]


# Tkinter

def UpdateImage():
    newimg = ImageTk.PhotoImage(Image.open("./assets/graphc.png"))
    label1.config(image=newimg)
    label1.image = newimg 

# Creo la ventana.

root = tk.Tk()
root.title("Ethereal Synthetizer")
root.geometry("1366x768")
root.resizable(False,False)

bg_img = tk.PhotoImage(file="assets/background.png")

# Añado pygame para controlar el sonido directamente desde su mixer.

pygame.init()
def stop_sound():
    pygame.mixer.stop()
def play_sound():
    # Path to your WAV file
    sound_path = "output/combined_signal.wav"
    
    # Stop the sound if it's already playing
    pygame.mixer.stop()
    
    # Load and play the sound
    pygame.mixer.init(frequency=44100)
    pygame.mixer.Sound(sound_path).play()

def on_closing():
    root.destroy()  # Cierro la ventana de TKINTER
    sys.exit()      # Cierro el script the python

# Valores Base

waveform1 = "SINE"
waveform2 = "SINE"
waveform3 = "SINE"
pitch1    = 0
pitch2    = 0
pitch3    = 0

# Funciones de Tkinter

def CambiarWaveForm1():
    global waveform1
    if waveform1 == "SINE":
        waveform1 = "TAN"
    elif waveform1 == "TAN":
        waveform1 = "SQUARE"
    elif waveform1 == "SQUARE":
        waveform1 = "TRIANGLE"
    elif waveform1 == "TRIANGLE":
        waveform1 = "SAW"
    else:
        waveform1 = "SINE"
    osc1_wave.config(text=waveform1)

def CambiarWaveForm2():
    global waveform2
    if waveform2 == "SINE":
        waveform2 = "TAN"
    elif waveform2 == "TAN":
        waveform2 = "SQUARE"
    elif waveform2 == "SQUARE":
        waveform2 = "TRIANGLE"
    elif waveform2 == "TRIANGLE":
        waveform2 = "SAW"
    else:
        waveform2 = "SINE"
    osc2_wave.config(text=waveform2)

def CambiarWaveForm3():
    global waveform3
    if waveform3 == "SINE":
        waveform3 = "TAN"
    elif waveform3 == "TAN":
        waveform3 = "SQUARE"
    elif waveform3 == "SQUARE":
        waveform3 = "TRIANGLE"
    elif waveform3 == "TRIANGLE":
        waveform3 = "SAW"
    else:
        waveform3 = "SINE"
    osc3_wave.config(text=waveform3)

def GenerateSignals():
    global waveform1
    global waveform2
    global waveform3

    if waveform1 == "SINE":
        wavfile.write('output/signal1.wav', sampling_rate, generate_signal(equation_1, frequencies[3+pitch1]))
        print("done.")
    elif waveform1 == "TAN":
        wavfile.write('output/signal1.wav', sampling_rate, generate_signal(equation_tan, frequencies[3+pitch1]))
        print("done.")
    elif waveform1 == "SQUARE":
        wavfile.write('output/signal1.wav', sampling_rate, generate_signal(equation_square, frequencies[3+pitch1]))
        print("done.")
    elif waveform1 == "TRIANGLE":
        wavfile.write('output/signal1.wav', sampling_rate, generate_signal(equation_triangle, frequencies[3+pitch1]))
        print("done.")
    elif waveform1 == "SAW":
        wavfile.write('output/signal1.wav', sampling_rate, generate_signal(equation_saw, frequencies[3+pitch1]))
        print("done.")

    if waveform2 == "SINE":
        wavfile.write('output/signal2.wav', sampling_rate, generate_signal(equation_1, frequencies[3+pitch2]))
        print("done.")
    elif waveform2 == "TAN":
        wavfile.write('output/signal2.wav', sampling_rate, generate_signal(equation_tan, frequencies[3+pitch2]))
        print("done.")
    elif waveform2 == "SQUARE":
        wavfile.write('output/signal2.wav', sampling_rate, generate_signal(equation_square, frequencies[3+pitch2]))
        print("done.")
    elif waveform2 == "TRIANGLE":
        wavfile.write('output/signal2.wav', sampling_rate, generate_signal(equation_triangle, frequencies[3+pitch2]))
        print("done.")
    elif waveform2 == "SAW":
        wavfile.write('output/signal2.wav', sampling_rate, generate_signal(equation_saw, frequencies[3+pitch2]))
        print("done.")

    if waveform3 == "SINE":
        wavfile.write('output/signal3.wav', sampling_rate, generate_signal(equation_1, frequencies[3+pitch3]))
        print("done.")
    elif waveform3 == "TAN":
        wavfile.write('output/signal3.wav', sampling_rate, generate_signal(equation_tan, frequencies[3+pitch3]))
        print("done.")
    elif waveform3 == "SQUARE":
        wavfile.write('output/signal3.wav', sampling_rate, generate_signal(equation_square, frequencies[3+pitch3]))
        print("done.")
    elif waveform3 == "TRIANGLE":
        wavfile.write('output/signal3.wav', sampling_rate, generate_signal(equation_triangle, frequencies[3+pitch3]))
        print("done.")
    elif waveform3 == "SAW":
        wavfile.write('output/signal3.wav', sampling_rate, generate_signal(equation_saw, frequencies[3+pitch3]))
        print("done.")

    # Ejemplo de uso
    input_files = ['output/signal1.wav', 'output/signal2.wav', 'output/signal3.wav']
    mix_audio(input_files, 'output/combined_signal.wav')

    GenWavF()
    UpdateImage()

    print("Combined signal saved.")

def CambiarPitch1():
    global pitch1
    pitch1 +=1
    if pitch1 == 4:
        pitch1 = -3
    pit1_but.config(text=pitch1)

def CambiarPitch2():
    global pitch2
    pitch2 +=1
    if pitch2 == 4:
        pitch2 = -3
    pit2_but.config(text=pitch2)

def CambiarPitch3():
    global pitch3
    pitch3 +=1
    if pitch3 == 4:
        pitch3 = -3
    pit3_but.config(text=pitch3)

# Estilización

bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Botón para reproducir sonido

play_button = tk.Button(root, text="PLAY SOUND", command=play_sound, font=("Spartan",17,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0)
play_button.place(x=950,y=309)
stop_button = tk.Button(root, text="STOP SOUND", command=stop_sound, font=("Spartan",17,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0)
stop_button.place(x=950,y=410)

# Creando las entradas

osc1_wave = tk.Button(root, text=waveform1, command=CambiarWaveForm1, font=("Spartan",17,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0)
osc1_wave.place(x=778,y=309)
osc2_wave = tk.Button(root, text=waveform2, command=CambiarWaveForm2, font=("Spartan",17,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0)
osc2_wave.place(x=778,y=361)
osc3_wave = tk.Button(root, text=waveform3, command=CambiarWaveForm3, font=("Spartan",17,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0)
osc3_wave.place(x=778,y=410)

# Variaciones de tono

pit1_but = tk.Button(root, text=pitch1, font=("Spartan",19,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0,command=CambiarPitch1)
pit1_but.place(x=465,y=307)
pit2_but = tk.Button(root, text=pitch3, font=("Spartan",19,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0,command=CambiarPitch2)
pit2_but.place(x=465,y=357)
pit3_but = tk.Button(root, text=pitch3, font=("Spartan",19,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0,command=CambiarPitch3)
pit3_but.place(x=465,y=408)

# Generando los sonidos

gen3s = tk.Button(root, text="GENERATE", command=GenerateSignals, font=("Spartan",17,"bold"),fg="#ff5757",background="#5e17eb",borderwidth=0)
gen3s.place(x=950,y=361)

# Imagén del gráfico de la función

image1 = Image.open("./assets/graphc.png")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test, borderwidth=1,bg="white")
label1.image = test

# Posicion de la imagen

label1.place(x=0, y=212)
root.mainloop()

# Protocolo para cerrar el script al cerrar la ventana.

root.protocol("WM_DELETE_WINDOW", on_closing)

# Tkinter Loop

root.mainloop()