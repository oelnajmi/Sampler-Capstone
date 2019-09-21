from services.files_services import FilesServices


class FilesServicesTest:
    @classmethod
    def get_tracks_test(cls):
        assert isinstance(FilesServices.get_tracks(), list)


FilesServicesTest.get_tracks_test()
