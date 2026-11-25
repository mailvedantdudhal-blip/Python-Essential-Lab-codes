def calculate_calories(carbs, fats, proteins):
    return (carbs * 4) + (fats * 9) + (proteins * 4)


try:
    c = float(input("Enter grams of carbohydrates: "))
    f = float(input("Enter grams of fats: "))
    p = float(input("Enter grams of proteins: "))

    total_cal = calculate_calories(c, f, p)
    print(f"\nTotal Daily Caloric Intake: {total_cal:.2f} kcal")
except ValueError:
    print("Error: Please enter valid numeric values for macronutrients.")
