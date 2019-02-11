import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(12, GPIO.OUT) 

try:  
    print "Waiting for falling edge on port 23"  
    GPIO.wait_for_edge(23, GPIO.RISING)  
    time.sleep(5)
    if GPIO.input(23):
        GPIO.output(12, GPIO.HIGH)
        RVC_set = 1
    while RVC_set == 1:
        time.sleep(5)
        if (GPIO.input(23) == FALSE):
            GPIO.output(12, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(12, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(12, GPIO.HIGH)
            RVC_set=0

# https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
  
