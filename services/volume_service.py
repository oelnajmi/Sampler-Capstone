###########################################################################
## To allow this to compile on our computers, the raspberry pi code has been
## commented. When running on a raspberry pi, uncomment all commented code
## and remove all `True` lines for each loop below
###########################################################################
#import alsaaudio


class VolumeService:
    volume = 100
    global_app = None

    @classmethod
    def set_global_app(cls, global_app):
        cls.global_app = global_app

    @classmethod
    def set_volume(cls, value, source):
        if source == 'LISTEN':
            cls.global_app.get_produce_page().set_volume(value)
        elif source == 'PRODUCE':
            cls.global_app.get_listen_page().set_volume(value)
        cls.volume = value
        # m = alsaaudio.Mixer('PCM')
        # m.setvolume(value)
