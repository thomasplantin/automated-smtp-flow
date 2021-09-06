import smtplib
from env.secrets import Profile

def main():
    try:
        my_profile = Profile()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print(my_profile.USERNAME, my_profile.PASSWORD)
        server.ehlo()
    
    except ValueError:
        print('Something went wrong...')


if __name__ == "__main__":
    main()
