from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('TimesNewRoman', 'times.ttf'))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Bold', 'timesbd.ttf'))

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

styles = getSampleStyleSheet()
style = styles["Normal"]
style.fontName = 'TimesNewRoman'
style.fontSize = 10
style.alignment = TA_LEFT
style.leading = 12
text = 'This is a <b>bold</b> word.'
para = Paragraph(text, style)
paraStyle = para.style
paraStyle.wordWrap = 'CJK'
paraStyle.add('b', paraStyle.fontName, 'TimesNewRoman-Bold')
