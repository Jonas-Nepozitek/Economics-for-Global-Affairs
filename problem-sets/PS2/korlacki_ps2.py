import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


dataset = "https://raw.githubusercontent.com/akhandelwal8/globaleconomics/refs/heads/main/hwk/hwk2_accounting.csv"

df = pd.read_csv(dataset,sep='\t')

a = 0.3

# 1A, y = Ak**0.3

# 1B

# 1C
k60 = df['cn1960']/df['pop1960']
y60 = df['cgdpo1960']/df['pop1960']
y18 = df['cgdpo2018']/df['pop2018']
k18 = df['cn2018']/df['pop2018']
A60 = y60/(k60**a)
A18 = y18/(k18**a)

lnk60 = np.log(k60)
lny60 = np.log(y60)
lnA60 = np.log(A60)
lny18 = np.log(y18)
lnk18 = np.log(k18)
lnA18 = np.log(A18)

print(f"The mean of ln A in 1960 is: {np.mean(lnA60)}\nThe standard deviation of ln A in 1960 is: {np.std(lnA60)}")

plt.figure()

'''

plt.figure()
plt.scatter(logy,logA,label='logA')
plt.scatter(logy,logk,label='logk')
plt.xlabel("Log(y)")
plt.legend()
plt.show()'''