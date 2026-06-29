import matplotlib.pyplot as plt
import numpy as np 
import os
import pandas as pd

files= ['W4BIG13-15.csv', 'W4BIG13-20.csv', 'W4BIG13-25.csv',]
graph = [file.replace("csv", "") for file in files]
for file in files:
    df=pd.read_csv(file)
    plt.plot(df['VMon'], df['IMon'])
plt.xlabel('Voltage [V]')
plt.gca().invert_xaxis()
plt.ylabel('Current [uA]')
plt.legend(["15C","20C","25C"], loc='center right', bbox_to_anchor=(1.25, 0.5))
plt.title('CAEN W4BIG1-3 I-V Characteristic Curve')
plt.grid(True)
plt.tight_layout()
plt.show()
