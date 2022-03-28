'''
Generator postaci bohaterów do gry fabularnej Tales From The Loop
Autor: Mateusz Wasyluk
'''
import random
from tkinter import *
from tkinter.ttk import *

import character.generator
from character.classes import Hero, Kid, Bookworm, Geek, Hick, Jock, Popular, Rocker, Troublemaker, Weirdo
from copy import copy
from pdfGenerate import pdfGenerator

class Window(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.hero = Hero()
        self.archetypeHelper = Kid()

        self.randomizerButton = Button(self, text="Generator Postaci", command=character.generator.generate)

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

        # self.vertSeparator = Separator(self, orient=VERTICAL)

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
        self.skillInvestigateLabel = Label(self)
        self.skillInvestigateEntry = Spinbox(self)
        self.skillComprehendLabel = Label(self)
        self.skillComprehendEntry = Spinbox(self)
        self.skillEmpathizeLabel = Label(self)
        self.skillEmpathizeEntry = Spinbox(self)

        # self.vertSeparator2 = Separator(self, orient=VERTICAL)

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
        self.prevButton1 = Button(self)
        self.prevButton2 = Button(self)
        self.nextButton1 = Button(self)
        self.nextButton2 = Button(self)

        self.arrows = PhotoImage(file='arrows2.png')
        self.randomizeItem = Button(self, width=2, image=self.arrows)
        self.randomizeProblem = Button(self, width=2, image=self.arrows)
        self.randomizeDrive = Button(self, width=2, image=self.arrows)
        self.randomizePride = Button(self, width=2, image=self.arrows)
        self.randomizeAnchor = Button(self, width=2, image=self.arrows)
        self.randomizeName = Button(self, width=2, image=self.arrows)
        self.randomizeSong = Button(self, width=2, image=self.arrows)

        self.style = Style()
        self.parent = parent
        self.creatorButton = Button(self, text="Kreator Postaci", command=self.start_creator)
        self.initialize()

    def initialize(self):
        self.parent.title("TFTL Generator Postaci")
        self.style.theme_use('clam')
        self.style.configure('.', font=('Helvetica', 15))
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(3,weight=1)

        self.randomizerButton.grid(row=1, column=0, pady=10, padx=10, sticky=W + N)
        self.creatorButton.grid(row=1, column=1, pady=10, padx=10, sticky=W + N)
        self.mainSeparator.grid(row=2, column=0, columnspan=3, padx=10, sticky=N + S + E + W)

        self.archLabel.configure(text='Archetyp')
        self.archEntry.set('Mól książkowy')
        self.ageLabel.configure(text='Wiek')
        self.ageEntry.set(10)
        self.attribLabel.configure(text='Atrybuty', font=('Helvetica', 17))
        self.attribBodyLabel.configure(text='Ciało')
        self.attribBodyEntry.set(1)
        self.attribTechLabel.configure(text='Technologia')
        self.attribTechEntry.set(1)
        self.attribHeartLabel.configure(text='Serce')
        self.attribHeartEntry.set(1)
        self.attribMindLabel.configure(text='Umysł')
        self.attribMindEntry.set(1)

        self.skillLabel.configure(text='Umiejętności', font=('Helvetica',17))
        self.skillSneakLabel.configure(text='Skradanie')
        self.skillForceLabel.configure(text='Siła')
        self.skillMoveLabel.configure(text='Poruszanie się')
        self.skillTinkerLabel.configure(text='Majsterkowanie')
        self.skillProgramLabel.configure(text='Programowanie')
        self.skillCalculateLabel.configure(text='Obliczanie')
        self.skillContactLabel.configure(text='Kontakt')
        self.skillCharmLabel.configure(text='Urok')
        self.skillLeadLabel.configure(text='Dowodzenie')
        self.skillInvestigateLabel.configure(text='Śledztwo')
        self.skillComprehendLabel.configure(text='Zrozumienie')
        self.skillEmpathizeLabel.configure(text='Empatia')

        #
        self.itemLabel.configure(text='Ikoniczny przedmiot')
        self.problemLabel.configure(text='Problem')
        self.driveLabel.configure(text='Motywacja')
        self.prideLabel.configure(text='Duma')
        self.anchorLabel.configure(text='Opoka')
        self.nameLabel.configure(text='Imię')
        self.songLabel.configure(text='Ulubiona piosenka')
        self.topdfButton.configure(text='Generuj PDF')

        # self.randomizeItem.configure(text='Losuj')
        # self.randomizeProblem.configure(text='Losuj')
        # self.randomizeDrive.configure(text='Losuj')
        # self.randomizePride.configure(text='Losuj')
        # self.randomizeAnchor.configure(text='Losuj')
        # self.randomizeName.configure(text='Losuj')
        # self.randomizeSong.configure(text='Losuj')

    def validate_attrib(self):
        attrib = int(self.attribBodyEntry.get())
        attrib += int(self.attribTechEntry.get())
        attrib += int(self.attribHeartEntry.get())
        attrib += int(self.attribMindEntry.get())

        if attrib != int(self.ageEntry.get()):
            self.nextButton1.configure(state='disabled')
        else:
            self.nextButton1.configure(state='enabled')

    def validate_skill(self):


        skill = int(self.skillSneakEntry.get())
        skill += int(self.skillForceEntry.get())
        skill += int(self.skillMoveEntry.get())
        skill += int(self.skillTinkerEntry.get())
        skill += int(self.skillProgramEntry.get())
        skill += int(self.skillCalculateEntry.get())
        skill += int(self.skillContactEntry.get())
        skill += int(self.skillCharmEntry.get())
        skill += int(self.skillLeadEntry.get())
        skill += int(self.skillInvestigateEntry.get())
        skill += int(self.skillComprehendEntry.get())
        skill += int(self.skillEmpathizeEntry.get())

        if skill != 10:
            self.nextButton2.configure(state='disabled')
        else:
            self.nextButton2.configure(state='enabled')

    def show_page1(self):
        self.hide_page2()
        self.hide_page3()

        self.archLabel.grid(row=3, column=0, pady=0, padx=10, sticky=W)
        self.archEntry.grid(row=3, column=1, pady=0, padx=10, sticky=W + N)
        self.archEntry.configure(values=character.generator.archetype, font=('Helvetica', 12), width=17)
        self.ageLabel.grid(row=4, column=0, pady=0, padx=10, sticky=W)
        self.ageEntry.grid(row=4, column=1, pady=0, padx=10, sticky=W + N)
        self.ageEntry.configure(from_=10, to=15, wrap=True, font=('Helvetica', 12), width=2,
                                command=self.validate_attrib)

        self.attribLabel.grid(row=5, column=0, sticky=E)

        self.attribBodyLabel.grid(row=6, column=0, pady=0, padx=10, sticky=W)
        self.attribBodyEntry.grid(row=6, column=1, pady=0, padx=10, sticky=W + N)
        self.attribBodyEntry.configure(from_=1, to=5, wrap=True, font=('Helvetica', 12), width=2,
            command=self.validate_attrib)

        self.attribTechLabel.grid(row=7, column=0, pady=0, padx=10, sticky=W)
        self.attribTechEntry.grid(row=7, column=1, pady=0, padx=10, sticky=W + N)
        self.attribTechEntry.configure(from_=1, to=5, wrap=True, font=('Helvetica', 12), width=2,
            command=self.validate_attrib)

        self.attribHeartLabel.grid(row=8, column=0, pady=0, padx=10, sticky=W)
        self.attribHeartEntry.grid(row=8, column=1, pady=0, padx=10, sticky=W + N)
        self.attribHeartEntry.configure(from_=1, to=5, wrap=True, font=('Helvetica', 12), width=2,
            command=self.validate_attrib)

        self.attribMindLabel.grid(row=9, column=0, pady=0, padx=10, sticky=W)
        self.attribMindEntry.grid(row=9, column=1, pady=0, padx=10, sticky=W + N)
        self.attribMindEntry.configure(from_=1, to=5, wrap=True, font=('Helvetica', 12), width=2,
            command=self.validate_attrib)

        self.nextButton1.configure(text='Dalej', command=self.creator_page2, state='disabled')
        # self.nextButton1.grid(row=16, column=1, pady=30, padx=10, sticky=E + N + S)
        self.nextButton1.place(x=270, y=445)
        self.validate_attrib()

    def hide_page1(self):
        self.archLabel.grid_forget()
        self.archEntry.grid_forget()
        self.ageLabel.grid_forget()
        self.ageEntry.grid_forget()
        self.attribLabel.grid_forget()
        self.attribBodyLabel.grid_forget()
        self.attribBodyEntry.grid_forget()
        self.attribTechLabel.grid_forget()
        self.attribTechEntry.grid_forget()
        self.attribHeartLabel.grid_forget()
        self.attribHeartEntry.grid_forget()
        self.attribMindLabel.grid_forget()
        self.attribMindEntry.grid_forget()
        self.nextButton1.place_forget()

    def show_page2(self):
        self.hide_page1()
        self.hide_page3()

        self.skillLabel.grid(row=3, column=0, sticky=E)

        self.skillSneakLabel.grid(row=4, column=0, padx=10, sticky=W)
        self.skillSneakEntry.grid(row=4, column=1, padx=10, sticky=W)

        self.skillForceLabel.grid(row=5, column=0, padx=10, sticky=W)
        self.skillForceEntry.grid(row=5, column=1, padx=10, sticky=W)

        self.skillMoveLabel.grid(row=6, column=0, padx=10, sticky=W)
        self.skillMoveEntry.grid(row=6, column=1, padx=10, sticky=W)

        self.skillTinkerLabel.grid(row=7, column=0, padx=10, sticky=W)
        self.skillTinkerEntry.grid(row=7, column=1, padx=10, sticky=W)

        self.skillProgramLabel.grid(row=8, column=0, padx=10, sticky=W)
        self.skillProgramEntry.grid(row=8, column=1, padx=10, sticky=W)

        self.skillCalculateLabel.grid(row=9, column=0, padx=10, sticky=W)
        self.skillCalculateEntry.grid(row=9, column=1, padx=10, sticky=W)

        self.skillContactLabel.grid(row=10, column=0, padx=10, sticky=W)
        self.skillContactEntry.grid(row=10, column=1, padx=10, sticky=W)

        self.skillCharmLabel.grid(row=11, column=0, padx=10, sticky=W)
        self.skillCharmEntry.grid(row=11, column=1, padx=10, sticky=W)

        self.skillLeadLabel.grid(row=12, column=0, padx=10, sticky=W)
        self.skillLeadEntry.grid(row=12, column=1, padx=10, sticky=W)

        self.skillInvestigateLabel.grid(row=13, column=0, padx=10, sticky=W)
        self.skillInvestigateEntry.grid(row=13, column=1, padx=10, sticky=W)

        self.skillComprehendLabel.grid(row=14, column=0, padx=10, sticky=W)
        self.skillComprehendEntry.grid(row=14, column=1, padx=10, sticky=W)

        self.skillEmpathizeLabel.grid(row=15, column=0, padx=10, sticky=W)
        self.skillEmpathizeEntry.grid(row=15, column=1, padx=10, sticky=W)

        self.prevButton1.configure(text='Wróć', command=self.show_page1)
        # self.prevButton1.grid(row=16, column=0, pady=30, padx=10, sticky=W + N + S)
        self.prevButton1.place(x=10, y=445)
        self.nextButton2.configure(text="Dalej", command=self.show_page3, state='disabled')
        self.nextButton2.place(x=270, y=445)
        # self.nextButton2.grid(row=16, column=1, pady=30, padx=10, sticky=W + N + S)



        self.validate_skill()

    def hide_page2(self):
        self.skillLabel.grid_forget()
        self.skillSneakLabel.grid_forget()
        self.skillSneakEntry.grid_forget()
        self.skillForceLabel.grid_forget()
        self.skillForceEntry.grid_forget()
        self.skillMoveLabel.grid_forget()
        self.skillMoveEntry.grid_forget()
        self.skillTinkerLabel.grid_forget()
        self.skillTinkerEntry.grid_forget()
        self.skillProgramLabel.grid_forget()
        self.skillProgramEntry.grid_forget()
        self.skillCalculateLabel.grid_forget()
        self.skillCalculateEntry.grid_forget()
        self.skillContactLabel.grid_forget()
        self.skillContactEntry.grid_forget()
        self.skillCharmLabel.grid_forget()
        self.skillCharmEntry.grid_forget()
        self.skillLeadLabel.grid_forget()
        self.skillLeadEntry.grid_forget()
        self.skillInvestigateLabel.grid_forget()
        self.skillInvestigateEntry.grid_forget()
        self.skillComprehendLabel.grid_forget()
        self.skillComprehendEntry.grid_forget()
        self.skillEmpathizeLabel.grid_forget()
        self.skillEmpathizeEntry.grid_forget()
        self.prevButton1.place_forget()
        self.nextButton2.place_forget()

    def creator_page2(self):
        self.get_values_p1()



        self.skillSneakEntry.set(0)
        self.skillForceEntry.set(0)
        self.skillMoveEntry.set(0)
        self.skillTinkerEntry.set(0)
        self.skillProgramEntry.set(0)
        self.skillCalculateEntry.set(0)
        self.skillContactEntry.set(0)
        self.skillCharmEntry.set(0)
        self.skillLeadEntry.set(0)
        self.skillInvestigateEntry.set(0)
        self.skillComprehendEntry.set(0)
        self.skillEmpathizeEntry.set(0)

        self.show_page2()

        if self.hero.archetype == 'Mól książkowy':
            self.archetypeHelper = copy(Bookworm)
        elif self.hero.archetype == 'Geek komputerowy':
            self.archetypeHelper = copy(Geek)
        elif self.hero.archetype == 'Prowincjusz':
            self.archetypeHelper = copy(Hick)
        elif self.hero.archetype == 'Osiłek':
            self.archetypeHelper = copy(Jock)
        elif self.hero.archetype == 'Popularny dzieciak':
            self.archetypeHelper = copy(Popular)
        elif self.hero.archetype == 'Rocker':
            self.archetypeHelper = copy(Rocker)
        elif self.hero.archetype == 'Urwis':
            self.archetypeHelper = copy(Troublemaker)
        elif self.hero.archetype == 'Dziwak':
            self.archetypeHelper = copy(Weirdo)

        if 'Skradanie' in self.archetypeHelper.skills:
            self.skillSneakEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                           command=self.validate_skill)
        else:
            self.skillSneakEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                           command=self.validate_skill)

        if 'Siła' in self.archetypeHelper.skills:
            self.skillForceEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                           command=self.validate_skill)
        else:
            self.skillForceEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                           command=self.validate_skill)

        if 'Poruszanie się' in self.archetypeHelper.skills:
            self.skillMoveEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                          command=self.validate_skill)
        else:
            self.skillMoveEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                          command=self.validate_skill)

        if 'Majsterkowanie' in self.archetypeHelper.skills:
            self.skillTinkerEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                            command=self.validate_skill)
        else:
            self.skillTinkerEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                            command=self.validate_skill)

        if 'Programowanie' in self.archetypeHelper.skills:
            self.skillProgramEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                             command=self.validate_skill)
        else:
            self.skillProgramEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                             command=self.validate_skill)

        if 'Obliczanie' in self.archetypeHelper.skills:
            self.skillCalculateEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                               command=self.validate_skill)
        else:
            self.skillCalculateEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                               command=self.validate_skill)

        if 'Kontakt' in self.archetypeHelper.skills:
            self.skillContactEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                             command=self.validate_skill)
        else:
            self.skillContactEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                             command=self.validate_skill)

        if 'Urok' in self.archetypeHelper.skills:
            self.skillCharmEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                           command=self.validate_skill)
        else:
            self.skillCharmEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                           command=self.validate_skill)

        if 'Dowodzenie' in self.archetypeHelper.skills:
            self.skillLeadEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                          command=self.validate_skill)
        else:
            self.skillLeadEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                          command=self.validate_skill)

        if 'Śledztwo' in self.archetypeHelper.skills:
            self.skillInvestigateEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                                 command=self.validate_skill)
        else:
            self.skillInvestigateEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                                 command=self.validate_skill)

        if 'Zrozumienie' in self.archetypeHelper.skills:
            self.skillComprehendEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                                command=self.validate_skill)
        else:
            self.skillComprehendEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                                command=self.validate_skill)

        if 'Empatia' in self.archetypeHelper.skills:
            self.skillEmpathizeEntry.configure(from_=0, to=3, wrap=True, font=('Helvetica', 12), width=2,
                                               command=self.validate_skill)
        else:
            self.skillEmpathizeEntry.configure(from_=0, to=1, wrap=True, font=('Helvetica', 12), width=2,
                                               command=self.validate_skill)

    def show_page3(self):
        self.hide_page2()

        self.itemLabel.grid(row=3, column=0, padx=10, sticky=W)
        self.itemEntry.grid(row=3, column=1, padx=10, sticky=W)

        self.problemLabel.grid(row=4, column=0, padx=10, sticky=W)
        self.problemEntry.grid(row=4, column=1, padx=10, sticky=W)

        self.driveLabel.grid(row=5, column=0, padx=10, sticky=W)
        self.driveEntry.grid(row=5, column=1, padx=10, sticky=W)

        self.prideLabel.grid(row=6, column=0, padx=10, sticky=W)
        self.prideEntry.grid(row=6, column=1, padx=10, sticky=W)

        self.anchorLabel.grid(row=7, column=0, padx=10, sticky=W)
        self.anchorEntry.grid(row=7, column=1, padx=10, sticky=W)

        self.nameLabel.grid(row=8, column=0, padx=10, sticky=W)
        self.nameEntry.grid(row=8, column=1, padx=10, sticky=W)

        self.songLabel.grid(row=9, column=0, padx=10, sticky=W)
        self.songEntry.grid(row=9, column=1, padx=10, sticky=W)

        self.prevButton2.configure(text='Wróć', command=self.show_page2)
        # self.prevButton2.grid(row=10, column=0, padx=10, sticky=W)
        self.prevButton2.place(x=10, y=445)
        self.topdfButton.configure(command=self.create_pdf)
        # self.topdfButton.grid(row=10, column=1, sticky=W)
        self.topdfButton.place(x=270, y=445)

        self.randomizeItem.grid(row=3, column=2, padx=0, sticky=W)
        self.randomizeProblem.grid(row=4, column=2, padx=0, sticky=W)
        self.randomizeDrive.grid(row=5, column=2, padx=0, sticky=W)
        self.randomizePride.grid(row=6, column=2, padx=0, sticky=W)
        self.randomizeAnchor.grid(row=7, column=2, padx=0, sticky=W)
        self.randomizeName.grid(row=8, column=2, padx=0, sticky=W)
        self.randomizeSong.grid(row=9, column=2, padx=0, sticky=W)

        self.randomizeItem.configure(command=self.randItem)
        self.randomizeProblem.configure(command=self.randProblem)
        self.randomizeDrive.configure(command=self.randDrive)
        self.randomizePride.configure(command=self.randPride)
        self.randomizeAnchor.configure(command=self.randAnchor)
        self.randomizeName.configure(command=self.randName)
        self.randomizeSong.configure(command=self.randSong)

    def hide_page3(self):
        self.itemLabel.grid_forget()
        self.itemEntry.grid_forget()
        self.problemLabel.grid_forget()
        self.problemEntry.grid_forget()
        self.driveLabel.grid_forget()
        self.driveEntry.grid_forget()
        self.prideLabel.grid_forget()
        self.prideEntry.grid_forget()
        self.anchorLabel.grid_forget()
        self.anchorEntry.grid_forget()
        self.nameLabel.grid_forget()
        self.nameEntry.grid_forget()
        self.songLabel.grid_forget()
        self.songEntry.grid_forget()
        self.prevButton2.place_forget()
        self.topdfButton.place_forget()
        self.randomizeItem.grid_forget()
        self.randomizeProblem.grid_forget()
        self.randomizeDrive.grid_forget()
        self.randomizePride.grid_forget()
        self.randomizeAnchor.grid_forget()
        self.randomizeName.grid_forget()
        self.randomizeSong.grid_forget()

    def creator_page3(self):
        self.show_page3()

    def start_creator(self):
        self.show_page1()

    def get_values_p1(self):
        self.hero.archetype = self.archEntry.get()
        self.hero.age = self.ageEntry.get()
        self.hero.attributes[0] = self.attribBodyEntry.get()
        self.hero.attributes[1] = self.attribTechEntry.get()
        self.hero.attributes[2] = self.attribHeartEntry.get()
        self.hero.attributes[3] = self.attribMindEntry.get()

    def get_values_p2(self):
        self.hero.skills[0] = self.skillSneakEntry.get()
        self.hero.skills[1] = self.skillForceEntry.get()
        self.hero.skills[2] = self.skillMoveEntry.get()
        self.hero.skills[3] = self.skillTinkerEntry.get()
        self.hero.skills[4] = self.skillProgramEntry.get()
        self.hero.skills[5] = self.skillCalculateEntry.get()
        self.hero.skills[6] = self.skillContactEntry.get()
        self.hero.skills[7] = self.skillCharmEntry.get()
        self.hero.skills[8] = self.skillLeadEntry.get()
        self.hero.skills[9] = self.skillInvestigateEntry.get()
        self.hero.skills[10] = self.skillComprehendEntry.get()
        self.hero.skills[11] = self.skillEmpathizeEntry.get()

    def get_values_p3(self):
        self.hero.iconicItem = self.itemEntry.get()
        self.hero.problem = self.problemEntry.get()
        self.hero.drive = self.driveEntry.get()
        self.hero.pride = self.prideEntry.get()
        self.hero.anchor = self.anchorEntry.get()
        self.hero.name = self.nameEntry.get()
        self.hero.favSong = self.songEntry.get()

    def randItem(self):
        self.itemEntry.delete(0,END)
        self.itemEntry.insert(0, random.choice(self.archetypeHelper.iconicItem))

    def randProblem(self):
        self.problemEntry.delete(0, END)
        self.problemEntry.insert(0, random.choice(self.archetypeHelper.problem))

    def randDrive(self):
        self.driveEntry.delete(0, END)
        self.driveEntry.insert(0, random.choice(self.archetypeHelper.drive))

    def randPride(self):
        self.prideEntry.delete(0, END)
        self.prideEntry.insert(0,random.choice(self.archetypeHelper.pride))

    def randAnchor(self):
        self.anchorEntry.delete(0, END)
        self.anchorEntry.insert(0,random.choice(self.archetypeHelper.anchor))

    def randName(self):
        self.nameEntry.delete(0,END)
        temp = character.generator.genFromFile('names.txt')
        self.nameEntry.insert(0, temp[:-1])

    def randSong(self):
        self.songEntry.delete(0, END)
        temp = character.generator.genFromFile('songs.txt')
        self.songEntry.insert(0, temp[:-1])

    def create_pdf(self):
        self.get_values_p3()
        pdfGenerator(self.hero)


def main():
    gui = Tk()
    gui.geometry('420x500')
    Window(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()
