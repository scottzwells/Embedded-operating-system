import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18.GPIO.OUT)
GPIO.setup(27.GPIO.OUT)
t=0.5

def loop():
    while True:
        GPIO.output(17,GPIO.HIGH)
        time.sleep(t)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(t)
        GPIO.output(17,GPIO.LOW)
        time.sleep(t)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(t)
        GPIO.output(27.GPIO.LOW)
        time.sleep(t)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(t)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        time.sleep(t)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()