from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

from kivy.properties import ObjectProperty, StringProperty

Times = [5, 4, 3, 2, 1]
Names = ["Start"]

class Manager(ScreenManager):
    pass

class SetTime(Screen):
    sets = ObjectProperty(None)
    workMinutes = ObjectProperty(None)
    workSeconds = ObjectProperty(None)
    restMinutes = ObjectProperty(None)
    restSeconds = ObjectProperty(None)

    def IncreaseNumberOfSets(self):
        if self.sets.text != "100":
            self.sets.text = str(int(self.sets.text) + 1)
        else:
            self.sets.text = "0"
    
    def DecreaseNumberOfSets(self):
        if self.sets.text != "0":
            self.sets.text = str(int(self.sets.text) - 1)
        else:
            self.sets.text = "100"
    
    def IncreaseNumberOfWorkMinutes(self):
        if self.workMinutes.text != "100":
            self.workMinutes.text = str(int(self.workMinutes.text) + 1)
        else:
            self.workMinutes.text = "0"
    
    def DecreaseNumberOfWorkMinutes(self):
        if self.workMinutes.text != "0":
            self.workMinutes.text = str(int(self.workMinutes.text) - 1)
        else:
            self.workMinutes.text = "100"
    
    def IncreaseNumberOfWorkSeconds(self):
        if self.workSeconds.text != "60":
            self.workSeconds.text = str(int(self.workSeconds.text) + 1)
        else:
            self.workSeconds.text = "0"
    
    def DecreaseNumberOfWorkSeconds(self):
        if self.workSeconds.text != "0":
            self.workSeconds.text = str(int(self.workSeconds.text) - 1)
        else:
            self.workSeconds.text = "60"
    
    def IncreaseNumberOfRestMinutes(self):
        if self.restMinutes.text != "100":
            self.restMinutes.text = str(int(self.restMinutes.text) + 1)
        else:
            self.restMinutes.text = "0"
    
    def DecreaseNumberOfRestMinutes(self):
        if self.restMinutes.text != "0":
            self.restMinutes.text = str(int(self.restMinutes.text) - 1)
        else:
            self.restMinutes.text = "100"
    
    def IncreaseNumberOfRestSeconds(self):
        if self.restSeconds.text != "60":
            self.restSeconds.text = str(int(self.restSeconds.text) + 1)
        else:
            self.restSeconds.text = "0"
    
    def DecreaseNumberOfRestSeconds(self):
        if self.restSeconds.text != "0":
            self.restSeconds.text = str(int(self.restSeconds.text) - 1)
        else:
            self.restSeconds.text = "60"
    
    def ResetPressed(self):
        global Times, Names
        Times = [5, 4, 3, 2, 1]
        Names = ["Start"]
        print(Times)
        print(Names)

    def AddPressed(self):
        global Times, Names
        if int(self.sets.text) > 0 and (int(self.workMinutes.text) * 60 + int(self.workSeconds.text) > 0 or int(self.restMinutes.text) * 60 + int(self.restSeconds.text) > 0):
            for i in range(int(self.sets.text)):
                for j in range(int(self.workMinutes.text) * 60 + int(self.workSeconds.text)):
                    if int(self.workMinutes.text) * 60 + int(self.workSeconds.text) > 0:
                        Times.append(int(self.workMinutes.text) * 60 + int(self.workSeconds.text) - j)
                if int(self.workMinutes.text) * 60 + int(self.workSeconds.text) > 0:
                    Names.append("Work")
                for j in range(int(self.restMinutes.text) * 60 + int(self.restSeconds.text)):
                    if int(self.restMinutes.text) * 60 + int(self.restSeconds.text) > 0:
                        Times.append(int(self.restMinutes.text) * 60 + int(self.restSeconds.text) - j)
                if int(self.restMinutes.text) * 60 + int(self.restSeconds.text) > 0:
                    Names.append("Rest")
        print(Times)
        print(Names)

class Training(Screen):
    seconds = StringProperty()
    names = StringProperty()
    oneSound = SoundLoader.load('Sounds/sone.wav')
    twoSound = SoundLoader.load('Sounds/stwo.wav')
    threeSound = SoundLoader.load('Sounds/sthree.wav')
    workSound = SoundLoader.load('Sounds/swork.wav')
    restSound = SoundLoader.load('Sounds/srest.wav')
    finishSound = SoundLoader.load('Sounds/sfinish.wav')
    isFirst = False
    def on_pre_enter(self):
        self.secondsnum = 0
        self.namesnum = 0
        self.schedule = Clock.schedule_interval(self.updatelabel, 1)
    def updatelabel(self, dt):
        global Times, Names
        if self.secondsnum < len(Times):
            self.seconds = str(Times[self.secondsnum])
            self.names = Names[self.namesnum]
            if self.names == "Work":
                if self.isFirst == True:
                    self.workSound.play()
                    self.isFirst = False
            elif self.names == "Rest":
                if self.isFirst == True:
                    self.restSound.play()
                    self.isFirst = False
            if Times[self.secondsnum]  == 3:
                self.threeSound.play()
            elif Times[self.secondsnum]  == 2:
                self.twoSound.play()
            elif Times[self.secondsnum]  == 1:
                self.namesnum += 1
                self.oneSound.play()
                self.isFirst = True
            self.secondsnum += 1
        else:
            self.seconds = "Finish"
            if self.isFirst == True:
                self.finishSound.play()
                self.isFirst = False
            self.names = ""
    
    def BackPressed(self):
        Clock.unschedule(self.schedule)

class SportTimerMD(MDApp):
    def build(self):
        return Builder.load_file("SportTimerMD.kv")
    
if __name__ == '__main__':
        SportTimerMD().run()