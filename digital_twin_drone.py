#implemented during saeindia competition
import random
import matplotlib.pyplot as plt

wind_effects = random.randint(0, 1)
weather_type = ["windy", "clear", "rainy"]
weather_condition = random.choice(weather_type)

print(weather_condition)
print(wind_effects)

Obstacles = random.randint(0, 1)
print(Obstacles)

battery_log = 100
altitude_log = 0
speed_log = 5
gps_x_log = 0
gps_y_log = 0
battery_drain = 0.8

parameters = []
battery = []
speed = []
gps_x = []
gps_y = []
altitude = []

for i in range(1, 51):

    if weather_condition == "windy" or weather_condition == "rainy":
        battery_log -= (battery_drain * 1.5)
        print("Battery Level: ", battery_log)
        battery.append(battery_log)
    else:
        battery_log -= battery_drain
        print("Battery Level: ", battery_log)
        battery.append(battery_log)

    if wind_effects == 1:
        speed_log += random.randint(-1, 1)
        print("Speed :", speed_log)
        speed.append(speed_log)
    else:
        print(speed_log)
        speed.append(speed_log)

    if Obstacles == 1:
        gps_x_log += random.randint(-2, 2)
        gps_y_log += random.randint(-2, 2)
        altitude_log += 0.5

    print("GPS_X :", gps_x_log)
    print("GPS_Y :", gps_y_log)
    print("Altitude:", altitude_log)

    gps_x.append(gps_x_log)
    gps_y.append(gps_y_log)
    altitude.append(altitude_log)

    # health monitoring
    if battery_log < 20:
        print("Battery is less than threshold")

    if altitude_log < 0:
        print("Altitude is lesser than zero")

    if (gps_x_log>1 and gps_y_log > 1):
        print("GPS drift is greater than 1")
    


# visualisation

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(battery, marker="o")
plt.title("Battery Level vs Simulation Step")
plt.xlabel("Simulation Step")
plt.ylabel("Battery Level (%)")

plt.subplot(2, 2, 2)
plt.plot(gps_x, gps_y, marker="o")
plt.title("Drone GPS Path")
plt.xlabel("GPS X")
plt.ylabel("GPS Y")

plt.subplot(2, 2, 3)
plt.plot(altitude, marker="o")
plt.title("Altitude vs Simulation Step")
plt.xlabel("Simulation Step")
plt.ylabel("Altitude")

plt.tight_layout()
plt.show()