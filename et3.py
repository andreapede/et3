import serial
import matplotlib.pyplot as plt
import numpy

def s16(value):
    """twos complement conversion into a signed integer"""
    return -(value & 0x8000) | (value & 0x7fff)
def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
    plt.draw()

comPort='COM3'
data=[]
ser=serial.Serial(comPort,baudrate=9600,bytesize=8,parity='N',stopbits=1)   #open serial port
print(ser.name)
hl, = plt.plot([], [])
while True:
    ser.write(hex(6).encode())
    line=ser.read(3)
    print(line)

    ser.write(hex(5).encode())
    line2=ser.read(20)
    print(line2.hex())

    for i in range(3,18,2):
        hex_string=line2[i:i+2]
        data=s16(int(hex_string.hex(), 16))/1000
        print(hex_string, s16(int(hex_string.hex(), 16))/1000)






ser.close()