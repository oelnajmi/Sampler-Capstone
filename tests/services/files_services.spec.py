from services.files_services import FilesServices


class FilesServicesTest:
    @classmethod
    def get_tracks_test(cls):
        assert FilesServices.get_tracks() == ['file_one.txt', 'file_two.txt']


FilesServicesTest.get_tracks_test()
