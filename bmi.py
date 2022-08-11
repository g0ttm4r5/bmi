print("BMI Rechner!")

weight_str = input("Bitte gib dein Gewicht in kg ein: ")
height_str = input("Bitte gib deine Körpergröße in m ein: ")

weight = float(weight_str.replace(",", "."))
height = float(height_str.replace(",", "."))

print("Gewicht: " + weight_str)
print("Größe: " + height_str)

bmi = weight / height ** 2

print("Der BMI ist: " + str(round(bmi, 2)))
