import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pwd = os.getcwd()

dataset = 'hwk1_convergence.csv'

df = pd.read_csv(pwd+'\\'+dataset,sep='\t')
                
gdp60 = df['gdppc1960']
gdp00 = df['gdppc2000']
n = 40.0
g = np.log(gdp00/gdp60)/n

# Part 1
plt.figure()
plt.hist(g,bins=np.arange(np.min(g),np.max(g)+0.01,0.01))
plt.title("Average Annual Growth Rate")
plt.xlabel("Growth Rate")
plt.show()

# Part 2
print(f"The percentiles of the growth rates are:\n\t10th: {np.nanpercentile(g,10)} \
      \n\t25th: {np.nanpercentile(g,25)}\n\t50th: {np.nanpercentile(g,50)}\n\t75th: {np.nanpercentile(g,75)} \
      \n\t90th: {np.nanpercentile(g,90)}")