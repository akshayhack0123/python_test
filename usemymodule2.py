import mymodule as utility

degrees = utility.get_weather("FLORIDA")

print("Weather in FLORIDA is %.2f degrees celsius" % degrees)

location = utility.postal_lookup("B323PP")

print("Latitude %.2f and langitude is %.2f" % location)