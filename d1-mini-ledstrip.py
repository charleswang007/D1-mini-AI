# 從 machine 模組匯入 Pin 物件
from machine import Pin
# 匯入時間相關的 time 模組
import time, ledstrip

ledstrip.setup(4,15)

while True:                             # 一直不斷執行
    ledstrip.rainbow_cycle(5)
