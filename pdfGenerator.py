from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import Paragraph
import textwrap
from reportlab.pdfbase.pdfmetrics import stringWidth

from tkinter import messagebox
from common import *

import subprocess

def writeWithWrap(towrite, pcanvas, start_height, row_height, start_width, num_of_char):
    wrap_text = textwrap.wrap(towrite, width=num_of_char)
    index_row = 0
    for mini_row in wrap_text:
        pcanvas.drawString(start_width, start_height - index_row * row_height * cm, mini_row)

        index_row = index_row + 1

    return start_height - index_row * row_height * cm


pdfmetrics.registerFont(TTFont("TimesNewRoman", "times.ttf"))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Bold', 'timesbd.ttf'))
registerFontFamily('TimesNewRoman', normal='TimesNewRoman', bold='TimesNewRoman-Bold')


def drawSpecial(text, canvas, style, wraponloc, drawonloc):
    para = Paragraph(text, style)
    para.wrapOn(canvas, wraponloc[0], wraponloc[1])
    para.drawOn(canvas, drawonloc[0], drawonloc[1])


def drawSpecialV2(text, canvas, fontsize, wraponloc, drawonloc, align=TA_LEFT, textcolor='black', try_align_middle=False):
    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.fontName = 'TimesNewRoman'
    styleN.fontSize = fontsize
    styleN.alignment = align
    styleN.textColor = textcolor

    para = Paragraph(text, styleN)
    para.wrapOn(canvas, wraponloc[0], wraponloc[1])

    line_count = len(para.blPara.lines)
    line_height = para.height / line_count

    x_align = 0
    if try_align_middle:
        textwidth = stringWidth(text, "TimesNewRoman", fontsize)
        x_align = int(textwidth / 2)

    para.drawOn(canvas, drawonloc[0] - x_align, drawonloc[1] - int(line_height * (line_count - 1)))



def generate_prescription(hospital_name, hospital_phone, hospital_address, patient_name, patient_dob,
                          patient_weight, patient_gender, patient_id, patient_address, doctor_comment,
                          day_time, doctor_name, doctor_phone, parent_info, patient_cmnd, prescription_ID,
                          list_diagnose, list_medicine):
    output_path = getConfig()['pdf_output_path'] + '/' + prescription_ID + ".pdf"

    c = canvas.Canvas(output_path, pagesize=A5)
    c.setFont("TimesNewRoman", 10)

    page_width, page_height = A5

    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.fontName = 'TimesNewRoman'
    styleN.fontSize = 9
    styleN.alignment = TA_LEFT

    start_heigh = 20
    row_heigh = 0.4

    drawSpecialV2(f'<b>{hospital_name}</b>', c, 9, (page_width - 2 * cm, page_height), (1 * cm, start_heigh * cm))
    drawSpecialV2(f"<b><u>Điện Thoại: {hospital_phone}</u></b>", c, 9, (page_width - 2 * cm, page_height), (1 * cm, (start_heigh - row_heigh) * cm))
    drawSpecialV2(f"Địa Chỉ: <b>{hospital_address}</b>", c, 9, (page_width - 2 * cm, page_height), (1 * cm, (start_heigh - row_heigh * 2) * cm))

    drawSpecialV2("<b>ĐƠN THUỐC</b>", c, 15, (page_width - 2 * cm, page_height), (cm, (start_heigh - row_heigh * 4) * cm), align=TA_CENTER, textcolor='red')

    start_heigh = (start_heigh - row_heigh * 5.5)
    row_heigh = 0.35

    drawSpecialV2(f"Họ tên: <b>{patient_name}</b>", c, 9, (page_width - 2 * cm, page_height), (1 * cm, start_heigh * cm))
    drawSpecialV2(f"Ngày sinh: <b>{patient_dob}</b>", c, 9, (page_width - 2 * cm, page_height), (1 * cm, (start_heigh - row_heigh) * cm))
    drawSpecialV2(f"Cân nặng: <b>{patient_weight}</b>", c, 9, (page_width - 2 * cm, page_height), (1 * cm, (start_heigh - row_heigh) * cm), align=TA_CENTER)
    drawSpecialV2(f"Giới tính: <b>{patient_gender}</b>", c, 9, (page_width - 2 * cm, page_height), (page_width - 4 * cm, (start_heigh - row_heigh) * cm))
    drawSpecialV2(f"Mã số thẻ bảo hiểm (nếu có): <b>{patient_id}</b>", c, 9, (page_width - 2 * cm, page_height), (1 * cm, (start_heigh - row_heigh * 2) * cm))
    drawSpecialV2(f"Địa chỉ liên hệ: <b>{patient_address}</b>", c, 9, (page_width - 2 * cm, page_height), (1 * cm, (start_heigh - row_heigh * 3) * cm))


    c.drawString(1 * cm, (start_heigh - row_heigh * 4) * cm, f"Chẩn đoán:")

    list_processed_dianose = []
    for row in list_diagnose:
        list_processed_dianose.append([Paragraph(x.get(), styleN) for x in row])

    data = [
        ["Mã", "Chẩn đoán", "Kết luận"]
    ] + list_processed_dianose

    table_diagnose = Table(data, colWidths=[1.3*cm, int((page_width - 3.25 * cm) / 2), int((page_width - 3.25 * cm) / 2)])
    table_diagnose.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'TimesNewRoman'),
        ('FONTNAME', (0, 0), (-1, 0), 'TimesNewRoman-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
    ]))
    table_diagnose.wrapOn(c, *A5)
    width_diagnose, height_diagnose = table_diagnose.wrap(*A5)
    table_diagnose.drawOn(c, 1 * cm, (start_heigh - row_heigh * 4.5) * cm - height_diagnose)

    start_heigh = (start_heigh - row_heigh * 5.5) * cm - height_diagnose

    c.drawString(1 * cm, start_heigh, f"Thuốc điều trị:")

    current_index = 1
    list_processed_medicine = []
    for row in list_medicine:
        current_parsed_row = [Paragraph(x.get(), styleN) for x in row]
        list_processed_medicine.append([Paragraph(str(current_index), styleN),
                                       current_parsed_row[1],
                                       current_parsed_row[2],
                                       current_parsed_row[3],
                                       current_parsed_row[4],
                                       current_parsed_row[5]])

        current_index = current_index + 1

    data_medicine = [
        ["STT", "Hoạt chất", "Tên thuốc", "Đơn vị tính", "Số lượng", "Cách dùng"]
    ] + list_processed_medicine

    table_medicine = Table(data_medicine, colWidths=[0.75*cm, int((page_width - 7.25 * cm) / 2), int((page_width - 7.25 * cm) / 2), 1.5*cm, 1.5*cm, 1.5*cm])
    table_medicine.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'TimesNewRoman'),
        ('FONTNAME', (0, 0), (-1, 0), 'TimesNewRoman-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
    ]))

    table_medicine.wrapOn(c, *A5)
    width_medicine, height_medicine = table_medicine.wrap(*A5)
    table_medicine.drawOn(c, 1 * cm, start_heigh - row_heigh * cm - height_medicine + 0.2 * cm)

    start_heigh = start_heigh - row_heigh * 2 * cm - height_medicine + 0.2 * cm

    start_heigh = writeWithWrap(f"Lời dặn của bác sĩ: {doctor_comment}", c, start_heigh, row_heigh, 1 * cm, 80) + row_heigh * cm

    # c.drawString(1 * cm, start_heigh, f"Lời dặn của bác sĩ: {doctor_comment}")

    c.drawCentredString(page_width - 4 * cm, start_heigh - row_heigh * 2 * cm, f"{day_time}")
    c.drawCentredString(page_width - 4 * cm, start_heigh - row_heigh * 3 * cm, "Bác sỹ/Y sỹ khám bệnh")
    c.drawCentredString(page_width - 4 * cm, start_heigh - row_heigh * 4 * cm, "(Ký, ghi rõ họ tên)")

    drawSpecialV2(f"<b>Bác sĩ: {doctor_name}</b>", c, 9, (page_width - 2 * cm, page_height), (page_width - 3.5 * cm, start_heigh - row_heigh * 10 * cm), try_align_middle=True)

    c.drawString(1 * cm, start_heigh - row_heigh * 11 * cm, f"Khám lại xin mang theo đơn này")

    drawSpecialV2(f"Số điện thoại liên hệ: <u>{doctor_phone}</u>", c, 9, (page_width - 2 * cm, page_height), (1 * cm, start_heigh - row_heigh * 12.3 * cm))

    start_heigh = writeWithWrap(f"Tên bố hoặc mẹ của trẻ hoặc người đưa trẻ đến khám bệnh, chữa bệnh: {parent_info}", c,
                                start_heigh - row_heigh * 13 * cm, row_heigh, 1 * cm, 80) + row_heigh * cm

    c.drawString(1 * cm, start_heigh - row_heigh * 1 * cm, f"Căn cước công dân/ chứng minh nhân dân người nhận thuốc: {patient_cmnd}")

    c.save()
    return output_path


def savePrescriptionAsPdf(data):
    config = getConfig()

    output_path = generate_prescription(config['hospital_name'],
                          config['hospital_phone'],
                          config['hospital_address'],
                          data['patientName'],
                          data['date_of_birth'],
                          data['weight'],
                          data['sex_var'],
                          data['insurance_id'],
                          data['address'],
                          data['loi_dan_entry'],
                          data['ngay_gio_ke_don'],
                          data['sdt_nguoi_kham'],
                          data['sdt_nguoi_kham'],
                          data['guardian_info'],
                          data['patient_id'],
                          data['prescription_ID'],
                          data['chandoan'],
                          data['don_thuoc'])

    answer = messagebox.askquestion("Chú ý", "Bạn có muốn mở đơn thuốc?")
    if answer == "yes":
        subprocess.Popen([output_path], shell=True)


# generate_prescription("Bệnh Viện II  Lâm Đồng", "0633123456", "Số 263 Trần Quốc Toản, Phường B'Lao, Thành phố Bảo Lộc, Lâm Đồng",
#                       "Patient Name", "12/1/1992", "80kg", "Nam", "213124123213",
#                       "Patient Address", "Doctor's Comment Doctor's Comment Doctor's Comment Doctor's Comment Doctor's Comment Doctor's Comment Doctor's Comment", "08:32 21/10/2022",
#                       "Trần Trương Nguyễn Thanh Thanh", "092432321", "Mother, AA Doctor's Comment Doctor's Comment Doctor's Comment Doctor's", "")


