def get_category(bmi):
    if bmi < 18.5: return "Underweight", "Consider eating more nutrient-rich foods and consulting a doctor."
    if bmi < 25.0: return "Normal weight", "Great! Maintain your balanced diet and regular exercise."
    if bmi < 30.0: return "Overweight", "Try a modest calorie deficit and increased physical activity."
    return "Obese", "Please consult a healthcare professional for a personalised plan."

unit = input("Unit system — M for metric (kg/cm) or I for imperial (lb/ft/in): ").strip().upper()

if unit == "M":
    h = float(input("Height (cm): ")) / 100
    w = float(input("Weight (kg): "))
elif unit == "I":
    ft = float(input("Height (ft): "))
    inch = float(input("Height (in): "))
    w = float(input("Weight (lb): ")) * 0.453592
    h = (ft * 12 + inch) * 0.0254
else:
    print("Invalid input. Please enter M or I.")
    exit()

bmi = w / h ** 2
category, suggestion = get_category(bmi)

print(f"\nBMI: {bmi:.1f} — {category}")
print(f"Suggestion: {suggestion}")

