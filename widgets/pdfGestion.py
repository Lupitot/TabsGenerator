from reportlab.pdfgen import canvas
   
class PdfGestion():
    def __init__(self, pdfContent, filename):
        self.filename = filename
        self.pdfContent = pdfContent
        self.create_pdf()

    def create_pdf(self):
        c = canvas.Canvas(self.filename)
        textobject = c.beginText()
        textobject.setTextOrigin(10, 730)
        textobject.textLines(' '.join(self.pdfContent))
        c.drawText(textobject)
        c.save()
        
        
        