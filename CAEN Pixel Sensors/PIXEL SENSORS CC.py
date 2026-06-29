import matplotlib.pyplot as plt
import numpy as np 
import os
import pandas as pd

files= ['W4BIG13-25.csv', 'W4BIG24-25.csv', 'W4SMOL12-25.csv', 'W4SMOL23-25.csv', 'W7BIG13-25.csv', 'W7BIG26-25.csv', 'W7SMOL12-25.csv', 'W7SMOL21-25.csv']
graph = [file.replace(".csv", "") for file in files]
for file in files:
    df=pd.read_csv(file)
    plt.plot(df['VMon'], df['IMon'])
plt.xlabel('Voltage [V]')
plt.gca().invert_xaxis()
plt.ylabel('Current [uA]')
plt.legend(graph, loc='center right', bbox_to_anchor=(1.25, 0.5))
plt.title('CAEN I-V Characteristic Curve 25C')
plt.grid(True)
plt.tight_layout()
plt.show()
