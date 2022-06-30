from djitellopy import *

me = tello.Tello()
me.connect()

battery = me.get_battery()
temperature = me.get_temperature()

print("BAT",battery)
print("TEMP",temperature)