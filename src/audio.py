from openai import OpenAI
import sounddevice as sd
import numpy as np
import keyboard
from vision import has_speaker_left_stage
import scipy.io.wavfile as wav
import cv2


def speak(text, client: OpenAI):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    response.stream_to_file("audio/output.mp3")


def record_speech(fs=44100):
    """
    This function records the speech of the speaker.
    :param fs: The sample rate for the recording. Default is 44100.
    :return: The filename of the recorded speech.
    """
    print("Recording... Press 'q' to stop.")

    # Start recording in a loop
    recording = []
    while True:
        # Record audio for a short duration
        short_recording = sd.rec(int(1 * fs), samplerate=fs, channels=2)
        sd.wait()
        recording.append(short_recording)

        # If 'q' is pressed, stop recording
        if keyboard.is_pressed('q'):
            break

    # Concatenate all short recordings
    recording = np.concatenate(recording, axis=0)

    filename = "recorded_speech.wav"
    wav.write(filename, fs, np.int16(recording))
    print("Recording completed.")
    return filename


def record_speech_vision(fs=44100):
    """
    This function records the speech of the speaker.
    :param fs: The sample rate for the recording. Default is 44100.
    :return: The filename of the recorded speech.
    """
    print("Recording... Stop when speaker leaves the stage.")

    # Start recording in a loop
    recording = []
    cap = cv2.VideoCapture(0)
    client = OpenAI()

    while True:
        # Record audio for a short duration
        short_recording = sd.rec(int(1 * fs), samplerate=fs, channels=2)
        sd.wait()
        recording.append(short_recording)

        # Capture frame-by-frame
        ret, frame = cap.read()

        # If the speaker has left the stage, stop recording
        if has_speaker_left_stage(frame, client):
            break

    # Concatenate all short recordings
    recording = np.concatenate(recording, axis=0)

    filename = "recorded_speech.wav"
    wav.write(filename, fs, np.int16(recording))
    print("Recording completed.")
    return filename


def transcribe(filename, client: OpenAI):
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
