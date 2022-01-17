from machine import Pin, PWM
import time

buzzer = PWM(Pin(5))
buzzer.duty(512)

buzzer.freq(330) # Mi
time.sleep(.5)
buzzer.freq(330) # Mi
time.sleep(.5)
buzzer.freq(349) # Fa
time.sleep(.5)
buzzer.freq(392) # Sol
time.sleep(.5)
buzzer.freq(392) # Sol
time.sleep(.5)
buzzer.freq(349) # Fa
time.sleep(.5)
buzzer.freq(330) # Mi
time.sleep(.5)
buzzer.freq(294) # Re
time.sleep(.5)
buzzer.freq(261) # Do
time.sleep(.5)
buzzer.freq(261) # Do
time.sleep(.5)
buzzer.freq(294) # Re
time.sleep(.5)
buzzer.freq(330) # Mi
time.sleep(1)
buzzer.freq(294) # Re
time.sleep(.5)
buzzer.freq(294) # Re
time.sleep(.5)

buzzer.duty(0) # 關閉蜂鳴器

