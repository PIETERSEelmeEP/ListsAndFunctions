def display_available_vehicles(seats_needed):
    print("VEHICLE NUMBER - TYPE - NO. SEATS")
    available_count = 0
    for vehicle in VEHICLE_LIST:
        if vehicle[2] >= seats_needed and vehicle[3]:
            print(f"No. {vehicle[0]} - {vehicle[1]} - {vehicle[2]} seats")
            available_count += 1
        elif vehicle[3]:
            print(f"No. {vehicle[0]} - {vehicle[1]} - {vehicle[2]} seats - "
                  f"NOTE: Not have enough seats")
    return available_count


# Main Routine
VEHICLE_LIST = [
    (1, 'Suzuki Van', 2, True),
    (2, 'Toyota Corolla', 4, True),
    (3, 'Honda CRV', 4, True),
    (4, 'Suzuki Swift', 4, True),
    (5, 'Mitsubishi Air-trek', 4, True),
    (6, 'Nissan DC Ute', 4, True),
    (7, 'Toyota Pre-via', 7, True),
    (8, 'Toyota Hi Ace', 12, True),
    (9, 'Toyota Hi Ace', 12, True)
]

booked_vehicles = []

print("Vehicle Booking System")
print("Enter -1 to quit at any time.")

while True:
    while True:
        print()
        number_seats = int(input("Please enter the number of seats required: "
                                 ""))
        if number_seats == -1:
            break
        print()
        available_count = display_available_vehicles(number_seats)
        print()
        if available_count == 0:
            print("No vehicles available with the specified number of seats.")
            break
        vehicle_number = int(input("Enter the number of the vehicle to be "
                                   "booked: "))
        if vehicle_number < 1 or vehicle_number > len(VEHICLE_LIST):
            print("Invalid vehicle number. Please try again.")
            continue
        if not VEHICLE_LIST[vehicle_number - 1][3]:
            print("The vehicle is already booked. Please select another "
                  "vehicle.")
            continue
        name = input("Enter your name: ")
        booked_vehicles.append((vehicle_number, VEHICLE_LIST[vehicle_number -
                                                             1][1], name))
        print(f"{VEHICLE_LIST[vehicle_number - 1][1]} booked by {name}")
        VEHICLE_LIST[vehicle_number - 1] = (VEHICLE_LIST[vehicle_number - 1][0]
                                            , VEHICLE_LIST[vehicle_number - 1]
                                            [1], VEHICLE_LIST[vehicle_number -
                                                              1][2], False)
        print("#" * 20)
    if number_seats == -1:
        break

print("\nVEHICLES BOOKED TODAY:\n")
for vehicle in booked_vehicles:
    print(f"No. {vehicle[0]} - {vehicle[1]} - Booked by: {vehicle[2]}")
