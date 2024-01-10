from re import A
import threading
import pygame
import time
from datetime import datetime, timedelta
import subprocess
import RPi.GPIO as GPIO
from pulsesensor import Pulsesensor
import sys
import schedule

global alltime 
alltime = int(input("想要在幾秒內起床"))
global halftime
halftime = alltime/2
# 用於通知線程停止的 Event
stop_event = threading.Event()
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
def clock():
    user_input_year = 2024
    user_input_month = 1
    user_input_day = 11
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

def main():
    global stop_event


    clock()
    # 使用 threading.Thread 同時執行 heart()、音樂播放和馬達控制
    heart_thread = threading.Thread(target=heart)
    music_thread = threading.Thread(target=play_mp3, args=('ringing.mp3', 1.0, alltime))  # 播放兩分鐘
    motor_thread = threading.Thread(target=run_motor)

    # 啟動所有線程
    heart_thread.start()
    music_thread.start()
    motor_thread.start()

    # 等待 heart() 完成，並檢查返回值
    heart_thread.join()
    
    if a > 50:
        stop_event.set()  # 設定 Event 通知其他線程停止
        music_thread.join()
        motor_thread.join()
        sys.exit()
    else         :
        stop_event.set()  # 設定 Event 通知其他線程停止
        music_thread.join()
        motor_thread.join()
        sys.exit()



if __name__ == "__main__":
    main()


