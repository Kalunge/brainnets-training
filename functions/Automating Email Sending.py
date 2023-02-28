# You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

# Here are the steps you can take to automate this process:

#     Use the smtplib library to connect to the email server and send the emails.

#     Use the email library to create the email message.


#     Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

#     Use the os library to access the report files that need to be sent.

#     Use a for loop to iterate through the list of recipients and send the email and attachment.

#     Use the schedule library to schedule the script to run daily at a specific time.

#     You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process.


def send_email(recipient, subject, body):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    sender_email = "titoh@mail.com"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    filename = "report.pdf"
    attachment = open("report.pdf", "rb")

    p = MIMEBase("application", "octet-stream")

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header("Content-Disposition", "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP("smtp.gmail.com", 587)

    s.starttls()

    s.login(sender_email, "password")

    text = msg.as_string()

    s.sendmail(sender_email, recipient, text)

    s.quit()

    print("Email sent to " + recipient)


def main():
    import os
    import schedule
    import time

    recipients = []
    subject = "Daily Report"
    body = "Hi, Please find attached the daily report for your review.Thanks!"

    for recipient in recipients:
        send_email(recipient, subject, body)

    schedule.every().day.at("10:30").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
