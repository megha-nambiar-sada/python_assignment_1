def get_length_value():
    while True:
        user_input = input("Enter the length value: ")
        if user_input.lower() in ('q', 'quit'):
            print("Exiting program")
            exit()
        try:
            return float(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")

def get_unit(prompt):
    valid_units = ['mm', 'cm', 'm', 'km']
    while True:
        unit = input(prompt).lower()
        if unit in ('q', 'quit'):
            print("Exiting program")
            exit()
        if unit in valid_units:
            return unit
        else:
            print("Error: Please enter a valid unit like mm, cm, m, or km.")

def convert_length(value, from_unit, to_unit):
    
    to_meters = {
        'mm': value / 1000,
        'cm': value / 100,
        'm': value,
        'km': value * 1000
    }
    meters = to_meters[from_unit]

   
    from_meters = {
        'mm': meters * 1000,
        'cm': meters * 100,
        'm': meters,
        'km': meters / 1000
    }
    return from_meters[to_unit]

def length_converter():
    print("Welcome to the Length Unit Converter!")
    print("Supported units: mm, cm, m, km")
    print("Type 'q' or 'quit' at any prompt to exit.\n")

    while True:
        value = get_length_value()
        from_unit = get_unit("Enter the source unit (mm, cm, m, km): ")
        to_unit = get_unit("Enter the target unit (mm, cm, m, km): ")

        result = convert_length(value, from_unit, to_unit)
        print(f"✅ {value} {from_unit} is equal to {result} {to_unit}\n")

length_converter()
