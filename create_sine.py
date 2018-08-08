"""Create a sine wave"""

import math

def create_sine(note: str="A", seconds: float=1, framerate: float=44100.00) -> list:
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

