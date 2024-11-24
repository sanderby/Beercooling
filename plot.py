import numpy as np
import matplotlib.pyplot as plt

def T_air(t):
    return 23 + (4.6 - 23) * np.exp(-t / 455)

def T_water(t):
    return 23 + (4.6 - 23) * np.exp(-t / 5.4)


t_values = np.linspace(0, 240, 120)

#Model prediction for air 5 min
print(T_air(5))
#Model prediction for water 1 min
print(T_water(1))


plt.plot(t_values, T_air(t_values), label = "luft", color='blue')
plt.plot(t_values, T_water(t_values),label = "vann" , color='red')
plt.plot(5, 6.6, "bo")
plt.plot(1,8.9, "ro")
plt.grid(True)
plt.legend()
plt.show()

