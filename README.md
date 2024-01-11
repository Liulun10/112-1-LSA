# 112-1 LSA期末專題 ALARAGE逼人起床氣

## 動機發想 (Concept Development)
最近天氣越來越冷，每天都好難起床，但已經翹太多課的小源，必須得起床去上課，為了幫助他，我們用樹莓派做了一個互動式鬧鐘，讓他一定能起床上課!!!
## 說明
使用者先設定起床時間及幾秒內要起床，時間到後喇叭會先撥出音樂，過了起床時間的一半則開始轉動馬達攻擊，超過起床時間後則傳送秘密，若要暫停鬧鐘，心跳須達到95次/分鐘  
例如：設定9:00的鬧鐘，10分鐘內要起床，那麼9:00就會先開始撥放音樂，9:05馬達開始轉動，9:10發送郵件
## 軟體架構 (Existing Library/Software)
Python3  

## 硬體
| 設備名稱     | 圖片           | 來源  |
| ---- |:---:| ---:|
| Raspberry Pi 4        |  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/raspberrypi.jpg)    | $0 |
| RF-15 強扭力直流馬達        | ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E9%A6%AC%E9%81%94.jpg)      |   $120 自行購買 台中今華電子 |
| 8顆1.5V電池+電池盒子      |  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E9%9B%BB%E6%B1%A0.jpg)     |    $10幾塊? 自行購買 台中今華電子 |
| L298N 步進馬達驅動模組      | ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/L298N.jpg)      |    $80 自行購買 台中今華電子 |  
| MCP3008類比訊號轉換器      | ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/mcp3008.jpg)|  $250 自行購買 台中今華電子 |
| 心律傳感器     | ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E5%BF%83%E8%B7%B3%E6%84%9F%E6%B8%AC%E5%99%A8.jpg)  |  $120 自行購買(買的沒有焊接好，後來在moli找到焊接好的) 台中今華電子 |
| 喇叭(有3.5mm輸出的)      | ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E5%96%87%E5%8F%AD.jpg)    |    $0(柏瑋學長提供 |
| 杜邦線(數條)&麵包板 | | $0 moli提供 | 


## 前置下載 (Installation)
#### 使用到的軟體與套件  
* python3  
* smtplib  
* pygame
* time
* RPi.GPIO   
* threading
* spidev  
* datetime  
* subprocess   
* sys

## 執行過程 (Implementation Process)
### 組裝硬體設備
  * #### MCP3008參考此圖接線  
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/MCP3008%E6%8E%A5%E7%B7%9A%E5%9C%96.jpg)  
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/mcp3008.png)
  * #### L298N參考此圖接線  
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/L298N%E6%8E%A5%E7%B7%9A%E5%9C%96.jpg)
  * #### 我們整個設備的接線狀態  
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E6%8E%A5%E7%B7%9A%E7%B4%B0%E7%AF%80%E5%9C%96/%E6%95%B4%E9%AB%94%E6%8E%A5%E7%B7%9A.jpg)
  * #### 各部分細節
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E6%8E%A5%E7%B7%9A%E7%B4%B0%E7%AF%80%E5%9C%96/L298N%E7%B4%B0%E7%AF%80.jpg)
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E6%8E%A5%E7%B7%9A%E7%B4%B0%E7%AF%80%E5%9C%96/%E6%A8%B9%E8%8E%93%E6%B4%BE%E7%B4%B0%E7%AF%80.jpg)
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E6%8E%A5%E7%B7%9A%E7%B4%B0%E7%AF%80%E5%9C%96/%E9%BA%B5%E5%8C%85%E7%89%88%E7%B4%B0%E7%AF%801.jpg)
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/%E6%8E%A5%E7%B7%9A%E7%B4%B0%E7%AF%80%E5%9C%96/%E9%BA%B5%E5%8C%85%E7%89%88%E7%B4%B0%E7%AF%802.jpg)
  * 按照以上圖接線就能成功
## code
### 鬧鐘
* 設定時間
```
def clock():
     # 讓使用者輸入日期和時間
    user_input_year = 2024 #int(input("請輸入年份: "))
    user_input_month = 1 #int(input("請輸入月份: "))
    user_input_day = 11 #int(input("請輸入日期: "))
    user_input_hour = int(input("請輸入小時（24小時制）: "))
    user_input_minute = int(input("請輸入分鐘: "))
    user_input = int(input("請輸入秒數: "))

    global user_alarm_time
    # 使用者鬧鐘時間
    user_alarm_time = datetime(user_input_year, user_input_month, user_input_day, user_input_hour, user_input_minute,user_input)

    # 計算等待時間
    time_until_alarm = user_alarm_time - datetime.now()

    print(f"鬧鐘已設定在 {user_alarm_time.strftime('%Y-%m-%d %H:%M:%S')} 觸發")
    target_time = user_alarm_time + timedelta(minutes=2)


    # 等待使用者設定的時間
    time.sleep(time_until_alarm.total_seconds())
```
* 撥放音樂
```
def play_mp3(file_path, volume=1.0, duration=alltime):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.set_volume(volume)

        start_time = time.time()
        while time.time() - start_time < duration and not stop_event.is_set():
            pygame.mixer.music.play()

            # 等待直到音樂播放完畢
            while pygame.mixer.music.get_busy() and not stop_event.is_set():
                time.sleep(1)
    except Exception as e:
        print("")
        pygame.mixer.quit()
        pygame.quit()
    finally:
        return
```
### 馬達轉動
```
def run_motor():
    in1 = 13
    in2 = 19
    en = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    p = GPIO.PWM(en, 100)
    p.start(25)
    time.sleep(halftime)
    
    # 運動時間
    motor_run_time = halftime  # 假設運動時間為10秒
    
    start_time = time.time()
    
    while (time.time() - start_time) < motor_run_time and not stop_event.is_set():
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        p.ChangeDutyCycle(100)
        time.sleep(1)
    
    # 停止馬達
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    
    # 停止PWM
    p.stop()
    
    # 釋放GPIO資源
    GPIO.cleanup()
```
#### 偵測心跳
* 時間到即發送郵件
```
def heart():
    p = Pulsesensor()
    p.startAsyncBPM()

    bpm_data = []

    target_time = user_alarm_time + timedelta(minutes=1)
    current_time = datetime.now()
    global a
    try:
        while True:
            while not stop_event.is_set():
                bpm = p.BPM
                if 0 < bpm < 150:
                    print("BPM: %d" % bpm)
                    bpm_data.append(bpm)
                else:
                    bpm_data.append(0)
                time.sleep(1)

                # 取最右邊的五個元素
                last_five_elements = bpm_data[-5:]
                average_value = sum(last_five_elements) / len(last_five_elements)

                if len(bpm_data) > alltime:
                    print("發送帥照喔！")
                    play_mp3('photo.mp3',1.0,1)
                    subprocess.run(["python3", "EMAAAAA.py"])
                    a = 0
                    return

                if average_value > 50:
                    print("謝謝，祝你有愉快的一天")
                    play_mp3('happyday.mp3',1.0,1)
                    a = average_value
                    return
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        p.stopAsyncBPM()
```
#### 發送電子郵件
```
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
```
## 開始玩囉！ (Usage)
* 購買以上設備，並組裝完成  
* Clone the project on GitHub：`https://github.com/Liulun10/112-1-LSA-ALARAGE.git`
* 偵測心跳需要搭配MCP3008把類比訊號轉為數位訊號，參考[搜尋到的資料](https://github.com/tutRPi/Raspberry-Pi-Heartbeat-Pulse-Sensor/tree/master)  
使用到這位的`MCP3008.py`及`pulsesensor.py`檔案，請搭配使用(因為是他人撰寫的程式就不在我們的github上傳)
* 可以到Email.py更改收送電子郵件的人及內容
* 從ALARAGE.py開始執行
## 心得反饋&遇到的困難
* 樹梅派很皮，明明一樣的設定，但有時候就是跑不出東西，所以遇到問題，給它一點時間，多做幾次(放一包綠色乖乖在旁邊
* 緊急發現樹莓派無法輸入類比訊號，趕快到台中採買  
* 剛開始要安裝套件時一直跑出錯誤訊息`error: externally-managed-environment`無法解決，後來看到這個[救命網頁](https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3)  
輸入裡面的`sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED` 才解決問題
* 裝馬達過程中發現，需要啟用SPI，(搜尋`樹莓派啟用SPI`)
* 鬧鐘響需要mp3等檔案，使用`scp FileName user@ip:/home/path/`，把檔案從本機複製到樹莓派
* 偵測心跳需要搭配MCP3008把類比訊號轉為數位訊號，參考[搜尋到的資料](https://github.com/tutRPi/Raspberry-Pi-Heartbeat-Pulse-Sensor/tree/master)
  使用到這位的`MCP3008.py`及`pulsesensor.py`檔案，請搭配使用
## 工作分配 (Job Assignment)
劉宜倫：github整理，製作PPT，出錢採買零件，討論，報告  
陳梓銜：題目發想，程式撰寫，排錯，硬體組裝，採買零件，討論，報告  
蔡宇哲：提供意見，硬體組裝，出錢採買零件，討論，報告  
藍奕勛：程式撰寫，硬體組裝，採買零件，討論，報告  
李浩源：查資料，出席報告
## 善用所學 (Knowledge from Lecture)
ssh，基礎指令，python程式
## 參考資料 (References)
https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3  
https://tutorials-raspberrypi.com/wp-content/uploads/Raspberry-Pi-MCP3008-ADC-Anschluss-Steckplatine.png  
https://104.es/index.php/2021/08/27/raspi-adc-mcp3008/  
https://randomnerdtutorials.com/raspberry-pi-analog-inputs-python-mcp3008/  
https://github.com/WorldFamousElectronics/Raspberry_Pi/blob/master/PulseSensor_Processing_Pi/PulseSensor_Processing_Pi.md  
https://s761111.gitbook.io/raspi-sensor/yi-de-xin-tiao-mo-ling-jian  
https://s761111.gitbook.io/raspi-sensor/pai-bi-wei-li  
https://github.com/jumejume1/pi-l298n-dc-motor  
https://www.gushiciku.cn/pl/pDLC/zh-tw  
https://www.youtube.com/watch?v=BpE6zDN21qs&t=164s  
https://pulsesensor.com/pages/pulsesensor-raspberrypi  
https://note.drx.tw/2008/03/ubuntuscp-part1.html  
