import pandas as pd
import matplotlib.pyplot as plt

parameters_data = pd.read_excel("parameters_dataset.xlsx")

parameters_data["Simulation Step"] = range(1, len(parameters_data) + 1)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(
    parameters_data["Simulation Step"],
    parameters_data["battery_log"],
    marker="o"
)
plt.title("Battery Level vs Simulation Step")
plt.xlabel("Simulation Step")
plt.ylabel("Battery Level (%)")

plt.subplot(2, 2, 3)
plt.plot(
    parameters_data["gps_x_log"],
    parameters_data["gps_y_log"],
    marker="o"
)
plt.title("Drone GPS Path")
plt.xlabel("GPS X")
plt.ylabel("GPS Y")


plt.subplot(2, 2, 4)
plt.plot(
    parameters_data["Simulation Step"],
    parameters_data["altitude_log"],
    marker="o"
)
plt.title("Altitude vs Simulation Step")
plt.xlabel("Simulation Step")
plt.ylabel("Altitude")


plt.tight_layout()
plt.show()