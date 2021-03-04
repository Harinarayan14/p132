import pandas as pd
import csv
import matplotlib.pyplot as plt
df = pd.read_csv("gravity_data.csv")
mass_list = df["Mass"]
radius_list = df["Radius"]
gravity_list = df["gravity"]
plt.scatter(x=mass_list,y=radius_list, color= "red",  
            marker= "*", s=30) 
plt.xlabel('Mass') 
plt.ylabel('Radius') 
plt.title('Mass-Radius Graph Of Stars') 
plt.show() 

plt.scatter(x=mass_list,y=gravity_list, color= "red",  
            marker= "+", s=30) 
plt.xlabel('Mass') 
plt.ylabel('Gravity') 
plt.title('Mass-Gravity Graph Of Stars') 
plt.show() 