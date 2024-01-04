# 112-1 LSA期末專題 ALARAGE逼人起床氣

## 動機發想 (Concept Development)
最近天氣越來越冷，每天都好難起床，但已經翹太多課的小源，必須得起床去上課，為了幫助他，我們用樹莓派做了一個互動式鬧鐘，讓他一定能起床上課!!!
說明
使用者先設定起床時間，以及不可告人的秘密和要發送的電子郵件，時間到後喇叭會先撥出音樂，五分鐘則開始轉動馬達
## 軟體架構 (Existing Library/Software)
Python3
Pygame
Time
smtplib
## 硬體
| 設備名稱     | 圖片           | 來源  |
| ---- |:---:| ---:|
| Raspberry Pi 4        | 靠右對齊      | $0 |
| RF-15 強扭力直流馬達        | 置中對齊      |   $120 自行購買 台中今華電子 |
| 8顆?V電池+電池盒子      | 是整齊的      |    $10幾塊? 自行購買 台中今華電子 |
| L298N 步進馬達驅動模組      | 是整齊的      |    $250 自行購買 台中今華電子 |  
| MCP3008類比訊號轉換器      | ![image](https://github.com/Liulun10/112-1-LSA/assets/148021967/d1dd9456-b3b6-4554-9d6f-684c9157edb7)|  $250 自行購買 台中今華電子 |
| 心律傳感器     | 是整齊的      |    $120 自行購買(買的沒有焊接好，後來在moli找到焊接好的) 台中今華電子 |
| 喇叭(有3.5mm輸出的      |       |    $0(柏瑋學長提供 |
| 杜邦線 | | $0 moli提供 | 


## 前置下載 (Installation)
Sodo apt install python3
Pip3
## 執行過程 (Implementation Process)

## 開始玩囉！ (Usage)
先設定起床時間
再設定不可告人秘密及要傳送對象的電子郵件

## 心得反饋&遇到的困難
樹梅派很皮，明明一樣的設定，但有時候就是跑不出東西，所以遇到問題，給它一點時間，多做幾次(放一包綠色乖乖在旁邊

## 工作分配 (Job Assignment)
劉宜倫：github整理，製作PPT，提供
陳梓銜：題目發想，程式
蔡宇哲：程式
藍奕勛：程式
## 善用所學 (Knowledge from Lecture)
## 參考資料 (References)
https://104.es/index.php/2021/08/27/raspi-adc-mcp3008/
https://randomnerdtutorials.com/raspberry-pi-analog-inputs-python-mcp3008/
https://github.com/WorldFamousElectronics/Raspberry_Pi/blob/master/PulseSensor_Processing_Pi/PulseSensor_Processing_Pi.md
