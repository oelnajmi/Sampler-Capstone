from pydub import AudioSegment
from constants import Constants

WAVE = 'wav'
MP3 = 'mp3'


class AudioServices:
    @classmethod
    def slice_track(cls, file_name, start, end):
        file_type = file_name.split('.')[1]
        if file_type == WAVE:
            song = AudioSegment.from_wav(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        elif file_type == MP3:
            song = AudioSegment.from_mp3(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        return song[start: end]
