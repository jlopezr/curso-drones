from djitellopy import tello

# Arrancar comunicacions amb Tello
me = tello.Tello()
me.connect()

# Obtenir bateria
battery = me.get_battery()
print(battery)

# Enlairament, moviments i aterrar
me.takeoff()
me.move_forward(300)
me.move_back(300)
me.land()
