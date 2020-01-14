km = int(input("Please enter kilometers to drive: "))
liters = int(input("Please enter liters-per-kilometers usage of the car: "))
price = int(input("Please enter price per liter of fuel: "))

km_per_liters = km/liters
total_fuel_cost = km_per_liters*price
print(int(total_fuel_cost))
