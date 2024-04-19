from pymusicbox.audio.audio import Audio
from pymusicbox.symbolic.symbols import Note, NoteEvent, Track


class Instrument:
    sample_rate: int = 44100


class AdditiveInstrument(Instrument):
    def render_note(self, note: Note):
        raise NotImplementedError()

    def render_track(self, track: Track):
        audio = Audio.empty(track.length, self.sample_rate)

        for event in track:
            if isinstance(event, NoteEvent):
                audio.add(event.time, self.render_note(event.note))

        return audio
