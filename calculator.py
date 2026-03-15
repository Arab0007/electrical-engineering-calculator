# Electrical Engineering Calculator

def ohms_law():
    print("Ohm's Law Calculator")
    v = float(input("Enter Voltage (V): "))
    r = float(input("Enter Resistance (Ω): "))
    i = v / r
    print("Current =", i, "Amps")

def power():
    print("Power Calculator")
    v = float(input("Enter Voltage (V): "))
    i = float(input("Enter Current (A): "))
    p = v * i
    print("Power =", p, "Watts")

print("Electrical Engineering Calculator")
print("1. Ohm's Law")
print("2. Power")

choice = input("Choose option: ")

if choice == "1":
    ohms_law()

elif choice == "2":
    power()
