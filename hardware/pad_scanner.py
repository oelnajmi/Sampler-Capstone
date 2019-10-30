from threading import Thread


class PadScanner(Thread):
    def __init__(self, interface):
        Thread.__init__(self)
        self.interface = interface
        self.daemon = True
        self.start()

    def run(self):
        count = 0
        print('begun')
        while True:
            for i in range(4):
                for j in range(4):
                    if count % 1555555 == 33:
                        self.interface.click_pad(i, j)
                    count += 1


#####################################
## Code to read simple button
#####################################

# from gpiozero import Button
#
# class Pad:
#     def __init__(self, gpio_index):
#         print('Init Button Begin')
#         button = Button(2)
#         self.sample = None
#         while True:
#             button.when_pressed = self.on_pressed
#
#     def on_pressed(self):
#         print('pressed')
#
#     def assign_sample(self, sample):
#         self.sample = sample
#
#     def reset(self):
#         self.sample = None
#
# pad = Pad()
