import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, from_email, to_emails, username, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_emails, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    

    emails = input("Enter email id's whom you want to send emails separated by space:\n")
    from_email = "kapil902677@gmail.com"
    to_emails = emails.split() 
    username = "kapil902677@gmail.com"
    
    
    subject = input("Write subject of mails.\n")
    message = input("Write your mail content here..........\n")
    password = input("Enter your Password\n") #use due to security
    
    send_email(subject, message, from_email, to_emails, username, password)
