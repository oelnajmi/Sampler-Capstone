###########################################################################
## To allow this to compile on our computers, the raspberry pi code has been
## commented. When running on a raspberry pi, uncomment all commented code
## and remove all `True` lines for each loop below
###########################################################################
# import Adafruit_ADS1x15


class KnobsServices:
    # adc = Adafruit_ADS1x15.ADS1015()
    # GAIN=1

    @classmethod
    def get_knob_value(cls, index):
        # return adc.read_adc(index, gain=GAIN)
        return 1650
