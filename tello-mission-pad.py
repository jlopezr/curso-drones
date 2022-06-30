from djitellopy import *

me = tello.Tello()
me.connect()

battery = me.get_battery()
temperature = me.get_temperature()

print("BAT",battery)
print("TEMP",temperature)

me.enable_mission_pads()
me.set_mission_pad_detection_direction(1)

pad = me.get_mission_pad_id()

while pad != 1:        
    pad = me.get_mission_pad_id()
    print("PAD", pad)
    
me.disable_mission_pads()
me.end()

