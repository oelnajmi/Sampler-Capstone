from pydub import AudioSegment


class ProducingService:
    def __init__(self):
        self.complete_song = None

    def add_sample(self, sample):
        if self.complete_song is None:
            self.complete_song = sample
        else:
            self.complete_song += sample

    def add_silence(self, length):
        self.complete_song += [0] * length

    def complete(self):
        return True
        # Save the track

