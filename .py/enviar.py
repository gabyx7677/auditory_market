#===========================================================================
# Enviar el PDF por correo


import time
import pyautogui
from pywinauto import Application
import smtplib, os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\gabri\OneDrive\Escritorio\proyectos\auditory_market\notebook\.env")

EMAIL_USER = os.getenv("ALERT_EMAIL")   # tu correo remitente
EMAIL_PASS = os.getenv("ALERT_PASS")   # tu contraseña / app password
EMAIL_TO   = 'gabriel.garcia@utp.edu.co'     # destinatario (o varios separados por coma)

# Ruta del PDF (el que ya generaste con tu script)
pdf_file = r"C:\Users\gabri\OneDrive\Escritorio\proyectos\auditory_market\dashboards\guardados\dashboard.pdf"

def enviar_informe():
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO
    msg["Subject"] = "📊 Informe automático - Dashboard actualizado"

    # Cuerpo del correo
    body = "Hola,\n\nAdjunto encontrarás el informe actualizado en PDF.\n\nSaludos."
    msg.attach(MIMEText(body, "plain"))

    # Adjuntar archivo PDF
    with open(pdf_file, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f'attachment; filename="{os.path.basename(pdf_file)}"')
        msg.attach(part)

    # Enviar correo (ejemplo con Gmail)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, EMAIL_TO.split(","), msg.as_string())
        server.quit()
        print("✅ Correo enviado correctamente.")
    except Exception as e:
        print("❌ Error al enviar correo:", e)

# Ejecutar envío
enviar_informe()