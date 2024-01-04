import spidev
from gpiozero import MCP3008
from time import sleep

# 初始化SPI介面
spi = spidev.SpiDev()
spi.open(0, 0)

# 定義MCP3008通道
channel = 0

# 定義心率感測器的最小和最大值
min_heart_rate = 70
max_heart_rate = 100

# 定義一個函數用於轉換ADC值為心率
def adc_to_heart_rate(adc_value):
    # 在這裡實現你的轉換邏輯
    # 這只是一個簡單的範例，實際上需要根據你的感測器和應用調整
    range_adc = 1023  # MCP3008的ADC範圍
    range_heart_rate = max_heart_rate - min_heart_rate
    normalized_value = adc_value / range_adc
    heart_rate = min_heart_rate + int(normalized_value * range_heart_rate)

    # 限制心率值在正常範圍內
    heart_rate = max(min_heart_rate, min(max_heart_rate, heart_rate))

    return heart_rate

try:
    while True:
        # 讀取MCP3008的數值
        adc_value = spi.xfer2([1, (8 + channel) << 4, 0])
        adc_value = ((adc_value[1] & 3) << 8) + adc_value[2]

        # 將ADC值轉換為心率
        heart_rate = adc_to_heart_rate(adc_value)

        # 顯示心率
        print(f"Heart Rate: {heart_rate} BPM")

        # 等待一段時間再進行下一次讀取
        sleep(1)

except KeyboardInterrupt:
    # 在按下Ctrl+C時停止程式執行
    spi.close()
    print("程式已停止執行")