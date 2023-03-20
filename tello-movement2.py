from djitellopy import *

me = tello.Tello()
me.connect()

me.takeoff()
me.move_forward(200)
me.move_left(100)
me.move_right(200)
me.move_left(100)
me.move_back(200)

me.land()
me.end()
