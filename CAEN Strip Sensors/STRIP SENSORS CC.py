import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

files= ['W23X221-25.csv', 'W23X223-25.csv', 'W23X441-25.csv', 'W23X443-25.csv', 'W63X151-25.csv', 'W123X111-25.csv', 'W153X111-25.csv' ,'W153X112-25.csv', 'W153X221-25.csv', 'W153X223-25.csv']
graph = [file.replace(".csv", "") for file in files]
for file in files:
    df=pd.read_csv(file)
    plt.plot(df['VMon'], df['IMon'])
plt.xlabel('Voltage [V]')
# plt.gca().invert_xaxis()
plt.ylabel('Current [uA]')
plt.legend(graph, loc='center right', bbox_to_anchor=(1.25, 0.5))
plt.title('CAEN I-V Characteristic Curve 25C')
plt.grid(True)
plt.tight_layout()
plt.show()
