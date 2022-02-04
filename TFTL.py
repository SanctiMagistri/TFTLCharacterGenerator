'''
Generator postaci bohaterów do gry fabularnej Tales From The Loop
Autor: Mateusz Wasyluk
'''

from tkinter import *
from tkinter.ttk import *

class Window(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.style = Style()
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.parent.title("TFTL Generator Postaci")
        self.style.theme_use('clam')
        self.style.configure('.', font=('Helvetica', 12))

def main():
    gui = Tk()
    gui.geometry('1280x720')
    Window(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()