import pygame,time
import wave
import numpy as np
import os
import matplotlib.pyplot as plt

def welcome():
    print('''
    ***********************
    *                     *
    *      WELCOME        *
    *                     *
    ***********************
    ''')
def select():
    print('''
    *****************************
    * 1.Previous  2.Next        *
    * 3.Pause     4. Unpause    *
    * 5.V up      6.V down      *
    * 7.Plotting  8. Exit       *
    *0.Current music            *
    *****************************
    ''')
    num = input("plz input what u want：")
    return num

def playMusic(path,volue=0.5):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volue)
    pygame.mixer.music.play()


def upMusic(index,musicList):
    if index <= 0:
        print("It is the First!")
    else:
        index -= 1
    playMusic(musicList[index])
    return index

def downMusic(index,musicList):
    if index >= len(musicList)-1:
        print("It is the Last!")
    else:
        index += 1
        playMusic(musicList[index])
    return index

def pauseMusic():
    pygame.mixer.music.pause()

def unpauseMusic():
    pygame.mixer.music.unpause()

def nowMusic():
    playMusic(musicList[index])


welcome()
volue = 0.5  #initial volume
index = 0
while True:
    time.sleep(1)
    num = select()
    musicList = []#route of music
    path = r"C:\Users\ricli\PycharmProjects\test1\music"
    filepath = os.listdir(path)#getting files from poflio
    for file in filepath:
        musicList.append(os.path.join(path,file))
    if num == "0":
        print("play current music")
        nowMusic()
    elif num == "1":
        print("Previous")
        index = upMusic(index,musicList)
    elif num == "2":
        print("Next")
        index = downMusic(index,musicList)
    elif num == "3":
        print("Pause")
        pauseMusic()
    elif num == "4":
        print("Unpause")
        unpauseMusic()
    elif num == "5":
        print("Volume up")
        if volue >= 1:
            print("It is the Maximum")
        else:
            volue += 0.1
            pygame.mixer.music.set_volume(volue)
    elif num == "6":
        print("Volume Down")
        if volue <= 0:
            print("It it the minimum")
        else:
            volue -= 0.1
            pygame.mixer.music.set_volume(volue)
    elif num == "7":
        print("plotting")
        signal_wave = wave.open(musicList[index],'rb')
        sample_frequency = 16000
        data = np.fromstring(signal_wave.readframes(sample_frequency), dtype=np.int16)
        sig = signal_wave.readframes(-1)
        sig = np.fromstring(sig, 'Int16')
        sig = sig[:]
        sig = sig[25000:32000]
        left, right = data[0::2], data[1::2]
        lf, rf = abs(np.fft.rfft(left)), abs(np.fft.rfft(right))
        plt.figure(1)
        a = plt.subplot(211)
        a.set_xlabel('time [ms]')
        a.set_ylabel('sample value [-]')
        plt.plot(sig)
        plt.show()

    elif num == "8":
        print("Exit")
        break
    print(pygame.mixer.music.get_volume())

