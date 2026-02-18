#Problem 5 - Weather Forecast

temperature = int(input("Enter the temperature: "))
condition = input("Enter the weather condition: ")

if temperature < 32:
    if condition == "snowing":
        print("Bundle up! It's cold and snowy outside.")
    elif condition == "raining":
        print("Stay dry! It's cold and rainy outside.")
    else:
        print("Stay warm! It's cold outside.")
elif temperature > 80:
    if condition == "sunny":
        print("Stay cool! It's hot and sunny outside.")
    elif condition == "cloudy":
        print("Stay hydrated! It's hot and cloudy outside.")
    else:
        print("Stay indoors! It's hot outside.")
else:
    if condition == "sunny":
        print("Enjoy the weather! It's sunny outside.")
    elif condition == "cloudy":
        print("Don't forget your umbrella! It's cloudy outside.")
    else:
        print("Be prepared! It's", condition, "outside.")