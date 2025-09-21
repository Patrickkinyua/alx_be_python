weather1 = "sunny"
weather2 = "rainy"
weather3 = "cold"

user_input = input("Enter the weather condition (sunny, rainy, cold): ").strip().lower()

if user_input == weather1:
    print(" Wear a t-shirt and sunglasses.")
elif user_input == weather2:
    print(" don't forget your umbrella and raincoat.")
elif user_input == weather3:
    print(" Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
# This program provides clothing advice based on the weather condition input by the user.