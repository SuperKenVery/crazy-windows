import tkinter as tk
import random,threading,time



class window(tk.Tk):
    def setalpha(self,alpha):
        self.attributes("-alpha",alpha)
        self.alpha=alpha
    def move(self,x,y):
        x=int(x)
        y=int(y)
        self.geometry("+"+str(x)+"+"+str(y))
        self.x=x
        self.y=y
        if self.y>scrnHeight or self.y<-self.height-50 or self.x<-self.width-50 or self.x>scrnWidth+50:
            self.init()
    def init(self):
        self.wintype=random.choice(['rain','fruitNinja'])
        self.title(random.choice(['still using this computer?','fuck you','lol','memz','your computer has been fucked']))
        self.update()
        self.width=self.winfo_width()
        self.height=self.winfo_height()
        self.attributes("-alpha",0.25)
        self.attributes("-topmost",1)
        if self.wintype=='rain':
            self.rainInit()
        elif self.wintype=='fruitNinja':
            self.fruitNinjaInit()
        self.update()
        self.x=self.winfo_x()
        self.y=self.winfo_y()
        self.moving=True
        self.alpha=0.25
    def fruitNinjaInit(self):
        self.a=random.randint(-10,10)
        self.b=random.randint(-15,15)*0.1
        self.c=random.randint(-50,150)
        if random.randint(0,1)==0:
            self.move(-self.width,250)
            self.left=True
        else:
            self.move(scrnWidth,250)
            self.left=False
    def rainInit(self):
        self.move(random.randint(0,scrnWidth),-self.height-5)
        

windows=[]
scrnWidth=tk.Tk().winfo_screenwidth()
scrnHeight=tk.Tk().winfo_screenheight()
stopped=0
def mouseEnter(event):
    global stopped
    if stopped<0:
        event.widget.moving=False
        stopped=stopped+1
    for i in range(25,90,5):
        event.widget.setalpha(i)
        time.sleep(0.05)

def mouseLeave(event):
    global stopped
    if event.widget.moving==False:
        event.widget.moving=True
        stopped=stopped-1
    for i in range(90,25,-5):
        event.widget.setalpha(i)
        time.sleep(0.05)

def mouseLeaveStarter(event):
    a=threading.Thread(target=mouseLeave,args=[event])
    a.daemon=True
    a.start()
def mouseEnterStarter(event):
    a=threading.Thread(target=mouseEnter,args=[event])
    a.daemon=True
    a.start()
#g:y=-((x)/(25))^(2)+ (5x)/(25)+200
def newWin():
    win=window()
    win.init()
    win.bind("<Enter>",mouseEnterStarter)
    win.bind("<Leave>",mouseLeaveStarter)
    windows.append(win)
    #g:y=-((x)/(25))^(2)+ (5x)/(25)+200
    #            ^         ^        ^   Editable
    #            a         b        c
    #g:y=-(x/(25+a))^2+(5+b)x/25+200+c
    #  -10<=a<=10        -1.5<=b<=1.5    -50<=c<=150
    #winsound.Beep(random.randint(500,1200),random.randint(700,1200))
    win.mainloop()
    

def fruitNinja(win):
    x=win.x+10
    if win.left==False:
        x=scrnWidth-x
        y=scrnHeight-(-(x/(25+win.a))**2+(5+win.b)*x/25+200+win.c)-500
        x=win.x-10
    else:
        y=scrnHeight-(-(x/(25+win.a))**2+(5+win.b)*x/25+200+win.c)-500
    win.move(x,y)

def rain(win):
    if win.y<5:
        win.move(win.x,win.y+5)
    else:
        win.move(win.x,win.y*1.05+5)
while 1:
    if len(windows)<=25:
        a=threading.Thread(target=newWin)
        a.daemon=True
        a.start()
        time.sleep(0.2)
    for i in windows:
        if i.moving:
            if i.wintype=='rain':
                rain(i)
            elif i.wintype=='fruitNinja':
                fruitNinja(i)
        
        #time.sleep(0.01)
        

    
