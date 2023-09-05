from tkinter import *
import time


def main():
    global root, label

    root = Tk()
    Bottom = Frame(root)
    Bottom.pack(side=BOTTOM)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=BOTTOM)
    label = Label(root, background="black", font=(
        "arial", 25), foreground="cyan", borderwidth=10)
    label.pack(side=BOTTOM, pady=7)
    Top = Frame(root)
    Top.pack(side=BOTTOM)
    
    Start = Button(Bottom, text='START/RESUME',
                   command=stopWatch.Start, width=10, height=1, bg="chocolate1")
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='PAUSE',
                  command=stopWatch.Stop, width=2, height=1, bg="chocolate1")
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='RESET',
                   command=stopWatch.Reset, width=2, height=1, bg="chocolate1")
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='CLOSE',
                  command=stopWatch.Exit, width=2, bg="chocolate1", height=1)
    Exit.pack(side=LEFT)
    root.config(bg="grey")
    ttime()
    root.mainloop()


def ttime():
    string = time.strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000, ttime)


class StopWatch(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=(
            "arial", 25), fg="royal blue", bg="black")
        self.SetTime(self.nextTime)
        timeText.pack(pady=5, padx=10)

    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))

    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1

    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Exit(self):
        root.destroy()

    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)


if __name__ == '__main__':
    main()
