from dataclasses import dataclass

import numpy as np

from pymusicbox.audio.audio import Audio
from pymusicbox.symbolic.symbols import Note, NoteEvent, Track
from pymusicbox.synth.instrument import AdditiveInstrument


@dataclass
class Oscillator(AdditiveInstrument):
    sample_rate: int = 44100
    max_amp: float = 1e-1

    def render_note(self, note: Note):
        note_length = note.length*self.sample_rate

        freq = 55 * pow(2, (note.note / 12))
        t = np.linspace(0, note.length, int(note_length))

        data = self.max_amp * note.level * np.sin(2. * np.pi * freq * t)
        return Audio(data, self.sample_rate)

    def render_track(self, track: Track):
        audio = Audio.empty(track.length, self.sample_rate)

        for event in track:
            if isinstance(event, NoteEvent):
                audio.add(event.time, self.render_note(event.note))

        return audio


@dataclass
class HarmonicsConfiguration:
    attack: float
    decay: float
    release: float
    sustain_factor: float

    def lengths(self, length):
        if length < self.attack + self.decay + self.release:
            raise ValueError("Length too small for harmonics")

        lengths = (length * np.array([
            self.attack,
            self.decay,
            1 - self.attack - self.decay - self.release,
            self.release
        ])).astype(np.int64)

        lengths[-1] += length - lengths.sum()
        
        return lengths

    def amplitude_envelope(self, length, max_amplitude=1):
        attack_length, decay_length, sustain_length, release_length = self.lengths(length)

        attack = np.linspace(0, max_amplitude, attack_length)
        decay = np.linspace(max_amplitude, self.sustain_factor, decay_length)
        sustain = np.ones(sustain_length) * self.sustain_factor
        release = np.linspace(self.sustain_factor, 0.0, release_length)

        return np.concatenate((attack, decay, sustain, release))


@dataclass
class HarmonicOscillator(Oscillator):
    harmonics: HarmonicsConfiguration = None

    def render_note(self, note: Note):
        audio = super().render_note(note)

        audio *= self.harmonics.amplitude_envelope(len(audio))

        return audio