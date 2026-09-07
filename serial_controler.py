# https://www.w3schools.com/python/python_file_open.asp

import serial
import time

uno = serial.Serial('COM3',9600,timeout=1) # Update port to match your Pi (/dev/ttyACM0 or /dev/ttyUSB0), 9600, timeout=1)


def main():
    with open("Readings.csv","+a",encoding="utf-8") as csv:  
        amount = int(input("How many readings do you want to do?"))
        for i in range(amount) :
            time.sleep(2)
            uno.write(b'1')
            if uno.in_waiting > 0:
                text = str(uno.readline().decode('utf-8').rstrip())
                csv.write(text)
                data = text.split(',')
                print(f"Received {data}")


main()