import smtplib
smtp=smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('c2735940449@gmail.com','ygch szmk oeyt lzwe')
from_addr='c2735940449@gmail.com'
to_addr="s110213060@mail1.ncnu.edu.tw"
msg="Subject:Gmail sent by Python scripts\n no anger!"
status=smtp.sendmail(from_addr, to_addr, msg)#加密文件，避免私密信息被截取
if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
    smtp.quit()