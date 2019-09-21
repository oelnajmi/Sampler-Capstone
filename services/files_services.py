from constants import Constants
from os import listdir


class FilesServices:
    @classmethod
    def get_tracks(cls):
        return listdir(Constants.SAMPLES_FILE_PATH)
