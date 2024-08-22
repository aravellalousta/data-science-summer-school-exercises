import numpy as np

beverages = np.array(['Coffee', 'Tea', 'Milk', 'Juice', 'Water'])
prices = np.array([1.5, 1.0, 0.5, 2.0, 0.7])
cheap_beverages = beverages[prices < 1.0]
print(cheap_beverages)