import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


class Email:
    def __init__(self, sender_name, sender_email, sender_password, receivers_email, subject, body, attachments=None):
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receivers_email = receivers_email
        self.subject = subject
        self.body = body
        self.attachments = attachments if attachments else []

    def send_email(self):
        try:
            # Create the email object
            message = MIMEMultipart()
            message['From'] = f"{self.sender_name} <{self.sender_email}>"
            message['To'] = ', '.join(self.receivers_email)
            message['Subject'] = self.subject

            # Attach the body of the email
            message.attach(MIMEText(self.body, 'plain'))

            # Attach files if there are any
            if self.attachments:
                for attachment in self.attachments:
                    if os.path.isfile(attachment):
                        part = MIMEBase('application', 'octet-stream')
                        with open(attachment, 'rb') as file:
                            part.set_payload(file.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment)}')
                        message.attach(part)
                    else:
                        print(f"Warning: Attachment {attachment} was not found.")

            # Send the email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, self.receivers_email, message.as_string())

            print("Email sent successfully.")

        except Exception as e:
            print(f"Failed to send email. Error: {e}")


# Example usage
if __name__ == "__main__":
    email = Email(
        sender_name="Your Name",
        sender_email="your_email@gmail.com",
        sender_password="your_password",
        receivers_email=["receiver1@example.com", "receiver2@example.com"],
        subject="Test Email",
        body="This is a test email sent from Python.",
        attachments=["path/to/attachment1.txt", "path/to/attachment2.pdf"]
    )

    email.send_email()
