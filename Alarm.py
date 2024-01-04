import pygame
import time

def play_alarm(alarm_file):
    # 初始化pygame
    pygame.init()

    # 設置音訊設備
    pygame.mixer.init()

    # load音訊文件
    pygame.mixer.music.load(alarm_file)

    # 播放音訊
    pygame.mixer.music.play()

    # 等待音樂播放完畢
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def set_alarm(alarm_time, alarm_file):
    current_time = time.strftime("%H:%M:%S")
    while current_time != alarm_time:
        print("Current Time:", current_time)
        time.sleep(1)
        current_time = time.strftime("%H:%M:%S")
    print("Time's up! Playing alarm...")
    play_alarm(alarm_file)
if __name__ == "__main__":
    # 設置鬧鐘時間和播放的檔案
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    alarm_file = "/home/pi/up.mp3"  # 完整路徑

    # 啟動鬧鐘
set_alarm(alarm_time, alarm_file)