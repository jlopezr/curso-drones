from djitellopy import tello

me = tello.Tello()
me.connect()

print(me.get_battery())