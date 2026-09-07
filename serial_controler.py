# https://www.w3schools.com/python/python_file_open.asp

import serial
import time

def main():
    print ("NOTE there is a minute between each reading entered")
    amount = int(input("How many readings do you want? "))
    for i in range (amount):
        uno = serial.Serial('COM3',9600,timeout=1) # Update port to match your Pi (/dev/ttyACM0 or /dev/ttyUSB0), 9600, timeout=1) COM3 for win usuly
        time.sleep(2)
        with open(r"D:\Embeded-Systems-Project-2\Readings.csv","a",encoding="utf-8") as csv:  # dispite working relitivly at home abslute is needed for runing at course
            uno.write(b'1')
            for i in range(5) :
                    text = uno.readline().decode('utf-8').rstrip()
                    if (text != ""):
                        systime = time.localtime()
                        formtime = time.strftime("%d-%m-%Y %H:%M",systime)
                        csv.write("\n" + text + "," + formtime)
                    data = text.split(',')
                    print(f"Received {data}")
#excess data is not saved to the csv so having it loop 5 times is good for catching slow serial stuff 
    time.sleep(60)

main()