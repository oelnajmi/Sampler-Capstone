from pydub import AudioSegment
from constants import Constants
from services.player import Player

WAVE = 'wav'
MP3 = 'mp3'


class AudioServices:
    player = None

    @classmethod
    def slice_track(cls, file_name, start, end):
        file_type = file_name.split('.')[1]
        if file_type == WAVE:
            song = AudioSegment.from_wav(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        elif file_type == MP3:
            song = AudioSegment.from_mp3(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        return song[start: end]

    @classmethod
    def play_track(cls, file_name, start=None, end=None, on_track_complete=None):
        if cls.player:
            cls.end_track()

        file_type = file_name.split('.')[1]
        song = None
        if file_type == WAVE:
            song = AudioSegment.from_wav(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        elif file_type == MP3:
            song = AudioSegment.from_mp3(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        if song:
            cls.player = Player(song[start:end], on_track_complete)
        return True

    @classmethod
    def end_track(cls):
        if cls.player:
            cls.player.raise_exception()
            cls.player = None
        return True
