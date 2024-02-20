"""This task requires you to construct a program to record data about absences
in a workplace.
"""


def data_entered():
    absences = []
    while True:
        data = input("Enter employee name and number of days absent "
                     "(separated by a space), $ to finish: ")
        if data.strip() == "$":
            break
        name, days = data.split()
        absences.append((name, int(days)))
    return absences


def calculate_average(absences):
    total_days = sum(days for _, days in absences)
    return total_days / len(absences)


def find_most_absent(absences):
    most_absent = absences[0]
    for item in absences:
        if item[1] > most_absent[1]:
            most_absent = item
    return most_absent


def find_not_absent(absences):
    not_absent = [name for name, days in absences if days == 0]
    return not_absent


def find_above_average(absences, average):
    above_average = []
    for name, days in absences:
        if days > average:
            above_average.append((name, days))
    if above_average:
        max_days = above_average[0][1]
        most_absent = above_average[0]
        for name, days in above_average:
            if days > max_days:
                max_days = days
                most_absent = (name, days)
        return most_absent
    else:
        return None


def main():
    absences = data_entered()
    if not absences:
        print("No data provided")
        return
    average = calculate_average(absences)
    most_absent = find_most_absent(absences)
    not_absent = find_not_absent(absences)
    above_average = find_above_average(absences, average)
    print(f"Average number of days staff were absent: {average:.2f}")
    print(f"Person with most days absent: {most_absent[0]} with "
          f"{most_absent[1]} days")
    print("List of people not absent at all:")
    for name in not_absent:
        print(name)
    print("List of people absent above average:")
    for name, days in above_average:
        print(f"{name} {days}")


# Main Routine
main()
