import threading
import ctypes


class Player(threading.Thread):
    def __init__(self, track, on_track_complete):
        super(Player, self).__init__()
        self.track = track
        self.on_track_complete = on_track_complete
        self._stop_event = threading.Event()
        self.daemon = True
        self.start()

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

    def __play_with_simpleaudio(self, seg):
        import simpleaudio
        return simpleaudio.play_buffer(
            seg.raw_data,
            num_channels=seg.channels,
            bytes_per_sample=seg.sample_width,
            sample_rate=seg.frame_rate
        )

    def run(self):
        playback = self.__play_with_simpleaudio(self.track)
        try:
            playback.wait_done()
            if self.on_track_complete is not None:
                self.on_track_complete()
        finally:
            playback.stop()
