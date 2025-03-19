import pandas as pd

cars = pd.read_csv('data_C02_emission.csv')

    

print(cars.head(5))

print({len(cars)})

print(cars.dtypes)

print(f"null: {cars.isnull().sum()}")
cars.dropna(axis=0)

print(f"Duplicate: {cars.duplicated().sum()}")
cars.drop_duplicates()


cars[['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']] = cars[['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']].astype('category')

print(cars.dtypes)




fuel_consumption = cars.sort_values(by='Fuel Consumption City (L/100km)', ascending = False)
print("The biggest consumers: ")
print(fuel_consumption[["Make", "Model", "Fuel Consumption City (L/100km)"]].head(3))
print("The  smallest consumers:")
print(fuel_consumption[["Make", "Model", "Fuel Consumption City (L/100km)"]].tail(3))



cars_by_motor = cars[(cars["Engine Size (L)"]>2.5) & (cars["Engine Size (L)"]<3.5)]
print(f"{len(cars_by_motor)} 2.5L < 3.5L")
print(f"CO2:  {cars_by_motor["CO2 Emissions (g/km)"].mean()}")



audi_cars = cars[ cars["Make"] == "Audi"]
print(f"Audi count: {len(audi_cars)}")
print(f"CO2 for audi with 4 cylinders {audi_cars[audi_cars["Cylinders"]==4]["CO2 Emissions (g/km)"].mean()}")




cars_by_cylinders = cars[(cars["Cylinders"]%2==0) & (cars["Cylinders"] > 2) ]
grouped_by_cylinders = cars_by_cylinders.groupby(by=["Cylinders"])
for cylinder_count, group in grouped_by_cylinders:
    print(f"{cylinder_count} cylinders: {len(group)} cars")
print(grouped_by_cylinders["CO2 Emissions (g/km)"].mean())



grouped_by_fuel = cars.groupby(by = "Fuel Type")
print(f"Average city consumption for diesels {grouped_by_fuel.get_group("D")["Fuel Consumption City (L/100km)"].mean()}")
print(f"Average city consumption for gas stations {grouped_by_fuel.get_group("X")["Fuel Consumption City (L/100km)"].mean()}")




diesel_cars_with_4cylinders = cars[(cars["Cylinders"]==4) & (cars["Fuel Type"]=="D")]
print(f"Biggest consumption: {diesel_cars_with_4cylinders.sort_values(by = "Fuel Consumption City (L/100km)")[["Make", "Fuel Consumption City (L/100km)"]].head(1)}")




cars_with_manual = cars[cars["Transmission"].str.startswith("M")]
print(f"Manual transmission {len(cars_with_manual)}")



print (cars.corr(numeric_only = True))
print("Korelacija")

