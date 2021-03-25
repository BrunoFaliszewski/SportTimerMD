from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

from glob import glob
from os import listdir
from os.path import isfile, join
import os
import shutil

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.list import OneLineListItem
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

Times = [5, 4, 3, 2, 1]
Names = ["Start"]

try:
    os.mkdir('Sets')
except FileExistsError:
    pass

Sets = glob(os.path.join('Sets', "*", ""))

for i in range(len(Sets)):
    Sets[i] = Sets[i].replace('Sets', '')
    Sets[i] = Sets[i].replace('/', '')

NewSets = []

class Manager(ScreenManager):
    pass

class SetTime(Screen):
    sets = ObjectProperty(None)
    workMinutes = ObjectProperty(None)
    workSeconds = ObjectProperty(None)
    restMinutes = ObjectProperty(None)
    restSeconds = ObjectProperty(None)
    exerciseName = ObjectProperty(None)
    setName = ObjectProperty(None)

    def IncreaseNumberOfSets(self):
        try:
            if self.sets.text != "100":
                self.sets.text = str(int(self.sets.text) + 1)
            else:
                self.sets.text = "0"
        except ValueError:
            self.sets.text = "0"
        finally:
            pass
    
    def DecreaseNumberOfSets(self):
        try:
            if self.sets.text != "0":
                self.sets.text = str(int(self.sets.text) - 1)
            else:
                self.sets.text = "100"
        except ValueError:
            self.sets.text = "0"
        finally:
            pass
    
    def IncreaseNumberOfWorkMinutes(self):
        try:
            if self.workMinutes.text != "100":
                self.workMinutes.text = str(int(self.workMinutes.text) + 1)
            else:
                self.workMinutes.text = "0"
        except ValueError:
            self.workMinutes.text = "0"
        finally:
            pass
    
    def DecreaseNumberOfWorkMinutes(self):
        try:
            if self.workMinutes.text != "0":
                self.workMinutes.text = str(int(self.workMinutes.text) - 1)
            else:
                self.workMinutes.text = "100"
        except ValueError:
            self.workMinutes.text = "0"
        finally:
            pass
    
    def IncreaseNumberOfWorkSeconds(self):
        try:
            if self.workSeconds.text != "60":
                self.workSeconds.text = str(int(self.workSeconds.text) + 1)
            else:
                self.workSeconds.text = "0"
        except ValueError:
            self.workSeconds.text = "0"
        finally:
            pass
    
    def DecreaseNumberOfWorkSeconds(self):
        try:
            if self.workSeconds.text != "0":
                self.workSeconds.text = str(int(self.workSeconds.text) - 1)
            else:
                self.workSeconds.text = "60"
        except ValueError:
            self.workSeconds.text = "0"
        finally:
            pass
    
    def IncreaseNumberOfRestMinutes(self):
        try:
            if self.restMinutes.text != "100":
                self.restMinutes.text = str(int(self.restMinutes.text) + 1)
            else:
                self.restMinutes.text = "0"
        except ValueError:
            self.restMinutes.text = "0"
        finally:
            pass
    
    def DecreaseNumberOfRestMinutes(self):
        try:
            if self.restMinutes.text != "0":
                self.restMinutes.text = str(int(self.restMinutes.text) - 1)
            else:
                self.restMinutes.text = "100"
        except ValueError:
            self.restMinutes.text = "0"
        finally:
            pass
    
    def IncreaseNumberOfRestSeconds(self):
        try:
            if self.restSeconds.text != "60":
                self.restSeconds.text = str(int(self.restSeconds.text) + 1)
            else:
                self.restSeconds.text = "0"
        except ValueError:
            self.restSeconds.text = "0"
        finally:
            pass
    
    def DecreaseNumberOfRestSeconds(self):
        try:
            if self.restSeconds.text != "0":
                self.restSeconds.text = str(int(self.restSeconds.text) - 1)
            else:
                self.restSeconds.text = "60"
        except ValueError:
            self.restSeconds.text = "0"
        finally:
            pass
    
    def SavePressed(self):
        global Sets, Times, Names, NewSets
        try:
            Sets.append(self.setName.text)
            os.mkdir(f'Sets/{self.setName.text}')
            with open(f'Sets/{self.setName.text}/{self.setName.text}.txt', 'w') as self.file:
                for i in range(len(Times)):
                    self.file.write(f'{Times[i]}\n')
            with open(f'Sets/{self.setName.text}/{self.setName.text}names.txt', 'w') as self.file:
                for i in range(len(Names)):
                    self.file.write(f'{Names[i]}\n')
            with open(f'Sets/{self.setName.text}/{self.setName.text}trainingtext.txt', 'w') as self.file:
                self.file.write("TrainingText")
            NewSets.append(self.setName.text)
        except FileExistsError:
            self.setName.text = "There already is that set"
        
    def ResetPressed(self):
        global Times, Names
        Times = [5, 4, 3, 2, 1]
        Names = ["Start"]

    def AddPressed(self):
        global Times, Names
        if int(self.sets.text) > 0 and (int(self.workMinutes.text) * 60 + int(self.workSeconds.text) > 0 or int(self.restMinutes.text) * 60 + int(self.restSeconds.text) > 0):
            for i in range(int(self.sets.text)):
                for j in range(int(self.workMinutes.text) * 60 + int(self.workSeconds.text)):
                    if int(self.workMinutes.text) * 60 + int(self.workSeconds.text) > 0:
                        Times.append(int(self.workMinutes.text) * 60 + int(self.workSeconds.text) - j)
                if int(self.workMinutes.text) * 60 + int(self.workSeconds.text) > 0:
                    if self.exerciseName.text != "":
                        Names.append(self.exerciseName.text)
                        self.exerciseName.text = ""
                    else:
                        Names.append("Work")
                for j in range(int(self.restMinutes.text) * 60 + int(self.restSeconds.text)):
                    if int(self.restMinutes.text) * 60 + int(self.restSeconds.text) > 0:
                        Times.append(int(self.restMinutes.text) * 60 + int(self.restSeconds.text) - j)
                if int(self.restMinutes.text) * 60 + int(self.restSeconds.text) > 0:
                    Names.append("Rest")

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

    def on_leave(self):
        Clock.unschedule(self.schedule)

    def updatelabel(self, dt):
        global Times, Names
        if self.secondsnum < len(Times):
            self.seconds = str(Times[self.secondsnum])
            self.names = Names[self.namesnum]
            if self.names != "Rest":
                if self.isFirst == True:
                    self.workSound.play()
                    self.isFirst = False
            else:
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
        pass

class MySets(Screen):
    def __init__(self, **kwargs):
        global Sets
        self.setsList = ObjectProperty(None)
        Clock.schedule_once(self.MakeSetsList)
        super(MySets, self).__init__(**kwargs)

    def on_enter(self):
        Clock.schedule_once(self.AddNewSets)

    def AddNewSets(self, dt):
        global NewSets
        for i in range(len(NewSets)):
            self.setsList.add_widget(OneLineListItem(text=f"{NewSets[i]}"))
        NewSets = []

    def MakeSetsList(self, dt):
        for i in range(len(Sets)):
            self.setsList.add_widget(
                MDExpansionPanel(
                    content=ExpansionPanelContent(),
                    panel_cls=MDExpansionPanelOneLine(
                        text=f"{Sets[i]}"
                    )
                )
            )

class ExpansionPanelContent(MDBoxLayout):
    pass

class SportTimerMD(MDApp):
    def build(self):
        return Builder.load_file("SportTimerMD.kv")
    
if __name__ == '__main__':
        SportTimerMD().run()