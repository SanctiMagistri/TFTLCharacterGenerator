from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # logo
        self.image('tftl-logo.png', 40, 5, 130)
        self.ln(20)

def pdfGenerator(hero):

    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.set_margins(left=5, top=5, right=5)
    pdf.set_auto_page_break(auto=False)

    # https://sourceforge.net/projects/dejavu/
    pdf.add_font('DejaVu', fname='DejaVuSansCondensed-Bold.ttf')
    pdf.set_font('DejaVu', size=10)

    # 1st line
    pdf.set_fill_color(0,0,0)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(58, 10, 'ATRYBUTY', border=True, fill=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(2,10)
    pdf.cell(70, 10, f'IMIĘ: {hero.name}', border=True, fill=True)
    pdf.cell(70, 10, f'ARCHETYP: {hero.archetype}', border=True, ln=True, fill=True)
    print(hero.name)

    # 2nd line
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0,0,0)
    pdf.cell(48, 10, 'Ciało', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10,10, f'{list(hero.attributes.values())[0]}', border=True)


    pdf.set_font_size(10)
    pdf.cell(2,10)
    pdf.set_fill_color(255, 241, 218)
    pdf.cell(70, 10, f'Wiek: {hero.age}', border=True, fill=True)
    pdf.set_fill_color(249, 189, 141)
    pdf.cell(35, 10, 'Punkty szczęścia: ', border=True, fill=True)
    pdf.set_fill_color(255,255,255)
    pdf.cell(7, 10, border=True, fill=True)
    pdf.cell(7, 10, border=True, fill=True)
    pdf.cell(7, 10, border=True, fill=True)
    pdf.cell(7, 10, border=True, fill=True)
    pdf.cell(7, 10, border=True, fill=True, ln=True)

    # 3rd line
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Technologia', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.attributes.values())[1]}', border=True)

    pdf.set_font_size(10)
    pdf.cell(2, 10)
    pdf.set_fill_color(255, 241, 218)
    pdf.set_font_size(7)
    pdf.cell(90, 10, f'Motywacja: {hero.drive}', border=True, fill=True)
    pdf.set_fill_color(255, 241, 218)
    pdf.cell(50, 10, f'Opoka: {hero.anchor}', border=True, fill=True, ln=True)

    # 4th line
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font_size(10)
    pdf.cell(48, 10, 'Serce', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.attributes.values())[2]}', border=True)

    pdf.set_font_size(10)
    pdf.cell(2, 10)
    pdf.set_fill_color(255, 241, 218)
    pdf.cell(140, 10, f'Problem: {hero.problem}', border=True, fill=True, ln=True)

    # 5th line
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Umysł', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.attributes.values())[3]}', border=True)

    pdf.set_font_size(10)
    pdf.cell(2, 10)
    pdf.set_fill_color(255, 241, 218)
    pdf.cell(130, 10, f'Duma: {hero.pride}', border=True, fill=True)
    pdf.cell(10, 10, border=True, ln=True)

    # 6th line
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(58, 10, 'STANY', border=True, fill=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(2, 10)
    pdf.cell(140, 10, 'Opis: ', border=True, fill=True, ln=True)

    # 7th line
    pdf.set_fill_color(253, 230, 210)
    pdf.cell(48, 10, 'Smutny', border=True, fill=True)
    pdf.cell(10, 10, border=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.cell(2, 10)
    pdf.cell(140, 10, f'Ulubiona piosenka: {hero.favSong}', border=True, fill=True, ln=True)

    # 8th line
    pdf.set_fill_color(249, 189, 141)
    pdf.cell(48, 10, 'Przestraszony', border=True, fill=True)
    pdf.cell(10, 10, border=True)

    pdf.set_fill_color(0,0,0)
    pdf.set_text_color(255,255,255)
    pdf.cell(2, 10)
    pdf.cell(140, 10, 'RELACJE', border=True, fill=True, ln=True)

    # 9th line
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Zmęczony', border=True, fill=True)
    pdf.cell(10, 10, border=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.cell(2, 10)
    pdf.cell(140, 10, 'Dzieciak 1:', border=True, fill=True, ln=True)

    # 10th line
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Ranny', border=True, fill=True)
    pdf.cell(10, 10, border=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.cell(2, 10)
    pdf.cell(140, 10, 'Dzieciak 2:', border=True, fill=True, ln=True)

    # 11th line
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Załamany', border=True, fill=True)
    pdf.cell(10, 10, border=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.cell(2, 10)
    pdf.cell(140, 10, 'Dzieciak 3:', border=True, fill=True, ln=True)

    # 12th line
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(58, 10, 'UMIEJĘTNOŚCI', border=True, fill=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(2, 10)
    pdf.cell(140, 10, 'Dzieciak 4: ', border=True, fill=True, ln=True)

    # 13th line
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Skradanie (Ciało)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[0]}', border=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(2, 10)
    pdf.set_font_size(10)
    pdf.cell(140, 10, 'BN 1: ', border=True, fill=True, ln=True)

    # 14th line
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Siła (Ciało)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[1]}', border=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.cell(2, 10)
    pdf.set_font_size(10)
    pdf.cell(140, 10, 'BN 2:', border=True, fill=True, ln=True)

    # 15th line
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Poruszanie się (Ciało)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[2]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font_size(10)
    pdf.cell(69, 10, 'PRZEDMIOT                             BONUS', border=True, fill=True)
    pdf.cell(2, 10)
    pdf.cell(69, 10, 'KRYJÓWKA', border=True, fill=True, ln=True)

    # 16th line
    pdf.set_font_size(10)
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Majsterkowanie (Tech)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[3]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(254, 221, 158)
    pdf.set_font_size(7)
    pdf.cell(69, 10, f'Ikoniczny przedmiot: {hero.iconicItem} +2', border=True, fill=True)
    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.cell(69, 10, border=True, fill=True, ln=True)

    # 17th line
    pdf.set_font_size(10)
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Programowanie (Tech)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[4]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_font_size(7)
    pdf.cell(59, 10, '', border=True, fill=True)
    pdf.cell(10, 10, border=True)
    pdf.cell(2, 10)
    pdf.cell(69, 10, border=True, fill=True, ln=True)

    # 18th line
    pdf.set_font_size(10)
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Obliczanie (Tech)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[5]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_font_size(7)
    pdf.cell(59, 10, '', border=True, fill=True)
    pdf.cell(10, 10, border=True)
    pdf.cell(2, 10)
    pdf.cell(69, 10, border=True, fill=True, ln=True)

    # 19th line
    pdf.set_font_size(10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Kontakt (Serce)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[6]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_font_size(7)
    pdf.cell(59, 10, '', border=True, fill=True)
    pdf.cell(10, 10, border=True)
    pdf.cell(2, 10)
    pdf.cell(69, 10, border=True, fill=True, ln=True)

    # 20th line
    pdf.set_font_size(10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Urok (Serce)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[7]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_font_size(7)
    pdf.cell(59, 10, '', border=True, fill=True)
    pdf.cell(10, 10, border=True)
    pdf.cell(2, 10)
    pdf.cell(69, 10, border=True, fill=True, ln=True)

    # 21st line
    pdf.set_font_size(10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Dowodzenie (Serce)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[8]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_font_size(7)
    pdf.cell(59, 10, '', border=True, fill=True)
    pdf.cell(10, 10, border=True)
    pdf.cell(2, 10)
    pdf.cell(69, 10, border=True, fill=True, ln=True)

    # 22nd line
    pdf.set_font_size(10)
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Śledztwo (Umysł)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[9]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font_size(10)
    pdf.cell(140, 10, 'NOTATKI', border=True, fill=True, ln=True)

    # 23rd line
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(48, 10, 'Zrozumienie (Umysł)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[10]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.cell(140, 10, border=True, fill=True, ln=True)

    # 24th line
    pdf.set_fill_color(249, 189, 141)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font_size(10)
    pdf.cell(48, 10, 'Empatia (Umysł)', border=True, fill=True)
    pdf.set_font_size(15)
    pdf.cell(10, 10, f'{list(hero.skills.values())[11]}', border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.cell(140, 10, border=True, fill=True, ln=True)

    # 25th line
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(58, 10, 'DOŚWIADCZENIE', border=True, fill=True)


    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(140, 10, border=True, fill=True, ln=True)

    # 25th line
    for i in range(0,10):
        pdf.cell(5.8,10, border=True)

    pdf.cell(2, 10)
    pdf.set_fill_color(253, 230, 210)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(140, 10, border=True, fill=True, ln=True)

    pdf.output('Karta_Postaci.pdf')