from machine import Pin, PWM
from rtttl import RTTTL
import time
from neopixel import NeoPixel

led_strip = NeoPixel(Pin(4), 15)

buzzer = PWM(Pin(5))

#tune = RTTTL("James Bond:d=4,o=5,b=140:8e,16f#,16f#,8f#,f#,8e,8e,8e,8e,16g,16g,8g,g,8f#,8f#,8f#,8e,16f#,16f#,8f#,f#,8e,8e,8e,8e,16g,16g,8g,g,8f#,8f,8e,8d#6,2d.6,8b,8a,1b,")
#tune = RTTTL("Phantom:d=4,o=5,b=225:d#.,g#.,d#.,f#.,8e.,2e.,c#.,f#.,8c#.,1d#.,d#.,g#.,d#.,f#.,8e.,2e.,c#.,f#.,8c#.,1d#.,d#.,g#.,b.,d#.6,8c#.6,2c#.6,c#.6,f#.6,8c#.6,1d#.6,d#.6,1g#.6,8f#.6,8e.6,8d#.6,8c#.6,8b.,8a#.,8g#.,1g.,e.,e.,8d#.,1d#.")
tune = RTTTL("Two Tigers:d=4,o=5,b=140:4c,4d,4e,4c,4c,4d,4e,4c,4e,4f,2g,4e,4f,2g,8g,8a,8g,8f,4e,4c,8g,8a,8g,8f,4e,4c,4c,4g,2c,4c,4g,2c")

i = 0

# 將音符資訊放入變數
tune_list = []
for freq, msec in tune.notes():
    tune_list.append((freq, msec))
    
# 計算音符數量
tune_lenth = len(tune_list)

# 建立播放索引變數和鬧鐘狀態變數
tune_index = 0

buzzer.duty(0)

def play_tone(freq, msec):
    if freq > 0:        
        buzzer.freq(freq)
        buzzer.duty(512)
        time.sleep(msec*0.001)  
        buzzer.duty(0)
    time.sleep(0.05)

while True:       
    freq = tune_list[tune_index][0]
    msec = tune_list[tune_index][1]
    play_tone(freq, msec)
    # 準備播放下一個音符
    tune_index += 1
    if tune_index >= tune_lenth:
        tune_index = 0
    # Play LED
    led_strip[i%15] = (0, 00, 200)
    led_strip.write()              # 依設定顯示
    time.sleep_ms(10)              # 暫停 10 毫秒
    led_strip[i%15] = (0, 0, 0)    # 再將當顆燈珠熄滅
    i = i + 1

buzzer.duty(0)
