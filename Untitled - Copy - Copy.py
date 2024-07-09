import os
import time
import serial
import threading
import sys
from PyQt5.QtWidgets import QApplication, QWidget

Reset_Angle=False
Angle = 0

def get_user_input():
    global Angle
    while True:
        user_input = input()
        if user_input.lower() == 'f':
            Angle=0


def Read_FOG():
    global Angle
    ser = serial.Serial(
    port='COM20',\
    baudrate=460800,\
    parity=serial.PARITY_EVEN,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS)

    print("connected to: " + ser.portstr)

    try:
        while True:
            header = ser.read(1)
            if header and header[0]==0x94 :
                FOG_Bytes = ser.read(20)
                FOG_Bytes_HEX=FOG_Bytes.hex()
                LSB_1=int(FOG_Bytes_HEX[2:4],16)
                LSB_2=int(FOG_Bytes_HEX[4:6],16)
                LSB_3=int(FOG_Bytes_HEX[6:8],16)
                LSB_4=int(FOG_Bytes_HEX[8:10],16)
                
                Raw_Gyro_Data=LSB_4 | LSB_3<<7 | LSB_2<<14 | LSB_1<<21

                Raw_Gyro_Data=Raw_Gyro_Data<<4
                if(LSB_1 & 0x40):
                    Raw_Gyro_Data=Raw_Gyro_Data-4294967296
                Raw_Gyro_Data=Raw_Gyro_Data>>4

                Angle = Angle + Raw_Gyro_Data - 2615
                print(Raw_Gyro_Data,"\t",Angle/9.4342633545e7) 
    finally:
        ser.close()  

thread1 = threading.Thread(target=Read_FOG)
thread2 = threading.Thread(target=get_user_input)

thread1.start()
thread2.start()