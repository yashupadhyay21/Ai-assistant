# Wake word detection using Picovoice
# wakeword_listener.py
import pvporcupine
import pyaudio
import struct
import os
from demon_config import PICOVOICE_KEY, WAKEWORD_PATH

def listen_for_wake_word():
    if not os.path.exists(WAKEWORD_PATH):
        raise FileNotFoundError(f"Wake word file not found: {WAKEWORD_PATH}")
    #porcupine = pvporcupine.create(
    #access_key=PICOVOICE_KEY,
    #keywords=["picovoice"],   # ← built-in keyword (no .ppn needed)
    #sensitivities=[0.8]
#)

    porcupine = pvporcupine.create(
        access_key=PICOVOICE_KEY,
        keyword_paths=[WAKEWORD_PATH],
        sensitivities=[0.85]
    )

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("DEMON is listening for the wake word...")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            print(".", end="", flush=True)  # ← shows mic is reading


            if porcupine.process(pcm) >= 0:
                print("👁 Wake word 'Demon' detected.")
                break
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()
