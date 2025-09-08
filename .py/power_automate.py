# Script para abrir Power BI, exportar a PDF y enviar por correo

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

pbix_file = r"C:\Users\gabri\OneDrive\Escritorio\proyectos\auditory_market\dashboards\dahsboard.pbix"
pbidesktop_path = r"C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe"

print("🚀 Abriendo Power BI...")
app = Application(backend="uia").start(f'"{pbidesktop_path}" "{pbix_file}"')
main = app.window(title_re=r".*dahsboard.*|.*\.pbix.*")
main.wait('visible', timeout=180)
main.set_focus()
time.sleep(3)

# Forzar foco con click
rect = main.rectangle()
pyautogui.click(rect.left + 50, rect.top + 50)
time.sleep(6)

# ALT → activar KeyTips
print("🎹 ALT...")
pyautogui.press("alt")
time.sleep(2)

# A → abrir Archivo
print("🎹 A (Archivo)...")
pyautogui.press("a")
time.sleep(1.3)

# Enter → entrar al menú Archivo
print("🎹 Enter (entrar al menú Archivo)...")
pyautogui.press("enter")
time.sleep(0.9)

# 7 veces ↓ → Exportar
print("🎹 7 veces ↓ (hasta Exportar)...")
pyautogui.press("down", presses=7, interval=0.4)
time.sleep(0.3)

# Enter → abrir Exportar
print("🎹 Enter (abrir Exportar)...")
pyautogui.press("enter")
time.sleep(0.3)

# ↓ → Exportar a PDF
print("🎹 ↓ (seleccionar Exportar a PDF)...")
pyautogui.press("down")
time.sleep(0.3)

# Enter → abrir PDF en Chrome
print("🎹 Enter (abrir Exportar a PDF)...")
pyautogui.press("enter")
time.sleep(8)

# --- CTRL+S en Chrome para abrir el diálogo Guardar ---
print("🖫 En Chrome: CTRL + S...")
time.sleep(1)          # pequeño respiro para que Chrome termine de cargar el PDF
pyautogui.hotkey("ctrl", "s")
time.sleep(1)          # espera a que aparezca el cuadro "Guardar como"

# --- Escribir la ruta completa del archivo en el cuadro Guardar como ---
pdf_file = r"C:\Users\gabri\OneDrive\Escritorio\proyectos\auditory_market\dashboards\guardados\dashboard.pdf"

print(f"💾 Guardando en: {pdf_file}")
time.sleep(0.3)

# Escribir ruta completa
pyautogui.typewrite(pdf_file)
time.sleep(0.3)

# Enter para confirmar guardado
pyautogui.press("enter")
time.sleep(0.3)

# --- Confirmar reemplazo si aparece popup ---
time.sleep(0.2)  # darle un respiro a Chrome para mostrar el aviso
print("⚠️ Si aparece confirmación de reemplazo: mover a 'Sí' y presionar Enter...")
pyautogui.press("left")   # mover selección a "Sí"
time.sleep(0.2)
pyautogui.press("enter")  # confirmar

# --- Cerrar Power BI con la X ---
print("🛑 Cerrando Power BI...")
try:
    main.close()  # intenta cerrar con el botón X
    time.sleep(2)
    print("✅ Power BI cerrado con la X.")
except Exception as e:
    print("⚠️ No se pudo cerrar con la X, forzando kill:", e)
    app.kill()
time.sleep(2)
#===========================================================================
# Enviar el PDF por correo


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