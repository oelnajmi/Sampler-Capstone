from services.audio_services import AudioServices
from services.files_services import FilesServices
from constants import Constants
from pydub import AudioSegment


class AudioServicesTest:
    @classmethod
    def slice_track_test(cls):
        first_track = FilesServices.get_tracks()[0]
        total_length = len(AudioSegment.from_file(Constants.SAMPLES_FILE_PATH + '/' + first_track))
        start = 2 * total_length // 5
        end = 3 * total_length // 5
        difference_length = end - start
        assert len(AudioServices.slice_track(first_track, start, end)) == difference_length


AudioServicesTest.slice_track_test()
