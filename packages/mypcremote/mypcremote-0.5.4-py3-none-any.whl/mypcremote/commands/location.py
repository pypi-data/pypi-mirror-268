import serial
import pynmea2

rx_pin = 14
tx_pin = 15

def Desc():
    return "This will obtain the latest GPS information and share it here"

def read_gps_data():
    ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=0.5)
    try:
        data = ser.readline().decode("utf-8")
        if "GPGGA" in data:
            msg = pynmea2.parse(data)
            return "https://www.google.com/maps/place/{},{}".format(msg.latitude, msg.longitude)
        return "Cannot reliability evaluate GPS data"

    except pynmea2.ParseError as e:
        return str(e)
    except Exception as e:
        return str(e)

async def Run(ctx):
    ctx.channel.send(read_gps_data())