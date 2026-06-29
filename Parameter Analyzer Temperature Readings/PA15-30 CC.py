import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

files= ['W4BIG13-15.csv', 'W4BIG13-175.csv', 'W4BIG13-20.csv', 'W4BIG13-225.csv', 'W4BIG13-25.csv', 'W4BIG13-275.csv', 'W4BIG13-30.csv']
graph = [file.replace(".csv", "") for file in files]

for file in files:
    df = pd.read_csv(file, skiprows=4, header=None)
    x = df.iloc[:, 1]
    y = (-1*df.iloc[:, 2])
    plt.plot(x,y)

plt.xlabel('Voltage [V]')
plt.gca().invert_xaxis()
plt.ylabel('Current [uA]')
plt.legend(["15C","17.5C","20C","22.5C","25C","27.5C","30C"], loc='center right', bbox_to_anchor=(1.25, 0.5))
plt.title('Parameter Analyzer W4BIG1-3 I-V Characteristic Curve')
plt.grid(True)
plt.tight_layout()
plt.show()