class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (9/5) * c + 32  # Convert Celsius to Fahrenheit

# Calling the static method directly on the class
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")
