'''
Generator postaci bohaterów do gry fabularnej Tales From The Loop
Autor: Mateusz Wasyluk
'''

from tkinter import *
from tkinter.ttk import *

class Hero:
    archtype = []
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

class Window(Frame):
    archtype = ['Mól książkowy',
                'Geek komputerowy',
                'Prowincjusz',
                'Osiłek',
                'Popularny dzieciak',
                'Rocker',
                'Urwis',
                'Dziwak']
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