from fpdf import FPDF
from hero import Hero

class PDF(FPDF):
    def header(self):
        # logo
        self.image('tftl-logo.png', 40, 5, 130)
        self.ln(20)

def pdfGenerator(hero):
    # Layout ('P','L')
    # Unit ('mm','cm','in')
    # format ('A3', 'A4' (default), 'A5', 'Letter', Legal, (100,150)
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.set_margins(left=5, top=5, right=5)
    pdf.set_auto_page_break(auto=False)

    # https://sourceforge.net/projects/dejavu/
    pdf.add_font('DejaVu', fname='DejaVuSansCondensed-Bold.ttf')
    pdf.set_font('DejaVu', size=12)

    # 1st line
    pdf.set_fill_color(0,0,0)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(60, 10, 'ATRYBUTY', border=True, fill=True)

    pdf.set_fill_color(255, 241, 218)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(70, 10, f'IMIĘ: {hero.name}', border=True, fill=True)
    pdf.cell(70, 10, f'ARCHETYP: {hero.archetype}', border=True, ln=True, fill=True)

    # 2nd line





    pdf.output('test.pdf')
    # print(Hero.name)
# pdfGenerator()