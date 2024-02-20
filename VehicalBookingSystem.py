"""You will be designing basic software for a booking system for the local
University's vehicle booking system. It allows staff to borrow a vehicle for
the day, and keeps track of which vehicles have already been booked.
"""


def availability():
    global booked_by
    return booked_by is None


def book(name):
    global booked_by
    booked_by = name


def display_available_vehicles(seats_needed):
    print("VEHICLE NUMBER - TYPE - NO. SEATS")
    for vehicle in VEHICLE_LIST:
        if vehicle[2] < seats_needed:
            print(f"No. {vehicle[0]} -- {vehicle[1]} -- {vehicle[2]} seats -- "
                  f"Note: Don't have enough seats")
        else:
            print(f"No. {vehicle[0]} -- {vehicle[1]} -- {vehicle[2]} seats")


# Main Routine
VEHICLE_LIST = [
    (1, 'Suzuki Van', 2),
    (2, 'Toyota Corolla', 4),
    (3, 'Honda CRV', 4),
    (4, 'Suzuki Swift', 4),
    (5, 'Mitsubishi Air-trek', 4),
    (6, 'Nissan DC Ute', 4),
    (7, 'Toyota Pre-via', 7),
    (8, 'Toyota Hi Ace', 12),
    (9, 'Toyota Hi Ace', 12)
]
number = 0
car_type = ""
seats = 0
booked_by = None
number_seats = int(input("Please enter the number of seats required (Type -1 "
                         "to quit): "))
display_available_vehicles(number_seats)
