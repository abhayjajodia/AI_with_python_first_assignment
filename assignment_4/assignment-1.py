import numpy as np
import matplotlib.pyplot as plt

# values of n (number of dice throws)
roll = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

for n in roll:
    # 1) simulate dice throws
    dice_1 = np.random.randint(1, 7, n)
    dice_2 = np.random.randint(1, 7, n)
    s = dice_1 + dice_2

    # 2) histogram
    h, h2 = np.histogram(s, range(2, 14))

    # 3) plot
    plt.bar(h2[:-1], h / n)
    plt.title(f"n = {n}")
    plt.xlabel("Sum of dice")
    plt.ylabel("Frequency")
    plt.show()
