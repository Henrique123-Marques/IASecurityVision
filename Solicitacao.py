from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', '', 25.0)
pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Olá, meu nome é Henrique Marques", border=0)
pdf.output('test.pdf', 'F')