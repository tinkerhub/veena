from openai import OpenAI
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def speak(text, client: OpenAI):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    response.stream_to_file("audio/output.mp3")

def record_speech(duration, fs=44100):
    """
    This function records the speech of the speaker.
    :param duration: The duration for which to record the speech.
    :param fs: The sample rate for the recording. Default is 44100.
    :return: The filename of the recorded speech.
    """
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    filename = "recorded_speech.wav"
    wav.write(filename, fs, np.int16(recording))
    print("Recording completed.")
    return filename

def speech_to_text(filename, client: OpenAI):
    # Open the audio file in binary mode
    with open(filename, 'rb') as audio_file:
        # Convert the audio file to text using OpenAI's Whisper ASR API
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )

    # Extract the text from the response
    text = transcript['text']

    return text