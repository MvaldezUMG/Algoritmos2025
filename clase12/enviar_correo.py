import smtplib
import os

def enviar_correo(destinatario, asunto, cuerpo):
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    contrasena = os.getenv("GOOGLE_APP_PASS")
    email = os.getenv("GOOGLE_APP_EMAIL")
    #Iniciar la conexion
    smtp.starttls()
    #iniciamos sesion
    smtp.login(email, contrasena)
    smtp.sendmail(email, destinatario, f"""Subject: {asunto} \n\n {cuerpo} """ )

enviar_correo("mvaldeza2@miumg.edu.gt", "Hola", "Hola desde algoritmos 2025")