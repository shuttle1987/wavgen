"""Create a sine wave"""

import math
import wave
import struct
import io


def create_sine(*, note: str="A", seconds: float=1, framerate: float=44100.00) -> list:
    """Create a sine wave representing the frequency of a piano note 
    in octave 4 using the A440 tuning"""
    note_to_freq = {
        "C": 261.63,
        "C♯": 277.18, "D♭": 277.18,
        "D": 293.66,
        "E♭": 311.13, "D♯": 311.13,
        "E": 329.63,
        "F": 349.23,
        "F♯": 369.99, "G♭": 369.99, 
        "G": 392.00,
        "A♭": 415.30, "G♯": 415.30,
        "A": 440.00,
        "B♭": 466.16, "A♯": 466.16,
        "B": 493.88,
    }
    datasize = int(seconds * framerate)
    freq = note_to_freq[note]
    sine_list=[]
    for x in range(datasize):
        sine_list.append(math.sin(2*math.pi * freq * (x/framerate)))
    return sine_list


def make_audio(*, audio_data, framerate: float=44100.00, duration: float=1) -> io.BytesIO:
    """Create a file with appropriate WAV magic bytes and encoding

    :audio_data: raw frame data to be placed into the wav file
    :framerate: hertz
    :duration: seconds this file will go for
    """
    amp = 8000.0 # amplitude
    wav_data = io.BytesIO()
    wav_file = wave.open(wav_data, "wb")
    # wav params
    nchannels = 1
    sampwidth = 2
    framerate = int(framerate)
    nframes = int(framerate*duration)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    # write the contents
    for s in audio_data:
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.close()

    # Seek to start of the audio stream data
    wav_data.seek(0)
    return wav_data


if __name__ == "__main__":
    a_tone = create_sine(note="A", seconds=1)
    file_contents = make_audio(audio_data=a_tone, duration=1)
    with open("a_tone.wav", "wb") as f:
        f.write(file_contents.getvalue()) # TODO: This is a bit nasty from an efficiency point of
                                          #       view, change this if using for production
    file_contents.close()
