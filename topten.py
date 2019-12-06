import csv
import matplotlib.pyplot as plt
import numpy as np


medals = [263, 280, 285, 360, 433, 434, 440, 457, 625, 653]
country = ['RUS', 'AUT', 'SUI', 'GER', 'SWE', 'FIN', 'URS', 'NOR', 'CAN', 'USA']

y_pos = np.arange(len(country))

plt.title("Top Ten Countries by Total Medals")
plt.barh(y_pos, medals)
plt.yticks(y_pos, country)
plt.show()