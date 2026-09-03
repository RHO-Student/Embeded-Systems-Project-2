import serial
import struct
import time

PACKET_FORMAT = "<HHHHff" #i need 4 16bit ints (raw sensor, control, offset, diff) and two floats (calculated diff and temp)
PACKET_SIZE = struct.calcsize(PACKET_FORMAT) #16bytes

uno = serial.Serial('') # Update port to match your Pi (/dev/ttyACM0 or /dev/ttyUSB0), 9600, timeout=1)
time.sleep(4) #timeout to allow connection

def request_data():
    uno.reset_input_buffer()
    uno .write(b'R')
    
    raw_bytes = uno.read(PACKET_SIZE)
    if len(raw_bytes) == PACKET_SIZE: #change to match raw data
        sensor1, sensor2, temp, status = struct.unpack(PACKET_FORMAT, raw_bytes)
        return {
            "sensor1": sensor1,
            "sensor2": sensor2,
            "temperature": round(temp, 2),
            "status": status
        }
    else:
        raise TimeoutError("Bad data received")

def main():
    req = True
    while req:
        try:
            data = request_data()
            print(f"Received via Serial: {data}")
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)
        print("Do you want to request more data")
        req = input ## wrong fix latter