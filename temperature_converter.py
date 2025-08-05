def get_temperature_input():
    while True:
        temp_input = input("Enter the temperature value: ")
        if temp_input.lower() in ('q', 'quit'):
            print("Exiting program. Goodbye!")
            exit()
        try:
            return float(temp_input)
        except ValueError:
            print("Error: Please enter a valid number.")

def display_menu():
    print("\nChoose a conversion option:")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("q: Quit")

def convert_temperature(choice, temp):
    if choice == '1':
        return f"{temp}°C = {(temp * 9/5) + 32}°F"
    elif choice == '2':
        return f"{temp}°F = {(temp - 32) * 5/9}°C"
    elif choice == '3':
        return f"{temp}°C = {temp + 273.15}K"
    elif choice == '4':
        return f"{temp}K = {temp - 273.15}°C"

def temperature_converter():
    print("Welcome to the Interactive Temperature Converter!")
    print("You can type 'q' or 'quit' at any time to exit.")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice.lower() in ('q', 'quit'):
            print("Exiting program. Goodbye!")
            break
        elif choice in ('1', '2', '3', '4'):
            temp = get_temperature_input()
            result = convert_temperature(choice, temp)
            print("✅ Result:", result)
        else:
            print("Error: Invalid choice. Please select a valid option (1-4 or 'q').")


temperature_converter()
