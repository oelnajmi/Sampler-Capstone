class Pad:
    def __init__(self):
        self.track = None
        self.start = None
        self.end = None
        self.active = False

    def click(self):
        if self.active:
            print('pressed')
        else:
            print('Pressed but unassigned')

    def assign_sample(self, track, start, end):
        self.track = track
        self.start = start
        self.end = end
        self.active = True

    def reset(self):
        self.track = None
        self.start = None
        self.end = None
        self.active = False
