import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Gmail SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "vlmgopal2004@gmail.com"
SENDER_PASSWORD = "pmov boit agrr hkba"  # ⚠️ use env variable for safety

def send_email(to_email, subject, body, attachments=None):
    """Send a single email (handles its own SMTP connection)"""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            msg = MIMEMultipart()
            msg["From"] = SENDER_EMAIL
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            if attachments:
                for file_path in attachments:
                    if os.path.exists(file_path):
                        with open(file_path, "rb") as f:
                            mime_base = MIMEBase("application", "octet-stream")
                            mime_base.set_payload(f.read())
                            encoders.encode_base64(mime_base)
                            mime_base.add_header(
                                "Content-Disposition",
                                f"attachment; filename={os.path.basename(file_path)}"
                            )
                            msg.attach(mime_base)

            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
            print(f"✅ Email sent to {to_email}")

    except Exception as e:
        print(f"❌ Error sending email to {to_email}: {e}")


def send_bulk_emails(csv_file, subject, body, attachments=None):
    """Send emails to all recipients in a CSV file (with same attachment to all)"""
    try:
        csv_path = os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f"Error: CSV file '{csv_file}' not found.")
            return

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            with open(csv_path, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)  # skip header row

                for row in reader:
                    if row:
                        email = row[0].strip()
                        send_email(server, email, subject, body, attachments)  # ✅ pass attachments

    except Exception as e:
        print(f"❌ Error reading CSV file: {e}")
