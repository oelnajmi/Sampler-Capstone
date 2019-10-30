from services.producing_service import ProducingService

from services.audio_services import AudioServices
from services.files_services import FilesServices
from constants import Constants
from pydub import AudioSegment


class ProducingServiceTest:
    @classmethod
    def initialization_test(cls):
        producing = ProducingService()
        assert producing.complete_song is None

    @classmethod
    def add_sample_to_empty_song(cls):
        first_track = FilesServices.get_tracks()[0]
        song = AudioSegment.from_file(Constants.SAMPLES_FILE_PATH + '/' + first_track)
        producing = ProducingService()
        producing.add_sample(song)
        assert producing.complete_song == song

    @classmethod
    def add_sample_to_existing_song(cls):
        first_track = FilesServices.get_tracks()[0]
        song = AudioSegment.from_file(Constants.SAMPLES_FILE_PATH + '/' + first_track)
        producing = ProducingService()
        producing.add_sample(song)
        producing.add_sample(song)
        assert producing.complete_song == (song + song)


ProducingServiceTest.initialization_test()
ProducingServiceTest.add_sample_to_empty_song()
ProducingServiceTest.add_sample_to_existing_song()
