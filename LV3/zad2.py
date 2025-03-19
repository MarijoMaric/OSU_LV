import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_CO2_emission.csv')

plt.figure(figsize=(10, 6))
data['CO2 Emissions (g/km)'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of CO2 Emissions')
plt.xlabel('CO2 Emissions (g/km)')
plt.ylabel('Number of Vehicles')
plt.grid(True)
plt.show()


data = pd.read_csv('data_CO2_emission.csv')

plt.figure(figsize=(10, 6))
scatter = plt.scatter(data['Fuel Consumption City (L/100km)'], 
                      data['CO2 Emissions (g/km)'], 
                      c=data['Fuel Type'].astype('category').cat.codes, 
                      cmap='viridis', 
                      alpha=0.6)
plt.title('City Fuel Consumption vs CO2 Emissions')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')
plt.colorbar(scatter, label='Fuel Type (Encoded)')
plt.grid(True)
plt.show()


data = pd.read_csv('data_CO2_emission.csv')

plt.figure(figsize=(12, 6))
data.boxplot(column='Fuel Consumption Hwy (L/100km)', by='Fuel Type', grid=True)
plt.title('Highway Fuel Consumption by Fuel Type')
plt.suptitle('') 
plt.xlabel('Fuel Type')
plt.ylabel('Fuel Consumption Hwy (L/100km)')
plt.show()

data = pd.read_csv('data_CO2_emission.csv')

fuel_counts = data.groupby('Fuel Type').size()
plt.figure(figsize=(10, 6))
fuel_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Number of Vehicles by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Vehicles')
plt.grid(True)
plt.show()

data = pd.read_csv('data_CO2_emission.csv')

cylinder_avg_co2 = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
plt.figure(figsize=(10, 6))
cylinder_avg_co2.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Average CO2 Emissions by Number of Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Average CO2 Emissions (g/km)')
plt.grid(True)
plt.show()

