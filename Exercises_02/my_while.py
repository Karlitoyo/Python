kelvin_values = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390]

def convert_temperature(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return kelvin, celsius, fahrenheit

for kelvin in kelvin_values:
    k, c, f = convert_temperature(kelvin)
    print(f"{k} K = {c:.2f} °C = {f:.2f} °F")

