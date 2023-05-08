import smtplib
import imghdr

from email.message import EmailMessage

email_sender ="saaiid748@gmail.com"
receiver = "mis1411@gmail.com"
password = "uzivfkythgiuiizd"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer Showed up!"
    email_message.set_content("new customer")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email_sender, password)
    gmail.sendmail(email_sender, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email("images/12.png")
