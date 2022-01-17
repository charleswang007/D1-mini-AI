from machine import Pin, PWM
from rtttl import RTTTL
import time
from neopixel import NeoPixel

led_strip = NeoPixel(Pin(4), 15)

buzzer = PWM(Pin(5))
buzzer.duty(0)

def play_tone(freq, msec):
    if freq > 0:        
        buzzer.freq(freq)
        buzzer.duty(512)
        time.sleep(msec*0.001)  
        buzzer.duty(0)
    time.sleep(0.05)

#tune = RTTTL("Castle on a Cloud: d=4,o=5,b=90:8a,16b,16c6,8b,8a,8a,8g#,a,p,8a,16b,16c6,8b,8a,8g,8f,e,p,8d,16e,16f,8e,8a,8b,8c6,a,p,8d,16e,16f,8e,8d,8c,8b,a")
tune = RTTTL("James Bond Theme : d=4,o=5,b=140:8e,16f#,16f#,8f#,f#,8e,8e,8e,8e,16g,16g,8g,g,8f#,8f#,8f#,8e,16f#,16f#,8f#,f#,8e,8e,8e,8e,16g,16g,8g,g,8f#,8f,8e,8d#6,2d.6,8b,8a,1b,")
#tune = RTTTL("Phantom:d=4,o=5,b=225:d#.,g#.,d#.,f#.,8e.,2e.,c#.,f#.,8c#.,1d#.,d#.,g#.,d#.,f#.,8e.,2e.,c#.,f#.,8c#.,1d#.,d#.,g#.,b.,d#.6,8c#.6,2c#.6,c#.6,f#.6,8c#.6,1d#.6,d#.6,1g#.6,8f#.6,8e.6,8d#.6,8c#.6,8b.,8a#.,8g#.,1g.,e.,e.,8d#.,1d#.")
i = 0

for freq, msec in tune.notes():
    play_tone(freq, msec)
    led_strip[i%15] = (0, 0, 200)
    led_strip.write()              # 依設定顯示
    time.sleep_ms(10)              # 暫停 200 毫秒
    led_strip[i%15] = (0, 0, 0)    # 再將當顆燈珠熄滅
    i = i + 1
    
buzzer.duty(0)