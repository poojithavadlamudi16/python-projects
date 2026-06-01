weather_data = {
    "hyderabad": "Sunny, 32°C",
    "mumbai": "Rainy, 28°C",
    "delhi": "Cloudy, 30°C"
}

def show_menu():
    print("\n=== Weather App ===")
    print("1. View weather")
    print("2. Add new city weather")
    print("3. Update existing city weather")
    print("4. Show all cities")
    print("5. Exit")

def view_weather():
    city = input("Enter city name: ").lower()
    if city in weather_data:
        print(f"The weather in {city.title()} is {weather_data[city]}.")
    else:
        print("Sorry, weather data for this city is not available.")

def add_weather():
    city = input("Enter new city name: ").lower()
    if city in weather_data:
        print("City already exists. Use update option instead.")
    else:
        condition = input("Enter weather condition (e.g., Sunny, 30°C): ")
        weather_data[city] = condition
        print(f"Weather data for {city.title()} added.")

def update_weather():
    city = input("Enter city name to update: ").lower()
    if city in weather_data:
        condition = input("Enter new weather condition: ")
        weather_data[city] = condition
        print(f"Weather data for {city.title()} updated.")
    else:
        print("City not found. Use add option instead.")

def show_all():
    print("\n--- All Cities Weather ---")
    for city, condition in weather_data.items():
        print(f"{city.title()}: {condition}")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_weather()
    elif choice == "2":
        add_weather()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        show_all()
    elif choice == "5":
        print("Exiting Weather App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")