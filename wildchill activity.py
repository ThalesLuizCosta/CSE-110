def calculate_windchill(temperature, wind_speed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16
    return windchill

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    temperatures = list(range(-20, 11))  # Lista de temperaturas de -20°C a 10°C
    wind_speeds = [2, 4, 6, 8, 10]       # Lista de velocidades do vento em m/s

    print("Temperatura (°C)  Velocidade do Vento (m/s)  Sensação Térmica (°C)")
    print("-" * 50)

    for temperature in temperatures:
        for wind_speed in wind_speeds:
            windchill_celsius = calculate_windchill(temperature, wind_speed)
            windchill_fahrenheit = convert_celsius_to_fahrenheit(windchill_celsius)
            print(f"{temperature:^10} {wind_speed:^25} {windchill_celsius:.2f}°C / {windchill_fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
