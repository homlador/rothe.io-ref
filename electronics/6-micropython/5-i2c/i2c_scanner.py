import machine

#scl = machine.Pin(22)
#sda = machine.Pin(21)

scl = machine.Pin(5)
sda = machine.Pin(4)
i2c = machine.I2C(-1, scl, sda)

led = machine.Pin(5, machine.Pin.OUT)
print("Scan i2c bus...")
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print("i2c devices found: ",len(devices))
    for device in devices:  
        print("Address: ",device," | Address: ",hex(device))
