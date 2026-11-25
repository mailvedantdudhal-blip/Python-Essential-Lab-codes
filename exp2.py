# Named Constants
EARTH_GRAVITY = 9.81   # N/kg
MOON_GRAVITY = 1.622   # N/kg


def calculate_weights(mass_kg):
    earth_weight = mass_kg * EARTH_GRAVITY
    moon_weight = mass_kg * MOON_GRAVITY
    return earth_weight, moon_weight


try:
    mass = float(input("Enter object mass in kg: "))
    if mass < 0:
        print("Error: Mass cannot be negative.")
    else:
        w_earth, w_moon = calculate_weights(mass)
        print(f"Weight on Earth: {w_earth:.2f} N")
        print(f"Weight on Moon: {w_moon:.2f} N")
except ValueError:
    print("Error: Please enter a valid numerical mass.")
