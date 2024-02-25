from django.shortcuts import render

from django.conf import settings
from django.http import FileResponse

from weasyprint import HTML, CSS
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

import io

# Create your views here.
def generate_pdf(request):
    filename='documents/file.pdf'
    # HTML(string='''
    # <h1>The title</h1>
    # <p>Content goes here
    # ''').write_pdf(filename)
    
    # CSS(string='@page { size: A3; margin: 1cm }')

    HTML('https://www.google.com/').write_pdf(filename)

    return render(request,'csv.html')


def generate_pdf2(request):
    filename='file2.pdf'

    c = canvas.Canvas(settings.PDF_ROOT+filename)

    c.drawString(0,0, 'Hello world')

    c.setStrokeColorRGB(0,255,0)
    c.setFillColorRGB(255,0,0)
    c.circle(2*inch,2*inch,50, fill=1, stroke=1)
    c.setStrokeColorRGB(0,255,255)
    c.setFillColorRGB(255,0,255)
    c.rect(2*inch, 2*inch,8*inch,10*inch, fill=1, stroke=1)
    c.line(2*inch,2*inch,8*inch,10*inch)

    c.showPage()
    c.save()

    return render(request,'csv.html')

def generate_pdf_download(request):
    filename='file2.pdf'

    buffer = io.BytesIO()

    c = canvas.Canvas(buffer)

    c.drawString(0,0, 'Hello world')

    c.setStrokeColorRGB(0,255,0)
    c.setFillColorRGB(255,0,0)
    c.circle(2*inch,2*inch,50, fill=1, stroke=1)
    c.setStrokeColorRGB(0,255,255)
    c.setFillColorRGB(255,0,255)
    c.rect(2*inch, 2*inch,8*inch,10*inch, fill=1, stroke=1)
    c.line(2*inch,2*inch,8*inch,10*inch)

    c.showPage()
    c.save()

    buffer.seek(0)

    return FileResponse(buffer, filename=filename)

def download_file(request):
    filename='documents/pdf/file2.pdf'

    return FileResponse(open(filename,'rb'), filename=filename)
