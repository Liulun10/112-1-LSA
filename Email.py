import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('mailfrom', 'password')
#mailfrom請替換為寄信人信箱
from_addr = 'mailfrom'
#mailto請替換為收件人信箱
to_addr = ["mailto","mailto2"]
#主旨
subject = '外流請查收(Demo無毒請安心食用)'
#內文
body = '請查收'

# 創建 MIMEMultipart 物件
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = ', '.join(to_addr)
msg['Subject'] = subject

# 在郵件內容中添加文字部分
msg.attach(MIMEText(body, 'plain'))

# 在郵件內容中添加附件（圖片）
image_path = r'/home/pi/bigBT.png'#放檔案的路徑
with open(image_path, 'rb') as image_file:
    image_attachment = MIMEApplication(image_file.read(), Name='bt.png')
    image_attachment['Content-Disposition'] = f'attachment; filename="{image_path}"'
    msg.attach(image_attachment)

# 發送郵件
smtp.send_message(msg)

print("郵件傳送成功!")
smtp.quit()
