import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df= pd.read_csv("epa-sea-level.csv")
plot1=plt.scatter(data=df,x='Year',y='CSIRO Adjusted Sea Level')
plt.show()
