from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("TimesNewRoman", "times.ttf"))

def create_prescription_pdf(hospital_name, hospital_phone, hospital_address,
                            title, patient_name, patient_dob, patient_weight,
                            patient_gender, patient_id, patient_address,
                            diagnosis, medicine, doctor_comment,
                            day_time, doctor_name):
    # Create a new PDF file
    pdf = canvas.Canvas("prescription.pdf", pagesize=letter)

    # Set the font and font size
    pdf.setFont("TimesNewRoman", 12)

    # Add the hospital information
    pdf.drawString(100, 750, hospital_name)
    pdf.drawString(100, 735, 'Điện thoại:' + hospital_phone)
    pdf.drawString(100, 720, 'Địa chỉ: ' + hospital_address)

    # Add the title
    pdf.drawString(250, 650, title)

    # Add the patient information
    pdf.drawString(100, 600, "Patient Name: {}".format(patient_name))
    pdf.drawString(100, 585, "Patient DOB: {}".format(patient_dob))
    pdf.drawString(100, 570, "Patient Weight: {}".format(patient_weight))
    pdf.drawString(100, 555, "Patient Gender: {}".format(patient_gender))
    pdf.drawString(100, 540, "Patient ID: {}".format(patient_id))
    pdf.drawString(100, 525, "Patient Address: {}".format(patient_address))

    # Add the diagnosis table
    pdf.drawString(100, 475, "Diagnosis")
    pdf.drawString(150, 460, "CODE")
    pdf.drawString(250, 460, "DIAGNOSIS")
    pdf.drawString(400, 460, "CONCLUSION")
    y = 445
    for row in diagnosis:
        code = row[0]
        diag = row[1]
        concl = row[2]
        pdf.drawString(150, y, code)
        pdf.drawString(250, y, diag)
        pdf.drawString(400, y, concl)
        y -= 15

    # Add the medicine table
    pdf.drawString(100, y - 30, "Medicine")
    pdf.drawString(150, y - 45, "Index")
    pdf.drawString(200, y - 45, "Medical Name")
    pdf.drawString(300, y - 45, "Count Type")
    pdf.drawString(400, y - 45, "Count")
    pdf.drawString(500, y - 45, "How to Use")

    y -= 60

    for row in medicine:
        index = row[0]
        medical_name = row[1]
        count_type = row[2]
        count = row[3]
        how_to_use = row[4]

        pdf.drawString(150, y, str(index))
        pdf.drawString(200, y, str(medical_name))
        pdf.drawString(300, y, str(count_type))
        pdf.drawString(400, y, str(count))
        pdf.drawString(500, y, str(how_to_use))

        y -= 15

    # Add the doctor's comment
    y -= 30
    pdf.drawString(100, y, "Doctor's Comment:")

    y -= 15
    for line in doctor_comment:
        if len(line) > 80:
            line1 = line[:80]
            line2 = line[80:]
            if len(line2) > 80:
                line2 = line2[:80] + "-"
            else:
                y -= 15
                line2 = ""
            pdf.drawString(150, y, line1)
            y -= 15
            pdf.drawString(150, y, line2)
        else:
            y -= 15
            pdf.drawString(150, y, line)

    # Add the day time and doctor's name
    pdf.drawString(100, 100, "Day Time: {}".format(day_time))
    pdf.drawString(100, 85, "Doctor's Name: {}".format(doctor_name))

    # Save the PDF
    pdf.save()


hospital_name = "ABC Hospital"
hospital_phone = "123-456-7890"
hospital_address = "123 Main St, Anytown USA"
title = "Prescription"
patient_name = "John Smith"
patient_dob = "01/01/1970"
patient_weight = "150 lbs"
patient_gender = "Male"
patient_id = "12345"
patient_address = "456 Elm St, Anytown USA"
diagnosis = [("A01.0", "Cholera due to Vibrio cholerae 01, biovar cholerae", "Mild dehydration"),
             ("B20", "Human immunodeficiency virus [HIV] disease", "Asymptomatic HIV infection status"),
             ("C34.90", "Malignant neoplasm of unspecified part of unspecified bronchus or lung", "Metastatic lung cancer")]
medicine = [(1, "Aspirin", "Tablet", 30, "Take one tablet by mouth every 4 hours as needed for pain"),
            (2, "Ibuprofen", "Tablet", 30, "Take one tablet by mouth every 6 hours as needed for pain")]
doctor_comment = ["Patient should rest and drink plenty of fluids.",
                  "Follow up with primary care physician in 1 week."]
day_time = "06/25/2023 11:37 AM"
doctor_name = "Dr. Jane Doe"

create_prescription_pdf(hospital_name, hospital_phone, hospital_address,
                        title, patient_name, patient_dob, patient_weight,
                        patient_gender, patient_id, patient_address,
                        diagnosis, medicine, doctor_comment,
                        day_time, doctor_name)
