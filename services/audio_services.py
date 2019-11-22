from pydub import AudioSegment
from constants import Constants
from services.player import Player
from services.knobs_service import KnobsServices

WAVE = 'wav'
MP3 = 'mp3'
MAX_KNOB_VALUE = 1650


class AudioServices:
    player = None
    active_effects = [False, False, False, False]

    @classmethod
    def slice_track(cls, file_name, start, end):
        file_type = file_name.split('.')[1]
        if file_type == WAVE:
            song = AudioSegment.from_wav(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        elif file_type == MP3:
            song = AudioSegment.from_mp3(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        return song[start: end]

    @classmethod
    def play_track(cls, file_name, start=None, end=None, on_track_complete=None, apply_effects=False):
        file_type = file_name.split('.')[1]
        song = None
        if file_type == WAVE:
            song = AudioSegment.from_wav(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        elif file_type == MP3:
            song = AudioSegment.from_mp3(Constants.SAMPLES_FILE_PATH + '/' + file_name)
        if song:
            if apply_effects:
                song = cls.apply_sound_effects(song[start:end])
            else:
                song = song[start:end]
            if cls.player:
                cls.end_track()
            cls.player = Player(song, on_track_complete)
        return True

    @classmethod
    def end_track(cls):
        if cls.player:
            cls.player.raise_exception()
            cls.player = None
        return True

    @classmethod
    def apply_sound_effects(cls, song):
        if cls.active_effects[0]:
            song = cls.apply_low_pass_filter(song)
        if cls.active_effects[1]:
            song = cls.apply_high_pass_filter(song)
        if cls.active_effects[2]:
            song = cls.apply_panning(song)
        if cls.active_effects[3]:
            song = cls.apply_speedup_filter(song)
        return song

    @classmethod
    def apply_low_pass_filter(cls, song):
        value = KnobsServices.get_knob_value(0) * 22000 / MAX_KNOB_VALUE
        return song.low_pass_filter(value)

    @classmethod
    def apply_high_pass_filter(cls, song):
        value = KnobsServices.get_knob_value(1) * 22000 / MAX_KNOB_VALUE
        return song.high_pass_filter(value)

    @classmethod
    def apply_panning(cls, song):
        value = (2 * KnobsServices.get_knob_value(2) / MAX_KNOB_VALUE) - 1
        return song.pan(value)

    @classmethod
    def apply_speedup_filter(cls, song):
        value = (KnobsServices.get_knob_value(3)/MAX_KNOB_VALUE) + 1
        return song.speedup(value)

    @classmethod
    def activate_effect(cls, index):
        cls.active_effects[index] = True

    @classmethod
    def deactivate_effect(cls, index):
        cls.active_effects[index] = False

    @classmethod
    def reset_effect(cls):
        for index in range(4):
            cls.active_effects[index] = False
