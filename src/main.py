import smtplib
from pathlib import Path
from env.secrets import Profile

'''
Send email with attachments - https://stackoverflow.com/questions/3362600/how-to-send-email-attachments
'''

def init():
    my_profile = Profile()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(my_profile.USERNAME, my_profile.PASSWORD)
    return my_profile, server


def send_email(sent_from, to, subject, body, server):
    email = "\r\n".join([
        "From: {}".format(sent_from),
        "To: {}".format(to),
        "Subject: {}".format(subject),
        "",
        "{}".format(body)
    ])
    
    server.sendmail(sent_from, to, email)

    print("Email sent! - TO: {}".format(to))


def main():
    try:
        my_profile, server = init()
        sent_from = my_profile.USERNAME

        to = "tplantin@utexas.edu"
        subject = "Testing 3"
        first_name = "Thomas"
        body = Path("./src/body.txt").read_text().format(first_name)

        send_email(sent_from, to, subject, body, server)

        server.close()
    
    except ValueError:
        print('Something went wrong...')


if __name__ == "__main__":
    main()
