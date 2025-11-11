def check_clothing_recommendation():
    print("Welcome to Rohan's Clothing Advisor!")
    
    while True:
        try:
            temp_input = input("Please enter the current temperature in Celsius (°C): ")
            current_temp = float(temp_input)
            break
        except ValueError:
            print("Invalid input. Please enter a numerical temperature (e.g., 22.5).")

    if current_temp >= 20:
        print(f"\nTemperature: {current_temp}°C")
        print(" Recommendation: The weather is perfect for light and soft clothes!")
        print("   Enjoy wearing a T-shirt, light shirt, or simple dress.")

    elif current_temp >= 10 and current_temp < 20:
        print(f"\nTemperature: {current_temp}°C")
        print(" Recommendation: It's a bit cool. You might need a light sweater or long-sleeve shirt.")
        print("   A light pullover is ideal for this range.")

    else:
        print(f"\nTemperature: {current_temp}°C")
        print(" Recommendation: It's cold! It's best to wear your jacket and pullover to stay warm.")
        print("   Definitely do not skip the weather-appropriate layers!")

if __name__ == "__main__":
    check_clothing_recommendation()