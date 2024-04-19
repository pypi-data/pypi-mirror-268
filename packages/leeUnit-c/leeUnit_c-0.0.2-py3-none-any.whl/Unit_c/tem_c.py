# 섭씨 <-> 화씨 변환
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# 켈빈 <-> 섭씨 변환
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

# 화씨 <-> 켈빈 변환
def fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit