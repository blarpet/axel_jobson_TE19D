import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


nd = pd.read_csv("National_Daily_Deaths.csv")
nt = pd.read_csv("National_Total_Deaths_by_Age_Group.csv")  
labels = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90+"]


plt.pie(nt.Total_Deaths, labels = labels, autopct="%.2f %%")
plt.show()
