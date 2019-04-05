#Fungsi kod: Membaca bacaan Ultrasonik dan berbunyi jika ada halangan.
#Penulis: Khairul Fikri
#Kemaskini: 4 April 2019

import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#Tetapan pin GPIO 
GPIO_TRIGGER = 22
GPIO_ECHO = 25
Buzzer = 26
 
#Tetapan input output GPIO 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)

GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            
            if dist > 10:
				GPIO.output(GPIO_TRIGGER, False)
				
            elif dist < 10:
					GPIO.output(Buzzer, True)
					time.sleep(0.2)
					GPIO.output(GPIO_TRIGGER, False)
					time.sleep(0.2)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
