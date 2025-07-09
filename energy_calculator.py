name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
area = input("Enter your area name: ")
flat_tenament = input("Are you living in Flat or Tenement: ")
facility = input("Are you living in 1BHK, 2BHK, 3BHK? ").lower()

cal_energy = 0

# Calculate base energy consumption based on housing type
if facility == "1bhk":
    cal_energy += 2 * 0.4 + 2 * 0.8  # 2.4 kWh
    rooms = "1BHK"
elif facility == "2bhk":
    cal_energy += 3 * 0.4 + 3 * 0.8  # 3.6 kWh
    rooms = "2BHK"
elif facility == "3bhk":
    cal_energy += 4 * 0.4 + 4 * 0.8  # 4.8 kWh
    rooms = "3BHK"
else:
    print("Invalid input for housing type!")
    exit()

# Check for AC usage
ac = input("Are you using AC? (yes/no): ").lower()
if ac == "yes":
    cal_energy += 3

# Check for Fridge usage
fridge = input("Are you using Fridge? (yes/no): ").lower()
if fridge == "yes":
    cal_energy += 3

# Check for Washing Machine usage (fixed the question)
wm = input("Are you using Washing Machine? (yes/no): ").lower()
if wm == "yes":
    cal_energy += 3

# Display results
print(f"\n--- Energy Consumption Report ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {area}, {city}")
print(f"Housing Type: {rooms} {flat_tenament}")
print(f"Total Daily Energy Consumption: {cal_energy} kWh")
print(f"Estimated Monthly Consumption: {cal_energy * 30} kWh")
print(f"Estimated Annual Consumption: {cal_energy * 365} kWh")