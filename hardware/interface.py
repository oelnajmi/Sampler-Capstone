from hardware.pad import Pad
from hardware.pad_scanner import PadScanner


class Interface:
    def __init__(self):
        self.pads = [[None] * 4] * 4
        for i in range(4):
            for j in range(4):
                self.pads[i][j] = Pad()
        PadScanner(self)

    def assign_sample_to_pad(self, row, column, track, start, end):
        if row > 3:
            return False
        if column > 3:
            return False
        self.pads[row][column].assign_sample(track, start, end)

    def reset(self):
        for i in range(4):
            for j in range(4):
                self.pads[i][j].reset()

    def click_pad(self, row, column):
        self.pads[row][column].click()
