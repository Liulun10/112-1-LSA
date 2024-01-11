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
| 杜邦線(數條) | | $0 moli提供 | 


## 前置下載 (Installation)
使用到的軟體與套件
python3
smtplib
pygame
time
GIPO  
threading  
datetime  
timedelta  
subprocess  
Pulsesensor  
sys

## 執行過程 (Implementation Process)
### 組裝硬體設備
  * #### MCP3008參考此圖接線  
  ![image](https://github.com/Liulun10/112-1-LSA-ALARAGE/blob/main/MCP3008%E6%8E%A5%E7%B7%9A%E5%9C%96.jpg)  
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
* 裝馬達過程中發現，需要啟用SPI接口，(搜尋`樹莓派啟用SPI`)
* 鬧鐘響需要mp3等檔案，使用`scp FileName user@ip:/home/path/`，把檔案從本機複製到樹莓派
* 偵測心跳需要搭配MCP3008把類比訊號轉為數位訊號，參考[搜尋到的資料](https://github.com/tutRPi/Raspberry-Pi-Heartbeat-Pulse-Sensor/tree/master)
  使用到這位的`MCP3008.py`及`pulsesensor.py`檔案，請搭配使用
## 工作分配 (Job Assignment)
劉宜倫：github整理，製作PPT，零件採買，討論  
陳梓銜：題目發想，程式撰寫，排錯，硬體組裝，零件採買，討論  
蔡宇哲：提供意見，硬體組裝，零件採買，討論  
藍奕勛：程式撰寫，硬體組裝，零件採買，討論  
李浩源：查資料
## 善用所學 (Knowledge from Lecture)
ssh，基礎指令，pythont程式
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
