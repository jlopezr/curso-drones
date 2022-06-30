from djitellopy import *

me = tello.Tello()
me.connect()

battery = me.get_battery()
temperature = me.get_temperature()

print("BAT",battery)
print("TEMP",temperature)

me.enable_mission_pads()
me.set_mission_pad_detection_direction(1)


me.takeoff()

#tello.send_expansion_command("led 255 0 0")
#me.move_forward(300)
#me.move_left(200)
#me.move_right(200)
#me.move_left(200)
#me.move_back(300)

pad = me.get_mission_pad_id()

while pad != 1:
    if pad == 3:
        me.move_back(30)
        me.rotate_clockwise(90)
        
    if pad == 4:
        me.move_up(30)
        
    pad = me.get_mission_pad_id()
    print("PAD", pad)
    
me.disable_mission_pads()
me.land()
me.end()