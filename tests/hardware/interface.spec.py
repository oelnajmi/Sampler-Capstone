from services.files_services import FilesServices
from hardware.interface import Interface
from hardware.pad import Pad
from constants import Constants
from pydub import AudioSegment


class InterfaceTest:
    @classmethod
    def init_setups_pads(cls):
        interface = Interface()
        pads = interface.pads
        assert len(pads) == 4
        for i in range(4):
            assert len(pads[i]) == 4
            for j in range(4):
                assert isinstance(pads[i][j], Pad)
                assert pads[i][j].sample is None

    @classmethod
    def assign_sample_to_pad_test(cls):
        interface = Interface()
        pads = interface.pads
        first_track = FilesServices.get_tracks()[0]
        sample = AudioSegment.from_file(Constants.SAMPLES_FILE_PATH + '/' + first_track)
        interface.assign_sample_to_pad(2, 3, sample)
        assert pads[2][3].sample == sample

    @classmethod
    def assign_sample_to_pad_with_invalid_row_test(cls):
        interface = Interface()
        first_track = FilesServices.get_tracks()[0]
        sample = AudioSegment.from_file(Constants.SAMPLES_FILE_PATH + '/' + first_track)
        assert interface.assign_sample_to_pad(4, 3, sample) is False

    @classmethod
    def assign_sample_to_pad_with_invalid_column_test(cls):
        interface = Interface()
        first_track = FilesServices.get_tracks()[0]
        sample = AudioSegment.from_file(Constants.SAMPLES_FILE_PATH + '/' + first_track)
        assert interface.assign_sample_to_pad(2, 4, sample) is False

    @classmethod
    def reset_test(cls):
        interface = Interface()
        first_track = FilesServices.get_tracks()[0]
        sample = AudioSegment.from_file(Constants.SAMPLES_FILE_PATH + '/' + first_track)
        for i in range(4):
            for j in range(4):
                interface.assign_sample_to_pad(i, j, sample)
        interface.reset()
        for i in range(4):
            for j in range(4):
                assert interface.pads[i][j].sample is None


InterfaceTest.init_setups_pads()
InterfaceTest.assign_sample_to_pad_test()
InterfaceTest.assign_sample_to_pad_with_invalid_row_test()
InterfaceTest.assign_sample_to_pad_with_invalid_column_test()
InterfaceTest.reset_test()
