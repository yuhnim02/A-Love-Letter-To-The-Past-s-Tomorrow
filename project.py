import tkinter as tk
from tkinter import ttk, font
from random import *
from datetime import *
import customtkinter as ctk
from customtkinter import CTkFont
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from PIL import Image
import platform
# lib : https://felipetesc.github.io/CtkDocs/#/ctk_frame

# -------ClassManager----------

class Button_Gen(ctk.CTkButton):
    def __init__(self, master, command, w, h):
        super().__init__(master= master, command= command, width= w, height= h, hover= True, text=None)

class App(ctk.CTk):
    def __init__(self, name):
        super().__init__()
        self.title(name)
        self.geometry('600x600')
        self.resizable(width=False, height=False)

class label_gen(ctk.CTkLabel):
    def __init__(self, master, text, w, h, fg_color):
        super().__init__(master= master, 
                         text= text, 
                         width= w, 
                         height= h, 
                         fg_color= fg_color)
        
class Frame_gen(ctk.CTkFrame):
    def __init__(self, master, w, h, color, coradius):
        super().__init__(master= master, 
                         width= w, 
                         height= h, 
                         fg_color= color,
                         corner_radius=coradius)

class Entry_gen(ctk.CTkEntry):
    def __init__(self, master, placeholdertext, w, h, fonts):
        super().__init__(master= master, 
                         placeholder_text= placeholdertext, 
                         width=w, 
                         height=h, 
                         font= fonts)

class ProgressBarGen(ctk.CTkProgressBar):
    def __init__(self, master, w, h):
        super().__init__(master= master, width= w, height=h, progress_color="#3CDB51", corner_radius=0)

class tickbox(ctk.CTkCheckBox):
    def __init__(self, master, coradius, onvalue, offvalue):
        super().__init__(master= master, onvalue= onvalue, offvalue= offvalue, corner_radius= 10, checkbox_height=35, checkbox_width=35, text=None, width=1, height=1, hover_color="#BDF1AD", fg_color="#69E970")

class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, bgcolor, w, h):
        super().__init__(master=master, width=w, fg_color= bgcolor, corner_radius=0, height=h)


# ------MAIN------------------
def main():
    ctk.FontManager.load_font("FSEX300.ttf") #customTkinter.FontManger.load_font('') would load the file
    sys_mode('light')

    mixer.init()
    start=mixer.Sound(file='music/start.mp3')
    click= mixer.Sound(file='music/mausclick.mp3')
    start.play()

    #----------ROOT---------
    root = App("A Love Letter To The Past's Tomorrow")
    time.sleep(0.7) # pause for 0.7

    os = platform.system() # return the name of device's os
    mainicon_png = tk.PhotoImage(file='mainicon.png')

    if os == 'Windows':
        root.iconbitmap('mainicon.ico')
    elif os == 'Darwin' or os =='Linux':
        root.iconphoto(True, mainicon_png)
    # acess the family name through print(font.families()))
    global customfont
    customfont='Fixedsys Excelsior 3.01'
    # -------- IMAGES ---------
    screen =ctk.CTkImage(Image.open('widgets/computer.png'), size=(600,600))
    user_background = ctk.CTkImage(Image.open('widgets/userbackground.png'), size=(90,90))

    default = ctk.CTkImage(Image.open('widgets/default.png'), size=(55,35))
    on = ctk.CTkImage(Image.open('widgets/on.png'), size=(55,35))
    off = ctk.CTkImage(Image.open('widgets/off.png'), size=(55,35))
    next_img = ctk.CTkImage(Image.open('widgets/next.png'), size=(50,30))

    music_list = ['music/lecarrousel.mp3',
                 'music/aquaticambience.mp3',
                  'music/leash.mp3',
                  'music/newhome.mp3',
                  'music/breakinstory.mp3']

    img1 = ctk.CTkImage(Image.open('Background/asadal_stock_30.png'), size=(525,460))
    img2 = ctk.CTkImage(Image.open('Background/asadal_stock_18.png'), size=(525,460))
    img3 = ctk.CTkImage(Image.open('Background/Background2.png'), size=(525,460))
    img4 = ctk.CTkImage(Image.open('Background/asadal_stock_58.png'), size=(525,460))
    img5 = ctk.CTkImage(Image.open('Background/asadal_stock_61.png'), size=(525,460))
    img6 = ctk.CTkImage(Image.open('Background/asadal_stock_144.png'), size=(525,460))

    background_list = [img1, img3, img4, img5, img6]
    global backgroundindex
    backgroundindex = 0

    #--------------------------
    ctk.CTkLabel(root, image=screen).place(x=0,y=0)
    ctk.CTkButton(master= root, 
                  width= 60, 
                  command= lambda: change_bg(main_frame, background_list, title),
                  height= 30,
                  text='BACKGROUND',
                  font=(customfont, 14),
                  corner_radius=0,
                  fg_color="#747474",
                  hover_color="#202020").place(x=375,y=553)
    #---------mainFrame---------
    main_frame = Frame_gen(root, 525, 460, "#202020", 0)
    main_frame.configure(bg_color='black')
    main_frame.pack_propagate(False)
    main_frame.pack(side= 'top', pady= 40)
    main_frame.update()

    ctk.CTkLabel(main_frame, image=img1).place(x=0,y=0)
    #---------GridSystem-----
    main_frame.columnconfigure(0, weight=1) 
    main_frame.rowconfigure(0, weight=3)
    main_frame.rowconfigure(1, weight=4)
    main_frame.rowconfigure(2, weight=3)
    main_frame.rowconfigure(3, weight=15)
    main_frame.rowconfigure(4, weight=5)
    main_frame.grid_propagate(False)
    #---------BLOCK1-----------
    # Title entry, ramdon quote
    title = Entry_gen(main_frame, "To-do :3", 250, 90, fonts=(customfont, 35))
    title.configure(fg_color="#fafae5", corner_radius=0)
    title.bind('<Return>', on_enter)
    title.grid(column=0, row=1, sticky='ws', padx= 30, pady=5), 

    user_background = ctk.CTkLabel(main_frame, width= 90, height=90, image= user_background, fg_color="#fafae5", text='')
    user_background.place(x=290,y=16.7)

    emoticon_list = ['( ´ ▽ ` )ﾉ', 
                     '⊂(￣▽￣)⊃', 
                     '(^˵◕ω◕˵^)' ,
                     '(ノ= ⩊ = )ノ', 
                     '(￣﹃￣)', 
                     '(≖ ͜ʖ≖)']

    global songindex
    global pause
    global played
    played= False
    pause = False
    songindex = 0

    next_button = Button_Gen(main_frame, lambda: next(music_list), 65, 40)
    next_button.configure(corner_radius=0, image=next_img, hover=False)
    next_button.grid(column=0, row=1, sticky='es', pady=(0,5), padx=33)
    
    music_button = Button_Gen(main_frame, lambda: play_music(music_list, music_button, on, off), 65, 40)
    music_button.configure( image=default ,corner_radius=0, hover=False)
    music_button.grid(column=0, row=1, sticky='ne', pady=(15,0), padx=33)
    #---------BLOCK2----------------
    global pbar
    pbar = ProgressBarGen(main_frame,460,30)
    pbar.grid(column=0, row=2, pady=(10,0), sticky='ns')
    pbar.configure(fg_color="#fafae5", border_width=2)
    pbar.set(0)
    pbar.update()
    #---------BlOCK3-----------------
    maintasks= ScrollableFrame(main_frame, 'gray', 445, 265)
    maintasks.configure(fg_color="#fafae5", border_width=2)
    maintasks.grid(column=0, row=3)
    #-------------------------------------------------
    deletable = False
    task_frame= Frame_gen(maintasks, 410, 60, "#fafae5",0)
    task_frame.pack_propagate(False)
    task_frame.pack(side='top', pady=(10,0))
    task_frame.rowconfigure(0, weight=3)
    task_frame.rowconfigure(1, weight=0, minsize=10)
    task_frame.columnconfigure(0, weight=0, minsize=30) # forbid the grid to be overlaid by widgets
    task_frame.columnconfigure(1, weight=5)
    task_frame.columnconfigure(2, weight=0, minsize=40)
    task_frame.grid_propagate(False)
    task_frame.update()

    global tasknumb
    tasknumb = 1
    global ticked
    ticked = 0
    global step
    step = 0
    # TASK FRAME 1
    checkbox1 = tickbox(task_frame, 10, 'on', 'off')
    checkbox1.grid(row=0, column=0)
    checkbox1.bind('<Button-1>', lambda event: turningonoff(checkbox1.get())) 

    entry1 = Entry_gen(task_frame, '          ( ´ ▽ ` )ﾉ'
                       , 100, 40, 
                       (customfont, 20))
    entry1.configure(fg_color="#fafae5", text_color = '#000000')
    entry1.bind('<Return>', lambda event: on_enter(event))
    entry1.grid(row=0, column= 1, sticky= 'we')

    add_btn = Button_Gen(task_frame, lambda: task_generator(maintasks, add_btn, False), 30, 30)
    add_btn.configure(fg_color='transparent', text='+', font=(customfont,45), text_color='#000000', hover_color='#f5f5c3')
    add_btn.grid(row=0, column=2)

    root.bind('<Button-1>', lambda event: click.play())
    
    root.mainloop()


def sys_mode(mode):
    ctk.set_appearance_mode(mode)

def on_enter(event): # remove focus
   event.widget.winfo_toplevel().focus()
   # THIS MOVE THE FOCUS TO THE TOPLEVEL OR ROOT IN THIS CASEE

def delete_frame(widget, deletable, status):
    if deletable == True:
        widget.destroy()
        global tasknumb
        tasknumb -= 1
        global ticked # delete if tick button is ticked
        if status == 'on':
            ticked -= 1
    step_update()

def turningonoff(passin):
    global ticked
    if passin == 'on':
        ticked +=1
        step_update()
    else:
        ticked -=1
        step_update()

def step_update():
    global step, ticked, tasknumb, pbar
    step = float(ticked/tasknumb)
    pbar.set(step)

def task_generator(maintasks, selfdestruct, killable):
    global tasknumb
    tasknumb += 1
    step_update()
    deletable = True
    if killable == True:
        selfdestruct.destroy()
    task_frame= Frame_gen(maintasks, 410, 60, "#fafae5",0)
    task_frame.pack_propagate(False)
    task_frame.pack(side='top', pady=(15,0))
    task_frame.rowconfigure(0, weight=3)
    task_frame.rowconfigure(1, weight=0, minsize=10)

    task_frame.columnconfigure(0, weight=0, minsize=30)
    task_frame.columnconfigure(1, weight=5)
    task_frame.columnconfigure(2, weight=0, minsize=40)
    task_frame.grid_propagate(False)
    task_frame.update()

    checkbox1 = tickbox(task_frame, 10, 'on', 'off')
    checkbox1.grid(row=0, column=0)
    checkbox1.bind('<Button-1>', lambda event: turningonoff(checkbox1.get()))

    entry1 = Entry_gen(task_frame, '              ...', 
                       100, 40, 
                       (customfont, 20))
    entry1.configure(fg_color="#fafae5", text_color = '#000000')

    
    entry1.bind('<Return>', lambda event: on_enter(event))
    entry1.grid(row=0, column= 1, sticky= 'we')

    delete_btn = Button_Gen(task_frame, lambda: delete_frame(task_frame, deletable, checkbox1.get()), 30, 15)
    delete_btn.configure(fg_color="#9E0303", text= 'DEL', font=(customfont,15), hover_color="#e41212")
    delete_btn.grid(row=1, column=1, pady=(5,0))

    add_btn = Button_Gen(task_frame, lambda: task_generator(maintasks, add_btn, False), 30, 30)
    add_btn.configure(fg_color='transparent', text='+', font=(customfont,45), text_color='#000000', hover_color='#f5f5c3')    
    add_btn.grid(row=0, column=2)

def play_music(music_list, widget, on, off):
    global songindex, pause, played

    if played == False: # have never click
        mixer.music.load(music_list[songindex])
        mixer.music.play(loops=-1)
        
        played = True
        widget.configure( image=on,corner_radius=0)
    elif mixer.music.get_busy() == True and pause == False: # PLAYING AND NOT PAUSE : if button is clicked here, it would cause PLAYING FALSE and PAUSE TRUE
        mixer.music.pause()
        pause = True
        widget.configure(image=off ,corner_radius=0)

    elif mixer.music.get_busy() == False and pause == True: # PLAYING IS FALSE AND PAUSE IS TRUE: if button clicked in this condition, play and unpause
        mixer.music.unpause()
        pause= False
        widget.configure( image=on,corner_radius=0)

def next(music_list):
    global songindex, pause, played
    if played == True and pause == False:
        if songindex + 1 != len(music_list):
            songindex += 1
        else:
            songindex = 0
        
        mixer.music.load(music_list[songindex])
        mixer.music.play(loops=-1)

def change_bg(main_frame, imglist, belowwidget):
    global backgroundindex
    if backgroundindex +1 != len(imglist):
        backgroundindex +=1
    else:
        backgroundindex = 0
    label1= ctk.CTkLabel(master=main_frame, image=imglist[backgroundindex])
    label1.lower(belowwidget)
    label1.place(x=0,y=0)

if __name__ == '__main__':
    main()