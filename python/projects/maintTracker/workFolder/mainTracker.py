import json
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt  # Make sure this package is installed

DATA_FILE = "cars_data.json"


def load_data():
    """
    Load the car data from a JSON file.
    If the file doesn't exist, return an empty dictionary.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}
    return data


def save_data(data):
    """
    Save the car data to a JSON file.
    """
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_car(data):
    """
    Add a new car entry.
    Each car is uniquely identified by an ID (this could be a license plate or any unique string).
    """
    print("\nAdding a new car:")
    car_id = input("Enter a unique car ID (e.g., license plate): ").strip().lower()
    if car_id in data:
        print("A car with that ID already exists!")
        return data

    make = input("Enter the car make: ").strip().lower()
    model = input("Enter the car model: ").strip().lower()
    year_input = input("Enter the car year: ").strip().lower()
    odometer_input = input("Enter the current odometer reading: ").strip().lower()

    try:
        year = int(year_input)
    except ValueError:
        print("Invalid year input. Defaulting year to 0.")
        year = 0

    try:
        odometer = float(odometer_input)
    except ValueError:
        print("Invalid odometer reading. Defaulting odometer to 0.")
        odometer = 0.0

    data[car_id] = {
        "make": make,
        "model": model,
        "year": year,
        "odometer": odometer,
        "maintenance": [],  # List of maintenance records
    }
    print("Car added successfully!")
    return data


def list_cars(data):
    """
    List all the cars with their details.
    """
    if not data:
        print("\nNo cars available.")
        return

    print("\nCurrent cars in the system:")
    for car_id, info in data.items():
        print(
            f"ID: {car_id} | {info['year']} {info['make']} {info['model']} | Odometer: {info['odometer']} miles"
        )


def update_odometer(data):
    """
    Update the odometer reading for a specific car.
    """
    car_id = input("\nEnter car ID to update its odometer: ").strip().lower()
    if car_id not in data:
        print("Car not found!")
        return data

    new_reading = input("Enter the new odometer reading: ").strip().lower()
    try:
        new_reading = float(new_reading)
    except ValueError:
        print("Invalid input. Odometer not updated.")
        return data

    data[car_id]["odometer"] = new_reading
    print("Odometer updated!")
    return data


def add_maintenance_record(data):
    """
    Add a maintenance record for a given car.
    Supports both mileage-based and time-based intervals.
    You can specify:
      - the maintenance task,
      - the interval in miles until next maintenance,
      - the time interval in days until next maintenance,
      - and any additional notes.
    """
    car_id = input("\nEnter car ID for adding a maintenance record: ").strip().lower()
    if car_id not in data:
        print("Car not found!")
        return data

    task = (
        input("Enter the maintenance task (e.g., Oil change, Tire rotation): ")
        .strip()
        .lower()
    )
    due_interval_input = (
        input(
            "Enter the interval in miles until next maintenance (enter 0 if not applicable): "
        )
        .strip()
        .lower()
    )
    due_days_input = (
        input(
            "Enter the time interval in days until next maintenance (enter 0 if not applicable): "
        )
        .strip()
        .lower()
    )
    notes = input("Any additional notes (optional): ").strip().lower()

    try:
        due_interval = float(due_interval_input)
    except ValueError:
        print("Invalid mileage interval. Setting it to 0.")
        due_interval = 0.0

    try:
        due_days = float(due_days_input)
    except ValueError:
        print("Invalid time interval. Setting it to 0.")
        due_days = 0.0

    # Record the current odometer reading along with today's date.
    current_odometer = data[car_id]["odometer"]
    date_str = datetime.now().strftime("%Y-%m-%d")
    record = {
        "task": task,
        "date": date_str,
        "recorded_odometer": current_odometer,
        "due_interval": due_interval,  # Interval in miles
        "due_days": due_days,  # Interval in days
        "notes": notes,
    }
    data[car_id]["maintenance"].append(record)
    print("Maintenance record added!")
    return data


def view_maintenance(data):
    """
    Display all maintenance records for a specified car.
    """
    car_id = input("\nEnter car ID to view its maintenance records: ").strip().lower()
    if car_id not in data:
        print("Car not found!")
        return

    records = data[car_id]["maintenance"]
    if not records:
        print("No maintenance records found for this car.")
    else:
        print(f"\nMaintenance records for car ID '{car_id}':")
        for index, record in enumerate(records, start=1):
            print(f"\nRecord {index}:")
            print(f"  Date: {record['date']}")
            print(f"  Task: {record['task']}")
            print(f"  Odometer at record: {record['recorded_odometer']} miles")
            if record["due_interval"] > 0:
                print(f"  Mileage interval: {record['due_interval']} miles")
            if record["due_days"] > 0:
                print(f"  Time interval: {record['due_days']} days")
            print(f"  Notes: {record['notes']}")
            print("-" * 40)


def check_maintenance_due(data):
    """
    Check if maintenance is due for a specific car based on:
      - Mileage: if the miles driven since the record exceed due_interval.
      - Time: if the current date is past the due date computed from due_days.
    """
    car_id = input("\nEnter car ID to check maintenance due: ").strip().lower()
    if car_id not in data:
        print("Car not found!")
        return

    current_odometer = data[car_id]["odometer"]
    today = datetime.now()
    records = data[car_id]["maintenance"]
    due_tasks = []

    for record in records:
        task_due = False
        reasons = []
        # Check mileage interval
        if record.get("due_interval", 0) > 0:
            if (current_odometer - record["recorded_odometer"]) >= record[
                "due_interval"
            ]:
                task_due = True
                reasons.append("Mileage")

        # Check time interval
        if record.get("due_days", 0) > 0:
            record_date = datetime.strptime(record["date"], "%Y-%m-%d")
            due_date = record_date + timedelta(days=record["due_days"])
            if today >= due_date:
                task_due = True
                reasons.append("Time")

        if task_due:
            due_tasks.append((record, reasons))

    if due_tasks:
        print("\nThe following maintenance tasks are due:")
        for record, reasons in due_tasks:
            print(f"\nTask: {record['task']}")
            print(
                f"  Last performed on: {record['date']} at {record['recorded_odometer']} miles"
            )
            print(f"  Due reasons: {', '.join(reasons)}")
            if record["due_interval"] > 0:
                due_mileage = record["recorded_odometer"] + record["due_interval"]
                print(
                    f"  Mileage due at: {due_mileage} miles (Current: {current_odometer} miles)"
                )
            if record["due_days"] > 0:
                record_date = datetime.strptime(record["date"], "%Y-%m-%d")
                due_date = record_date + timedelta(days=record["due_days"])
                print(
                    f"  Time due on: {due_date.strftime('%Y-%m-%d')} (Today: {today.strftime('%Y-%m-%d')})"
                )
            print("-" * 40)
    else:
        print("No maintenance tasks are currently due based on mileage or time.")


def show_upcoming_maintenance_all(data):
    """
    Display upcoming maintenance tasks for all cars.
    Supports upcoming checks based on both:
      - Mileage: within a user-defined mile threshold.
      - Time: within a user-defined day threshold.
    For each maintenance record, the function calculates how far the next maintenance is:
      - For mileage: the difference between due mileage and current odometer.
      - For time: the number of days until the due date.
    """
    if not data:
        print("\nNo cars found in the system.")
        return

    threshold_miles_input = (
        input("\nEnter the mileage threshold to consider maintenance as upcoming: ")
        .strip()
        .lower()
    )
    threshold_days_input = (
        input(
            "Enter the time threshold (in days) to consider maintenance as upcoming: "
        )
        .strip()
        .lower()
    )
    try:
        threshold_miles = float(threshold_miles_input)
    except ValueError:
        print("Invalid mileage threshold. Setting mileage threshold to 500 miles.")
        threshold_miles = 500.0
    try:
        threshold_days = float(threshold_days_input)
    except ValueError:
        print("Invalid day threshold. Setting day threshold to 30 days.")
        threshold_days = 30.0

    found = False
    today = datetime.now()

    print("\nUpcoming maintenance tasks for all cars:")
    for car_id, info in data.items():
        current_odometer = info["odometer"]
        for record in info["maintenance"]:
            upcoming = False
            messages = []
            # Check mileage upcoming condition
            if record.get("due_interval", 0) > 0:
                due_mileage = record["recorded_odometer"] + record["due_interval"]
                miles_remaining = due_mileage - current_odometer
                if 0 <= miles_remaining <= threshold_miles:
                    upcoming = True
                    messages.append(
                        f"Mileage: Due at {due_mileage} miles (in {miles_remaining} miles)"
                    )
            # Check time upcoming condition
            if record.get("due_days", 0) > 0:
                record_date = datetime.strptime(record["date"], "%Y-%m-%d")
                due_date = record_date + timedelta(days=record["due_days"])
                days_remaining = (due_date - today).days
                if 0 <= days_remaining <= threshold_days:
                    upcoming = True
                    messages.append(
                        f"Time: Due on {due_date.strftime('%Y-%m-%d')} (in {days_remaining} days)"
                    )

            if upcoming:
                print(
                    f"\nCar ID: {car_id} ({info['year']} {info['make']} {info['model']})"
                )
                print(f"  Task: {record['task']}")
                print(
                    f"  Last performed on: {record['date']} at {record['recorded_odometer']} miles"
                )
                if record["notes"]:
                    print(f"  Notes: {record['notes']}")
                for msg in messages:
                    print(f"  {msg}")
                print("-" * 40)
                found = True

    if not found:
        print("No upcoming maintenance tasks found within the specified thresholds.")


def graph_maintenance_data(data):
    """
    Graph the maintenance history for a specific car.
    The plot displays the maintenance events over time, with the x-axis as the date
    and the y-axis as the recorded odometer reading. Each point is annotated with the task name.
    """
    car_id = input("\nEnter car ID for graphing maintenance history: ").strip().lower()
    if car_id not in data:
        print("Car not found!")
        return

    records = data[car_id]["maintenance"]
    if not records:
        print("No maintenance records to graph for this car.")
        return

    # Sort records by date
    try:
        sorted_records = sorted(
            records, key=lambda r: datetime.strptime(r["date"], "%Y-%m-%d")
        )
    except Exception as e:
        print("Error processing records:", e)
        return

    dates = [datetime.strptime(record["date"], "%Y-%m-%d") for record in sorted_records]
    odometers = [record["recorded_odometer"] for record in sorted_records]
    tasks = [record["task"] for record in sorted_records]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, odometers, marker="o", linestyle="-", color="b")
    plt.xlabel("Date")
    plt.ylabel("Odometer Reading (miles)")
    plt.title(f"Maintenance History for Car ID: {car_id}")
    plt.grid(True)

    # Annotate each point with the maintenance task name
    for i, task in enumerate(tasks):
        plt.annotate(
            task,
            (dates[i], odometers[i]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    plt.tight_layout()
    plt.show()


def main():
    """
    Main loop: presents a menu and lets the user choose various maintenance tracking options.
    """
    data = load_data()
    while True:
        print("\n========== Car Maintenance Tracker ==========")
        print("1. Add new car")
        print("2. List all cars")
        print("3. Update car odometer")
        print("4. Add maintenance record")
        print("5. View maintenance records")
        print("6. Check maintenance due for a car")
        print("7. Show upcoming maintenance for all cars")
        print("8. Graph maintenance data for a car")
        print("9. Exit")
        choice = input("Choose an option (1-9): ").strip().lower()

        if choice == "1":
            data = add_car(data)
            save_data(data)
        elif choice == "2":
            list_cars(data)
        elif choice == "3":
            data = update_odometer(data)
            save_data(data)
        elif choice == "4":
            data = add_maintenance_record(data)
            save_data(data)
        elif choice == "5":
            view_maintenance(data)
        elif choice == "6":
            check_maintenance_due(data)
        elif choice == "7":
            show_upcoming_maintenance_all(data)
        elif choice == "8":
            graph_maintenance_data(data)
        elif choice == "9":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
