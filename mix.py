import pyaudio
import wave
import numpy as np

# Función para combinar las señales

def mix_audio(input_files, output_file, volume=0.1):

    # Abro los archivos .wav

    waves = [wave.open(file, 'rb') for file in input_files]

    # Consigo sus formatos (number of channels, sample width, frame rate, number of frames, compression type, and compression name)

    formats = [w.getparams() for w in waves]

    # Chequeo que todos los valores sean iguales para una mezcla correcta

    if len(set(formats)) > 1:
        raise ValueError("All files must have the same number of channels, sample width, and frame rate.")

    num_channels, sample_width, frame_rate, num_frames, _, _ = formats[0]

    # Inicio PyAudio

    p = pyaudio.PyAudio()

    # Inicio el output

    stream = p.open(format=p.get_format_from_width(sample_width),
                    channels=num_channels,
                    rate=frame_rate,
                    output=True)

    # Leo y mezclo los archivos

    mixed_frames = np.zeros(num_frames, dtype=np.int16)
    for w in waves:
        frames = w.readframes(num_frames)
        audio_data = np.frombuffer(frames, dtype=np.int16)
        mixed_frames += audio_data

    # Normalizo las muestras entre 1 y -1

    mixed_frames = mixed_frames / len(waves)

    # Uso el valor de escala para regular el volumen

    mixed_frames *= volume

    # Vuelvo a convertir el formato en int16

    mixed_frames = mixed_frames.astype(np.int16)

    # Guardo el resultado

    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(num_channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(frame_rate)
        wf.writeframes(mixed_frames.tobytes())

    # Apago la libreria
    
    for w in waves:
        w.close()

    stream.stop_stream()
    stream.close()
    p.terminate()
