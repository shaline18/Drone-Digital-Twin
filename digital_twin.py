#implemented and changed after the saeindia competition
import random
import matplotlib.pyplot as plt
print("The randomly selected wind effect condition:")
wind_effects = random.randint(0, 1)
print(wind_effects)
#0-no effects
#1-wind effect
if(wind_effects==0):
    print("No effect")
else:
    print("Wind effect is there")
print("The randomly selected weather type is:")
weather_type = ["windy", "clear", "rainy"]

weather_condition = random.choice(weather_type)

print(weather_condition)

print("The randomly Obstacle situation:")
Obstacles = random.randint(0, 1)
print(Obstacles)
if(Obstacles==0):
    print("Obstacle is not there")
else:
    print("Obstacle present")

battery_log = 100
altitude_log = 10
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

    # Environment conditions
    weather_condition = random.choice(weather_type)
    wind_effects = random.randint(0, 1)
    Obstacles = random.randint(0, 1)

    # Battery
    if weather_condition == "windy" or weather_condition == "rainy":
        battery_log -= (battery_drain * 1.5)
    else:
        battery_log -= battery_drain

    if battery_log < 0:
        battery_log = 0

    print("Battery Level:", battery_log)
    battery.append(battery_log)

    # Speed
    if wind_effects == 1:
        speed_log += random.randint(-1, 1)

        if speed_log < 0:
            speed_log = 0

        print("Speed:", speed_log)
        speed.append(speed_log)
    else:
        print("Speed:", speed_log)
        speed.append(speed_log)

    # GPS movement
    gps_x_log += 1
    gps_y_log += 1

    # Obstacle effect
    if Obstacles == 1:
        gps_x_log += random.randint(-2, 2)
        gps_y_log += random.randint(-2, 2)
        altitude_log += random.uniform(-0.5, 0.5)
    else:
        altitude_log += random.uniform(-0.2, 0.2)

    print("GPS_X:", gps_x_log)
    print("GPS_Y:", gps_y_log)
    print("Altitude:", altitude_log)

    gps_x.append(gps_x_log)
    gps_y.append(gps_y_log)
    altitude.append(altitude_log)

    # Health monitoring
    if battery_log < 20:
        print("Battery is less than threshold")

    if altitude_log < 0:
        print("Altitude is lesser than zero")

    # GPS drift
    gps_drift_x = abs(gps_x_log - i)
    gps_drift_y = abs(gps_y_log - i)

    if gps_drift_x > 1 or gps_drift_y > 1:
        print("GPS drift is greater than 1")

# Visualisation

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