import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.rl_config import defaultPageSize
from reportlab.lib.pagesizes import landscape
from reportlab.pdfbase.pdfmetrics import stringWidth

PAGE_WIDTH  = landscape(defaultPageSize)


def drawText(c, text, font, points, x, y):

    width = stringWidth(text, font, points)
    textObject = c.beginText()
    textObject.setTextOrigin(x, y)  
    textObject.setFont(font, points)
    textObject.textLine(text)  
    c.drawText(textObject)


def centerText(c, text, font, points, y):

    width = stringWidth(text, font, points)
    x = (PAGE_WIDTH[0] - width) / 2.0
    drawText(c, text, font, points, x, y)


def createReport(name, city, startSeconds):

    dateString = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
    startTime = (datetime.datetime.today() - datetime.timedelta(seconds=startSeconds)).strftime('%H-%M-%S')

    path = 'reports/report_{}_{}.pdf'.format(name, dateString)
    c = canvas.Canvas(path, pagesize=landscape(defaultPageSize))

    # c.drawImage('images/border.png', 0, 0, 21*cm, 29.7*cm)

    centerText(c, 'Reporte de HEATS-Board', 'Times-BoldItalic', 38, 19*cm)
    centerText(c, '{} {}'.format(name, city), 'Times-BoldItalic', 32, 17.7*cm)
    centerText(c, 'Gráficos de Procesamiento {}'.format(dateString[:10]), 'Times-Italic', 24, 16.7*cm)
    drawText(c, f'Hora de inicio: {startTime.replace("-",":")}', 'Times-Italic', 16, 2.5*cm, 15*cm)
    drawText(c, f'Hora final: {dateString[11:].replace("-",":")}', 'Times-Italic', 16, 2.5*cm, 14*cm)
    #drawText(c, '(10 Hz - 24 kHz, logarithmisch)', 'Times-Italic', 16, 11.5*cm, 4.5*cm)

    # c.drawImage('images/fft.png', 2.3*cm, 11.8*cm, 16*cm, 6.8*cm, mask='auto')
    c.drawImage('images/spectrogram.png', 1.9*cm, 2.5*cm, 26*cm, 10*cm)

    c.drawImage('images/cujae_logo.png', 28*cm, 0.5*cm, 1.5*cm, 1.5*cm, mask='auto')

    c.showPage()
    c.save()

    return path
