import project
from project import *

'''
def step_update():
    global step, ticked, tasknumb, pbar
    step = float(ticked/tasknumb)
    pbar.set(step)
'''
def test_step_update():
    class pbartest:
        def set(self, val): # pass the step into val 
            self.value = val # call set() on the pbar
    
    project.tasknumb = 4
    project.ticked = 2
    project.pbar = pbartest() # reassign the pbar to a fake bar
    project.step = 0

    project.step_update()
    assert project.step == 0.5 # step = tasknumb / ticked
    assert project.pbar.value == 0.5

    project.ticked = 4
    project.step_update()
    assert project.step == 1.0
    assert project.pbar.value == 1.0


def test_turningonoff():
    class pbar: # a fake pbar instance because in my code, turningofoff() include step_update()
        def set(self, val): 
            self.value = val

    project.tasknumb = 3
    project.ticked = 0
    project.pbar = pbar()

    project.turningonoff('on')
    assert project.ticked == 1
    project.turningonoff('off')
    assert project.ticked == 0


def test_next():
    class testmusic:
        def load(self, song): self.loaded = song
        def play(self, loops): self.played = True

    project.mixer.music = testmusic()

    project.music_list = ["song1.mp3", "song2.mp3"]
    project.songindex = 0
    project.played = True
    project.pause = False

    project.next(project.music_list)
    assert project.songindex == 1
    assert project.mixer.music.loaded == "song2.mp3"

    project.songindex = 1
    project.next(project.music_list)
    assert project.songindex == 0
    assert project.mixer.music.loaded == "song1.mp3"

if __name__ == '__main__':
    test_step_update()
    test_next()
    test_turningonoff()