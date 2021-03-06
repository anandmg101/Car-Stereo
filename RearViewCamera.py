import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(3, GPIO.OUT) 

try:  
    print ("Waiting for falling edge on port 23")
    GPIO.wait_for_edge(2, GPIO.RISING)
    print ("Event detected")
    time.sleep(5)
    if GPIO.input(2):
        GPIO.output(3, GPIO.HIGH)
        RVC_set = 1
    while RVC_set == 1:
        time.sleep(5)
        if (GPIO.input(2) == FALSE):
            GPIO.output(3, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(3, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(3, GPIO.HIGH)
            RVC_set=0
except KeyboardInterrupt:  
    GPIO.cleanup()   
GPIO.cleanup()
