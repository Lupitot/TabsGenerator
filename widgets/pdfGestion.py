from reportlab.pdfgen import canvas
   
class PdfGestion():
    def __init__(self, firstline, secondeLine, thirdLine, fourthLine, filename):
        self.filename = filename
        self.pdfContent = [firstline, secondeLine , thirdLine, fourthLine]
        self.create_pdf()

    def create_pdf(self):
        c = canvas.Canvas(self.filename)
        textobject = c.beginText()
        textobject.setTextOrigin(10, 730)
        for line in self.pdfContent:
            textobject.textLine(line)
        c.drawText(textobject)
        c.save()
        

    def set_filename(self, filename):
        self.filename = filename
        print("filename set to", filename)
        
        
        