# https://www.w3schools.com/python/python_file_open.asp

import serial
import time

uno = serial.Serial('',9600,timeout=1) # Update port to match your Pi (/dev/ttyACM0 or /dev/ttyUSB0), 9600, timeout=1)
time.sleep(4) #timeout to allow connection

def main():
    req = True
    with open("","+a",encoding="utf-8") as csv:  
        while req:
            if uno.in_waiting > 0:
                text = uno.readline().decode('utf-8').rstrip
                csv.write(text + "\n")
                data = text.split(',')
                print(f"Receved {data}")