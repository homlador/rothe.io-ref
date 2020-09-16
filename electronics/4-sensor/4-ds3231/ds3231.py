DS3231_I2C_ADDR = 104

def bcd2dec(bcd):
    return (((bcd & 0b11110000) >> 4) * 10 + (bcd & 0b00001111))

def dec2bcd(dec):
    t = dec // 10
    o = dec - t * 10
    return (t << 4) + o

def tobytes(num):
    return num.to_bytes(1, 'little')

class DS3231:
    def __init__(self, i2c):
        self.i2c = i2c

    def get_time(self):
        if not DS3231_I2C_ADDR in self.i2c.scan():
            return False
        data = self.i2c.readfrom_mem(DS3231_I2C_ADDR, 0, 7)
        seconds = bcd2dec(data[0] & 0b01111111)
        minutes = bcd2dec(data[1] & 0b01111111)
        if data[2] & 0b01000000 > 0:
            hours = bcd2dec(data[2] & 0b00011111)
            if data[2] & 0b00100000 > 0:
                hours += 12
        else:
            hours = bcd2dec(data[2] & 0b00111111)
        day_of_week = data[3]
        days = bcd2dec(data[4] & 0b00111111)
        months = bcd2dec(data[5] & 0b00011111)
        years = bcd2dec(data[6]) + 1900
        if data[5] & 0b10000000 > 0:
            years = years + 100
        return (years, months, days, day_of_week, hours, minutes, seconds)

    def set_time(self, time):
        years, months, days, day_of_week, hours, minutes, seconds = time
        self.i2c.writeto_mem(DS3231_I2C_ADDR, 0, tobytes(dec2bcd(seconds)))
        self.i2c.writeto_mem(DS3231_I2C_ADDR, 1, tobytes(dec2bcd(minutes)))
        self.i2c.writeto_mem(DS3231_I2C_ADDR, 2, tobytes(dec2bcd(hours)))
        self.i2c.writeto_mem(DS3231_I2C_ADDR, 3, tobytes(dec2bcd(day_of_week)))
        self.i2c.writeto_mem(DS3231_I2C_ADDR, 4, tobytes(dec2bcd(days)))
        if years >= 2000:
            self.i2c.writeto_mem(DS3231_I2C_ADDR, 5, tobytes(dec2bcd(months) | 0b10000000))
            self.i2c.writeto_mem(DS3231_I2C_ADDR, 6, tobytes(dec2bcd(years - 2000)))
        else:
            self.i2c.writeto_mem(DS3231_I2C_ADDR, 5, tobytes(dec2bcd(months)))
            self.i2c.writeto_mem(DS3231_I2C_ADDR, 6, tobytes(dec2bcd(years - 1900)))
