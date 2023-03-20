from djitellopy import tello

me = tello.Tello()
me.connect()

battery = me.get_battery()
print(battery)