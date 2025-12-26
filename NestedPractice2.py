'''
Write a Python program that:
Takes driver speed (in km/h) as input.

Checks the type of road:
"highway" → speed limit 100 km/h
"city" → speed limit 50 km/h
"residential" → speed limit 30 km/h

Based on the speed, determine the penalty:
Within limit → “No penalty”
Slightly over (≤10 km/h above limit) → “Warning”
Moderately over (11–30 km/h above limit) → “Fine: $100”
Severely over (>30 km/h above limit) → “Fine: $500 and license suspension”
'''
# Take speed input from the user (in km/h)
Speed = int(input("Enter the speed (in km/h): "))

# Take road type input and convert to lowercase for consistency
road_type = input("Enter the road type (highway, city, residential): ").lower()

# HIGHWAY LOGIC
if road_type == "highway":
    # Check if speed is within the legal limit (≤ 100 km/h)
    if Speed <= 100:
        print("Within limit: No penalty")
    else:
        # Slightly over speed limit: 101–110 km/h
        if Speed <= 110:
            print("Slightly over limit: Warning!")
        else:
            # Moderately over speed limit: 111–130 km/h
            if Speed <= 130:
                print("Moderately over speed limit (Fine): $100")
            else:
                # Severely over speed limit: >130 km/h
                print("Severely over speed limit: Fine $500 + suspension")

# CITY ROAD LOGIC
elif road_type == "city":
    # Check if speed is within the legal limit (≤ 50 km/h)
    if Speed <= 50:
        print("Within limit: No penalty")
    else:
        # Slightly over speed limit: 51–60 km/h
        if Speed <= 60:
            print("Slightly over limit: Warning!")
        else:
            # Moderately over speed limit: 61–70 km/h
            if Speed <= 70:
                print("Moderately over speed limit (Fine): $100")
            else:
                # Severely over speed limit: >70 km/h
                print("Severely over speed limit: Fine $500 + suspension")

# RESIDENTIAL ROAD LOGIC
elif road_type == "residential":
    # Check if speed is within the legal limit (≤ 30 km/h)
    if Speed <= 30:
        print("Within limit: No penalty")
    else:
        # Slightly over speed limit: 31–40 km/h
        if Speed <= 40:
            print("Slightly over limit: Warning!")
        else:
            # Moderately over speed limit: 41–50 km/h
            if Speed <= 50:
                print("Moderately over speed limit (Fine): $100")
            else:
                # Severely over speed limit: >50 km/h
                print("Severely over speed limit (Fine): $500 + license suspension")

