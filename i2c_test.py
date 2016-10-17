import smbus

i2c = smbus.SMBus(1)
i2c_addr = 0x20


gyroAddress = 0x68
x1Address = 0x53

try :
    i2c.write_byte(gyroAddress, 0)
    print "Device ID: " + str(i2c.read_byte(gyroAddress))

    i2c.write_byte(x1Address, 0)
    print "Device ID: " + str(i2c.read_byte(x1Address))
except IOError :
    print "error"
else :
    print "good"
