from services.files_services import FilesServices
from services.player import Player
from pydub import AudioSegment
from constants import Constants
import time


class PlayerTest:
    @classmethod
    def play_track(cls):
        first_track = FilesServices.get_tracks()[0]
        song = AudioSegment.from_wav(Constants.SAMPLES_FILE_PATH + '/' + first_track)
        Player(song, None)
        time.sleep(30)


PlayerTest.play_track()
