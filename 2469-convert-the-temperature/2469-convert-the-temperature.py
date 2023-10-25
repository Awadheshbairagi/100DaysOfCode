from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Convert Celsius to Kelvin using the formula: Kelvin = Celsius + 273.15
        kelvin = celsius + 273.15
        
        # Convert Celsius to Fahrenheit using the formula: Fahrenheit = Celsius * 1.80 + 32.00
        fahrenheit = celsius * 1.80 + 32.00
        
        # Return the results as a list [kelvin, fahrenheit]
        return [round(kelvin, 5), round(fahrenheit, 5)]
