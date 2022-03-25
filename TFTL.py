'''
Generator postaci bohaterów do gry fabularnej Tales From The Loop
Autor: Mateusz Wasyluk
'''



from tkinter import *
from tkinter.ttk import *

import character.generator
from character.classes import Hero

from pdfGenerate import pdfGenerator




class Window(Frame):

    def __init__(self,parent):
        super().__init__(parent)

        self.randomizerButton = Button(self, text="Generator Postaci", command=character.generator.generate())
        self.creatorButton = Button(self, text="Kreator Postaci")
        self.mainSeparator = Separator(self, orient=HORIZONTAL)

        self.archLabel = Label(self)
        self.archEntry = Combobox(self)

        self.ageLabel = Label(self)
        self.ageEntry = Spinbox(self)

        self.attribLabel = Label(self)
        self.attribBodyLabel = Label(self)
        self.attribBodyEntry = Spinbox(self)
        self.attribTechLabel = Label(self)
        self.attribTechEntry = Spinbox(self)
        self.attribHeartLabel = Label(self)
        self.attribHeartEntry = Spinbox(self)
        self.attribMindLabel = Label(self)
        self.attribMindEntry = Spinbox(self)


        self.vertSeparator = Separator(self, orient=VERTICAL)

        self.skillLabel = Label(self)
        self.skillSneakLabel = Label(self)
        self.skillSneakEntry = Spinbox(self)
        self.skillForceLabel = Label(self)
        self.skillForceEntry = Spinbox(self)
        self.skillMoveLabel = Label(self)
        self.skillMoveEntry = Spinbox(self)
        self.skillTinkerLabel = Label(self)
        self.skillTinkerEntry = Spinbox(self)
        self.skillProgramLabel = Label(self)
        self.skillProgramEntry = Spinbox(self)
        self.skillCalculateLabel = Label(self)
        self.skillCalculateEntry = Spinbox(self)
        self.skillContactLabel = Label(self)
        self.skillContactEntry = Spinbox(self)
        self.skillCharmLabel = Label(self)
        self.skillCharmEntry = Spinbox(self)
        self.skillLeadLabel = Label(self)
        self.skillLeadEntry = Spinbox(self)
        self.skillInvestigateLeadLabel = Label(self)
        self.skillInvestigateLeadEntry = Spinbox(self)
        self.skillComprehendLabel = Label(self)
        self.skillComprehendEntry = Spinbox(self)
        self.skillEmpathizeLabel = Label(self)
        self.skillEmpathizeEntry = Spinbox(self)


        self.vertSeparator2 = Separator(self, orient=VERTICAL)

        self.itemLabel = Label(self)
        self.itemEntry = Entry(self)

        self.problemLabel = Label(self)
        self.problemEntry = Entry(self)

        self.driveLabel = Label(self)
        self.driveEntry = Entry(self)

        self.prideLabel = Label(self)
        self.prideEntry = Entry(self)

        self.anchorLabel = Label(self)
        self.anchorEntry = Entry(self)

        self.nameLabel = Label(self)
        self.nameEntry = Entry(self)

        self.songLabel = Label(self)
        self.songEntry = Entry(self)

        self.topdfButton = Button(self)



        self.style = Style()
        self.parent = parent
        self.initialize()



    def initialize(self):
        self.parent.title("TFTL Generator Postaci")
        self.style.theme_use('clam')
        self.style.configure('.', font=('Helvetica', 15))
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(9,weight=1)

        self.randomizerButton.grid(row=1, column=0, pady=10, padx=10, sticky=W + N)
        self.creatorButton.grid(row=1, column=8, pady=10, padx=10, sticky=E + N)
        self.mainSeparator.grid(row=2, column=0, columnspan=9,padx=10, sticky=N+S+E+W)


        self.archLabel.configure(text='Archetyp')
        self.archLabel.grid(row=3, column=0, pady=0, padx=10, sticky=W)
        self.archEntry.configure(values=character.generator.archetype, font=('Helvetica',12), width=17)
        self.archEntry.grid(row=3, column=1, pady=0, padx=10, sticky=W+N)

        self.ageLabel.configure(text='Wiek')
        self.ageLabel.grid(row=4, column=0, pady=0, padx=10, sticky=W)
        self.ageEntry.configure(from_=10, to=15, wrap=True, font=('Helvetica',12), width=2)
        self.ageEntry.grid(row=4, column=1, pady=0, padx=10, sticky=W+N)

        self.attribLabel.configure(text='Atrybuty', font=('Helvetica',17))
        self.attribLabel.grid(row=5, column=0, sticky=E)

        self.attribBodyLabel.configure(text='Ciało')
        self.attribBodyLabel.grid(row=6, column=0, pady=0, padx=10, sticky=W)
        self.attribBodyEntry.grid(row=6, column=1, pady=0, padx=10, sticky=W+N)
        self.attribBodyEntry.configure(from_=1, to=5, wrap=True, font=('Helvetica',12), width=2)

        self.attribTechLabel.configure(text='Technologia')
        self.attribTechLabel.grid(row=7, column=0, pady=0, padx=10, sticky=W)
        self.attribTechEntry.grid(row=7, column=1, pady=0, padx=10, sticky=W+N)
        self.attribTechEntry.configure(from_=1, to=5, wrap=True, font=('Helvetica',12), width=2)

        self.attribHeartLabel.configure(text='Serce')
        self.attribHeartLabel.grid(row=8, column=0, pady=0, padx=10, sticky=W)
        self.attribHeartEntry.grid(row=8, column=1, pady=0, padx=10, sticky=W+N)
        self.attribHeartEntry.configure(from_=1, to=5, wrap=True, font=('Helvetica',12), width=2)

        self.attribMindLabel.configure(text='Umysł')
        self.attribMindLabel.grid(row=9, column=0, pady=0, padx=10, sticky=W)
        self.attribMindEntry.grid(row=9, column=1, pady=0, padx=10, sticky=W+N)
        self.attribMindEntry.configure(from_=1, to=5, wrap=True, font=('Helvetica',12), width=2)


        self.vertSeparator.grid(row=2, column=4, pady=10,rowspan=26, sticky=N+S+W+E)

        self.skillLabel.configure(text='Umiejętności', font=('Helvetica',17))
        self.skillLabel.grid(row=3, column=4, sticky=E)

        self.skillSneakLabel.configure(text='Skradanie')
        self.skillSneakLabel.grid(row=4, column=4, padx=10, sticky=W)
        self.skillSneakEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillSneakEntry.grid(row=4, column=5, padx=10, sticky=E)

        self.skillForceLabel.configure(text='Siła')
        self.skillForceLabel.grid(row=5, column=4, padx=10, sticky=W)
        self.skillForceEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillForceEntry.grid(row=5, column=5, padx=10, sticky=W)

        self.skillMoveLabel.configure(text='Poruszanie się')
        self.skillMoveLabel.grid(row=6, column=4, padx=10, sticky=W)
        self.skillMoveEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillMoveEntry.grid(row=6, column=5, padx=10, sticky=W)

        self.skillTinkerLabel.configure(text='Majsterkowanie')
        self.skillTinkerLabel.grid(row=7, column=4, padx=10, sticky=W)
        self.skillTinkerEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillTinkerEntry.grid(row=7, column=5, padx=10, sticky=W)

        self.skillProgramLabel.configure(text='Programowanie')
        self.skillProgramLabel.grid(row=8, column=4, padx=10, sticky=W)
        self.skillProgramEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillProgramEntry.grid(row=8, column=5, padx=10, sticky=W)

        self.skillCalculateLabel.configure(text='Obliczanie')
        self.skillCalculateLabel.grid(row=9, column=4, padx=10, sticky=W)
        self.skillCalculateEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillCalculateEntry.grid(row=9, column=5, padx=10, sticky=W)

        self.skillContactLabel.configure(text='Kontakt')
        self.skillContactLabel.grid(row=10, column=4, padx=10, sticky=W)
        self.skillContactEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillContactEntry.grid(row=10, column=5, padx=10, sticky=W)

        self.skillCharmLabel.configure(text='Urok')
        self.skillCharmLabel.grid(row=11, column=4, padx=10, sticky=W)
        self.skillCharmEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillCharmEntry.grid(row=11, column=5, padx=10, sticky=W)

        self.skillLeadLabel.configure(text='Dowodzenie')
        self.skillLeadLabel.grid(row=12, column=4, padx=10, sticky=W)
        self.skillLeadEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillLeadEntry.grid(row=12, column=5, padx=10, sticky=W)

        self.skillInvestigateLeadLabel.configure(text='Śledztwo')
        self.skillInvestigateLeadLabel.grid(row=13, column=4, padx=10, sticky=W)
        self.skillInvestigateLeadEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillInvestigateLeadEntry.grid(row=13, column=5, padx=10, sticky=W)

        self.skillComprehendLabel.configure(text='Zrozumienie')
        self.skillComprehendLabel.grid(row=14, column=4, padx=10, sticky=W)
        self.skillComprehendEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillComprehendEntry.grid(row=14, column=5, padx=10, sticky=W)

        self.skillEmpathizeLabel.configure(text='Empatia')
        self.skillEmpathizeLabel.grid(row=15, column=4, padx=10, sticky=W)
        self.skillEmpathizeEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica',12), width=2)
        self.skillEmpathizeEntry.grid(row=15, column=5, padx=10, sticky=W)


        self.vertSeparator2.grid(row=2, column=7, pady=10, rowspan=26, sticky=N + S + W + E)

        self.itemLabel.configure(text='Ikoniczny przedmiot')
        self.itemLabel.grid(row=3, column=7, padx=10, sticky=W)
        self.itemEntry.configure()
        self.itemEntry.grid(row=3, column=8, padx=10, sticky=W)

        self.problemLabel.configure(text='Problem')
        self.problemLabel.grid(row=4, column=7, padx=10, sticky=W)
        self.problemEntry.configure()
        self.problemEntry.grid(row=4, column=8, padx=10, sticky=W)

        self.driveLabel.configure(text='Motywacja')
        self.driveLabel.grid(row=5, column=7, padx=10, sticky=W)
        self.driveEntry.configure()
        self.driveEntry.grid(row=5, column=8, padx=10, sticky=W)

        self.prideLabel.configure(text='Duma')
        self.prideLabel.grid(row=6, column=7, padx=10, sticky=W)
        self.prideEntry.configure()
        self.prideEntry.grid(row=6, column=8, padx=10, sticky=W)

        self.anchorLabel.configure(text='Opoka')
        self.anchorLabel.grid(row=7, column=7, padx=10, sticky=W)
        self.anchorEntry.configure()
        self.anchorEntry.grid(row=7, column=8, padx=10, sticky=W)

        self.nameLabel.configure(text='Imię')
        self.nameLabel.grid(row=8, column=7, padx=10, sticky=W)
        self.nameEntry.configure()
        self.nameEntry.grid(row=8, column=8, padx=10, sticky=W)

        self.songLabel.configure(text='Ulubiona piosenka')
        self.songLabel.grid(row=9, column=7, padx=10, sticky=W)
        self.songEntry.configure()
        self.songEntry.grid(row=9, column=8, padx=10, sticky=W)

        self.topdfButton.configure(text='Generuj PDF')
        self.topdfButton.grid(sticky=E)



def main():
    gui = Tk()
    gui.geometry('1000x500')
    Window(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()