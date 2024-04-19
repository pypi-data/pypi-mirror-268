# pymusicbox

A library with toolkits for music synthesis and analysis. This is a work in progress.

## Current Features

- Symbolic language to represent notes and tracks
- Create instruments with sine oscilators and harmonics

## Installation

```pip install pymusicbox```

## Example Usage

```python
from pymusicbox.synth.instrument.oscillator import HarmonicOscillator, HarmonicsConfiguration
from pymusicbox.symbolic.symbols import Note, NoteEvent, Track

track = Track(events=[
  NoteEvent(time=0, note=Note(pitch='C', octave=3, length=1, velocity=100)),
  NoteEvent(time=1, note=Note(pitch='D', octave=3, length=1, velocity=80)),
  NoteEvent(time=2, note=Note(pitch='E', octave=3, length=1, velocity=90)),
  NoteEvent(time=2, note=Note(pitch='A', octave=3, length=1, velocity=100)),
  NoteEvent(time=3, note=Note(pitch='A', octave=3, length=1.8, velocity=110)),
  NoteEvent(time=3, note=Note(pitch='D', octave=2, length=1.8, velocity=110)),
])

harmonics = HarmonicsConfiguration(attack=0.1, decay=0.2, release=0.2, sustain_factor=0.6)
oscillator = HarmonicOscillator(harmonics=harmonics)
audio = oscillator.render_track(track)
audio.write('output.wav')
```
