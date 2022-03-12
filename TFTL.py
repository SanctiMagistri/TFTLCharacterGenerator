'''
Generator postaci bohaterów do gry fabularnej Tales From The Loop
Autor: Mateusz Wasyluk
'''
from copy import copy
from tkinter import *
from tkinter.ttk import *
import os, random

class Hero:
    archetype = []
    age = 0
    attributes = {'Ciało': 0,
                  'Technologia': 0,
                  'Serce': 0,
                  'Umysł': 0}
    luckPoints = 0
    skills = {'Skradanie': 0,
              'Siła': 0,
              'Poruszanie się': 0,
              'Majsterkowanie': 0,
              'Programowanie': 0,
              'Obliczanie': 0,
              'Kontakt': 0,
              'Urok': 0,
              'Dowodzenie': 0,
              'Śledztwo': 0,
              'Zrozumienie': 0,
              'Empatia': 0}
    iconicItem = ''
    problem = ''
    motivation = ''
    pride = ''
    anchor = ''
    name = ''
    favSong = ''

class Kid:
    iconicItem = []
    problem = []
    drive = []
    pride = []
    anchor = []
    skills = []

Bookworm = Kid()
Bookworm.iconicItem = ['Piesek Leszek',
                       'Encyklopedia',
                       'Lupa']
Bookworm.problem = ['Nikt nie chce mi powiedzieć jak zginął mój tata.',
                    'Moja siostra jest poważnie chora.',
                    'Tamten dziwny mężczyzna ciagle za mną łazi.']
Bookworm.drive = ['Pragnę znaleźć odpowiedzi na zagadki tego świata.',
                  'Potrzebuję czegoś do przechwałek.']
Bookworm.pride = ['Jestem najmądrzejszym dzieciakiem w szkole.',
                  'Niczego się nie boję.']
Bookworm.anchor = ['Mama',
                   'Tata',
                   'Nauczyciel',
                   'Miejscowy pisarz']
Bookworm.skills = ['Obliczanie',
                   'Śledztwo',
                   'Zrozumienie']

Geek = Kid()
Geek.iconicItem = ['Komputer',
                   'Kieszonkowy kalkulator',
                   'Zabawkowy miecz świetlny']
Geek.problem = ['Szkolne osiłki mnie zaczepiają.',
                'Moi rodzice ciagle się kłócą.',
                'Moja sympatia nie wie o moim istnieniu.']
Geek.drive = ['Kocham zagadki.',
              'Presja rówieśników zmusza mnie do działania.']
Geek.pride = ['Gdy jest katastrofa, nigdy się nie cofam.',
              'Jestem najmądrzejszym dzieciakiem w szkole.']
Geek.anchor = ['Matka',
               'Ojciec',
               'Właściciel sklepu z komiksami']
Geek.skills = ['Obliczanie',
               'Programowanie',
               'Zrozumienie']

Hick = Kid()
Hick.iconicItem = ['Owczarek niemiecki',
                   'Łom',
                   'Traktor']
Hick.problem = ['Ktoś truje nasze zwierzęta.',
                'Mama/tata nie chce zaakceptować, że jest chory/a.',
                'Przypadkiem kogoś poważnie zraniłem/łam.']
Hick.drive = ['Na świecie jest więcej rzeczy, których oko nie dostrzega.',
              'Potrzebują mnie.']
Hick.pride = ['Moje maszyny kiedyś podbiją świat.',
              'Pomagam innym ludziom.']
Hick.anchor = ['Tata',
               'Mama',
               'Znajomy myśliwy',
               'Instruktor jeździectwa']
Hick.skills = ['Siła',
               'Poruszanie się',
               'Majsterkowanie']

Jock = Kid()
Jock.iconicItem = ['Kij bejsbolowy',
                   'Kij hokejowy',
                   'BMX']
Jock.problem = ['Mój brat odmawia wyjścia z pokoju od czasu wypadku.',
                'Mój nauczyciel nienawidzi mnie.',
                'Nie czytam zbyt dobrze i chcą mnie przenieść do klasy specjalnej.']
Jock.drive = ['Jestem w tym dla dreszczu emocji.',
              'Należałoby to zrobić.']
Jock.pride = ['Mój ojciec jest strażakiem.',
              'Nikt nie nazywa mnie tchórzem!']
Jock.anchor = ['Ojciec',
               'Matka',
               'Trener drużyny',
               'Brat',
               'Siostra']
Jock.skills = ['Siła',
               'Poruszanie się',
               'Kontakt']

Popular = Kid()
Popular.iconicItem = ['Paczka gum do rzucia',
                      'Pamiętnik z pikantnymi sekretami',
                      'Puszka spreju do włosów']
Popular.problem = ['Moja ciotka mieszka w naszej piwnicy i jest szalona',
                   'Mama ma kochanka.',
                   'Tata ma kochankę.',
                   'Mój rywal wie, co próbuję ukryć.']
Popular.drive = ['Ucieczka od ciężaru popularności to prawdziwe wytchnienie.',
                 'Niecierpię sekretów.']
Popular.pride = ['Wszyscy mnie lubią.',
                 'Wiem Wszystko o wszystkich.']
Popular.anchor = ['Starsze rodzeństwo',
                  'Mama',
                  'Tata',
                  'Sławny przyjaciel rodziny']
Popular.skills = ['Kontakt',
                  'Urok',
                  'Dowodzenie']

Rocker = Kid()
Rocker.iconicItem = ['Boombox',
                     'Gitara elektryczna',
                     'Skórzana kurtka']
Rocker.problem = ['Moi rodzice się rozwodzą.',
                  'Kradnę pieniadze.',
                  'Niespełniona miłość']
Rocker.drive = ['Robię to w imię miłości.',
                'Głód wszystkiego w życiu.']
Rocker.pride = ['Gram na gitarze.',
                'Stanąłem/Stanęłam w obronie mojego przyjaciela/przyjaciółki.']
Rocker.anchor = ['Nauczyciel muzyki',
                 'Starszy brat',
                 'Starsza siostra',
                 'Ten gość ze sklepu muzycznego']
Rocker.skills = ['Poruszanie się',
                 'Urok',
                 'Empatia']

Troublemaker = Kid()
Troublemaker.iconicItem = ['Zapalniczka i papierosy',
                           'Nóż',
                           'Deskorolka']
Troublemaker.problem = ['Rodzice uważają, że jestem do niczego.',
                        'Moja matka dużo pije.',
                        'Mój ojciec duzo pije.',
                        'Mamy problemy z pieniędzmi.']
Troublemaker.drive = ['Zrobię wszystko, by wyjść z domu.',
                      'Moi przyjaciele i to, co robimy to jedyna nie zepsuta rzecz w moim życiu.']
Troublemaker.pride = ['Pomogłem/am ptakowi ze złamanym skrzydłem.',
                      'Stanąłem/Stanęłam w obronie nauczyciela.']
Troublemaker.anchor = ['Szkolny woźny',
                       'Szkolna woźna',
                       'Szkolny pedagog',
                       'Babcia']
Troublemaker.skills = ['Siła',
                       'Skradanie',
                       'Dowodzenie']

Weirdo = Kid()
Weirdo.iconicItem = ['Brzytwa',
                     'Szkicownik',
                     'Szczur']
Weirdo.problem = ['Mój ojciec jest komunistą.',
                  'Mój brat robi dziwne rzeczy w swoim pokoju.',
                  'Byłem/am gnębiony/a w szkole.']
Weirdo.drive = ['Mówią, że jestem najciekawsza osobą na świecie.',
                'Ciągnie mnie do wszystkiego co dziwne lub inne.']
Weirdo.pride = ['Nie jestem heteroseksualny/a.',
                'Mama mówi, że jestem piękny/a.']
Weirdo.anchor = ['Babcia',
                 'Rodzic innego Dzieciaka',
                 'Sąsiad',
                 'Sąsiadka']
Weirdo.skills = ['Skradanie',
                 'Śledztwo',
                 'Empatia']

class Window(Frame):
    archetype = ['Mól książkowy',
                'Geek komputerowy',
                'Prowincjusz',
                'Osiłek',
                'Popularny dzieciak',
                'Rocker',
                'Urwis',
                'Dziwak']
    def __init__(self,parent):
        super().__init__(parent)

        self.randomizerButton = Button(self, text="Generator Postaci", command=self.generate)
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

        self.motivLabel = Label(self)
        self.motivEntry = Entry(self)

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

    def genArchetype(self):
        archetype = random.choice(self.archetype)
        return archetype

    def genAge(self):
        return random.randint(10,15)

    def genAttribValues(self, attribVal, age):
        while (sum(attribVal) != age):
            attribVal[0] = random.randint(1, 5)
            attribVal[1] = random.randint(1, 5)
            attribVal[2] = random.randint(1, 5)
            attribVal[3] = random.randint(1, 5)
        return attribVal

    def genSkillPoints(self, sum, maxSkillPoint):
        if sum > 0:
            points = random.randint(0, maxSkillPoint)
        else:
            points = 0

        return points

    def genFromFile(self, file_name):
        total_bytes = os.stat(file_name).st_size
        random_point = random.randint(0, total_bytes)
        file = open(file_name, encoding='utf-8')
        file.seek(random_point)
        file.readline()
        return file.readline()

    def generate(self):
        # initialize hero and archetype object
        global archetypeHelper
        hero = Hero()

        # randomize archetype and copy archetype object
        hero.archetype = self.genArchetype()
        if hero.archetype == 'Mól książkowy':
            archetypeHelper = copy(Bookworm)
        elif hero.archetype == 'Geek komputerowy':
            archetypeHelper = copy(Geek)
        elif hero.archetype == 'Prowincjusz':
            archetypeHelper = copy(Hick)
        elif hero.archetype == 'Osiłek':
            archetypeHelper = copy(Jock)
        elif hero.archetype == 'Popularny dzieciak':
            archetypeHelper = copy(Hick)
        elif hero.archetype == 'Rocker':
            archetypeHelper = copy(Rocker)
        elif hero.archetype == 'Urwis':
            archetypeHelper = copy(Troublemaker)
        elif hero.archetype == 'Dziwak':
            archetypeHelper = copy(Weirdo)

        # set Hero's age
        hero.age = self.genAge()

        # randomize Hero's attribute points
        attribVal = [0, 0, 0, 0]
        attribVal = self.genAttribValues(attribVal, hero.age)
        hero.attributes = {'Ciało': attribVal[0],
                           'Technologia': attribVal[1],
                           'Serce': attribVal[2],
                           'Umysł': attribVal[3]}

        # set Hero's luck points
        hero.luckPoints = 15 - hero.age

        # randomize Hero's skill points
        skillSum = 10
        for key in hero.skills.keys():
            if key in archetypeHelper.skills:
                skillPoints = self.genSkillPoints(skillSum, 3)
                skillSum -= skillPoints
            else:
                skillPoints = self.genSkillPoints(skillSum, 1)
                skillSum -= skillPoints

        # randomize iconic item, problem, drive, pride and anchor
        hero.iconicItem = random.choice(archetypeHelper.iconicItem)
        hero.problem = random.choice(archetypeHelper.problem)
        hero.motivation = random.choice(archetypeHelper.drive)
        hero.pride = random.choice(archetypeHelper.pride)
        hero.anchor = random.choice(archetypeHelper.anchor)

        # randomize name
        hero.name = self.genFromFile('names.txt')

        # randomize song
        hero.favSong = self.genFromFile('songs.txt')

        print(hero.archetype)
        print(hero.age)
        print(hero.attributes)
        print(hero.luckPoints)
        print(hero.skills)
        print(hero.iconicItem)
        print(hero.problem)
        print(hero.motivation)
        print(hero.pride)
        print(hero.anchor)
        print(hero.name)
        print(hero.favSong)

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
        self.archEntry.configure(values=self.archetype, font=('Helvetica',12), width=17)
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

        self.motivLabel.configure(text='Motywacja')
        self.motivLabel.grid(row=5, column=7, padx=10, sticky=W)
        self.motivEntry.configure()
        self.motivEntry.grid(row=5, column=8, padx=10, sticky=W)

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
    gui.geometry('1280x720')
    Window(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()