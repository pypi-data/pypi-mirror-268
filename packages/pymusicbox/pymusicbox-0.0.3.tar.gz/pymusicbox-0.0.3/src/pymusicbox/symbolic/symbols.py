from dataclasses import dataclass
import numpy as np


NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NOTES_PITCH = {p: i + 1 for i, p in enumerate(NOTES)}


@dataclass
class Note:
    pitch: str
    octave: int
    length: float
    velocity: int

    def __post_init__(self):
        pitch_upper = self.pitch.upper()
        if pitch_upper not in NOTES_PITCH:
            raise ValueError(f"Invalid pitch: {self.pitch}")
        self.note = NOTES_PITCH[pitch_upper] + 12 * self.octave

        if self.velocity > 127 or self.velocity < 1:
            raise ValueError("Velocity must be between 1..127")
        self.level = self.velocity / 127


@dataclass
class Event:
    time: float


@dataclass
class NoteEvent(Event):
    note: Note


@dataclass
class Track:
    events: list[Event]
    length: float = None

    def __post_init__(self):
        if self.length is None:
            last_event = max(
                self.events, key=lambda event: (event.time, event.note.length)
            )

            self.length = last_event.time + last_event.note.length

    def __iter__(self):
        return iter(self.events)
