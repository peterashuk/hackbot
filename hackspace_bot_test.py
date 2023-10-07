import socket
import network
import machine
#from secrets import secrets
from machine import Pin,PWM,UART 
import time 


led = machine.Pin("LED",Pin.OUT)


In1=Pin(6,Pin.OUT)  #IN1
In2=Pin(7,Pin.OUT)  #IN2


#OUT3  and OUT4
In3=Pin(4,Pin.OUT)  #IN3
In4=Pin(3,Pin.OUT)  #IN4


EN_A=PWM(Pin(8))
EN_B=PWM(Pin(2))
# Defining frequency for enable pins
EN_A.freq(1500)
EN_B.freq(1500)

# Setting maximum duty cycle for maximum speed (0 to 65025)
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)

# Left
def turn_left():
    print("Left I go")
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    
# Right
def turn_right():
    print("Right I go")
    In1.low()
    In2.high()
    In3.high()
    In4.low()
    
# Backward
def move_backward():
    print("Back up Back up")
    In1.low()
    In2.high()
    In3.low()
    In4.high()
    
# Forward
def move_forward():
    print("Onwards!")
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    
# Stop
def stop():
    print("All Stop")
    In1.low()
    In2.low()
    In3.low()
    In4.low()






while True:
    
    led.toggle()


    move_forward()

    time.sleep(2)
    turn_left()
    time.sleep(2)
    turn_right()
    time.sleep(2)
    time.sleep(2)
    move_backward()
    time.sleep(2)
    stop()
            
    time.sleep(2)
