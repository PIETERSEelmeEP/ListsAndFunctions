"""You will be designing basic software for a booking system for the local
University's vehicle booking system. It allows staff to borrow a vehicle for
the day, and keeps track of which vehicles have already been booked.
"""


def availability():
    return booked_by is None


# Main Routine
VEHICLE_LIST = [
    (1, 'Suzuki Van', 2),
    (2, 'Toyota Corolla', 4),
    (3, 'Honda CRV', 4),
    (4, 'Suzuki Swift', 4),
    (5, 'Mitsubishi Airtrek', 4),
    (6, 'Nissan DC Ute', 4),
    (7, 'Toyota Previa', 7),
    (8, 'Toyota Hi Ace', 12),
    (9, 'Toyota Hi Ace', 12)
]
number = 0
car_type = ""
seats = 0
booked_by = None
for vehicle in VEHICLE_LIST:
    print(f"{vehicle[0]} -- {vehicle[1]} -- {vehicle[2]}")

