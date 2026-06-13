# Simple Agriculture AI Agent

print("=== Agriculture AI Agent ===")

temperature = float(input("Enter temperature (°C): "))
rainfall = float(input("Enter rainfall (mm): "))

if temperature > 25 and rainfall > 100:
    crop = "Rice"
elif 20 <= temperature <= 30 and 50 <= rainfall <= 100:
    crop = "Maize"
elif 15 <= temperature <= 25 and rainfall < 50:
    crop = "Wheat"
else:
    crop = "Suitable crop not found"

print("Recommended Crop:", crop)
