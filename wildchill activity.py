def calculate_windchill(temperature, wind_speed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16
    return windchill

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    start_temperature = -20  # Starting temperature in Celsius
    end_temperature = 10    # Ending temperature in Celsius
    wind_speed = 5          # Wind speed in m/s

    print("Temperature (°C)  Windchill (°C)")
    print("-" * 30)

    for temperature in range(start_temperature, end_temperature + 1):
        windchill_celsius = calculate_windchill(temperature, wind_speed)
        windchill_fahrenheit = convert_celsius_to_fahrenheit(windchill_celsius)
        print(f"{temperature:^10} {windchill_celsius:.2f}°C / {windchill_fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
