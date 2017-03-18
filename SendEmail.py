import smtplib
import argparse 

def sendEmail(user_id, user_pwd, recipient, message):
    to = recipient
    # GMAIL
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo	
    smtpserver.login(user_id, user_pwd)
    header = 'To:' + to + '\n' + 'From: ' + user_id + '\n' + 'Subject: Profiles we recommend for Ya! \n'
    msg = header + '\n %s \n\n' % message
    smtpserver.sendmail(user_id, to, msg)
    smtpserver.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send email service')
    parser.add_argument('-u', '--user_id', help = "Email ID", type = str)
    parser.add_argument('-p', '--user_pwd', help = "Password for Email account", type = str)
    parser.add_argument('-r', '--recipient', help = "Recipient ID", type = str)
    parser.add_argument('-c', '--content', help = "Email content", type = str)
    args = parser.parse_args()

    user_id = args.user_id
    user_pwd = args.user_pwd
    email_recipient = args.recipient
    email_content = args.content
    try:
        sendEmail(user_id, user_pwd, email_recipient, email_content)
        print "Email Sent"
    except Exception as e:
        print "Email Not Sent. Possble reason: " + str(e)
