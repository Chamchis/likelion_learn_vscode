import smtplib
from email.message import EmailMessage
import imghdr
import re


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print('메일이 발송되었습니다.')
    else:
        print('유효한 이메일 주소가 아닙니다.')

message = EmailMessage()

message.set_content('안녕하세요 반갑습니다')
message['Subject'] = '테스트입니다 응답바람 아님말고 .'
message['From'] = 'junhoo8888@gmail.com'
message['To'] = 'ckacl159753@naver.com'

with open('Real_Madrid_CF.png','rb') as image:
    image_file = image.read()

image_type = imghdr.what('Real_Madrid_CF.png',image_file)
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login('junhoo88888@gmail.com',"mqqx qupa etjf fhls")

sendEmail('junhoo88888@gmail.com')
smtp.quit()