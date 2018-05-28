import serial
comPort='COM3'
ser=serial.Serial(comPort,baudrate=9600,bytesize=8,parity='N',stopbits=1)   #open serial port
print(ser.name)
ser.write(hex(5).encode())
line=ser.read(20)
print(line)
ser.close()