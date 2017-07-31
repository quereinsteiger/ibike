#!/usr/bin/python3
#Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
#[GCC 4.9.1] on linux
#Type "copyright", "credits" or "license()" for more information.
#>>> #Libraries
import RPi.GPIO as GPIO
import time
import sqlite3


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 5
GPIO_ECHO = 4
GPIO_TASTER = 20

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
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

def send_values():
        
        value=[time.time(), distance()]
        time.sleep(0.001)
        cursor.execute("INSERT INTO tblDistanz VALUES("+str(value[0])+",1,"+str(value[1])+");")
        print("Datenbankeintrag: %f \t 1 \t %f" % tuple(value))
        return 










if __name__ == '__main__':
        con=sqlite3.connect("./data/ibike.sqlite")
        cursor=con.cursor()
        
        try:
               while True:               
                        send_values()
                        time.sleep(0.1)
                        
                       
                                      
                # Reset by pressing CRL + C
        except KeyboardInterrupt:
                con.commit()
                con.close()
                print("Programm stopped by User")
                GPIO.cleanup() 
            
                

