def calculate_endurance(fuel_litres, fuel_consumption):
    if fuel_consumption == 0:
        print("Error: Fuel consumption cannot be zero.")
        return None
    
    try:
        endurance_minutes = fuel_litres / fuel_consumption
        return endurance_minutes
    
    except ZeroDivisionError:
        print("Error: Fuel consumption cannot be zero.")
        return None

fuel_litres = 50.0
fuel_consumption = 0.0 
endurance = calculate_endurance(fuel_litres, fuel_consumption)

if endurance is not None:
    print(f"Remaining endurance: {endurance:.2f} minutes")
else:
    print("Endurance calc failed.")
