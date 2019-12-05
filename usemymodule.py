import mymodule

degrees = mymodule.get_weather("FLORIDA")

print("Weather in FLORIDA is %.2f degrees celsius" % degrees)

location = mymodule.postal_lookup("B323PP")

print("Latitude %.2f and langitude is %.2f" % location)