class Pad:
    def __init__(self):
        self.sample = None

    def click(self):
        if self.sample:
            print('pressed')
        else:
            print('Pressed but unassigned')

    def assign_sample(self, sample):
        self.sample = sample

    def reset(self):
        self.sample = None
