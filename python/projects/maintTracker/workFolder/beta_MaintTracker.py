#!/usr/bin/env python3
import sqlite3
import datetime

DB_FILE = "vehicle_maintenance.db"


def create_database():
    """
    Creates the SQLite database and maintenance table if they do not already exist.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle TEXT NOT NULL,
            service_date TEXT NOT NULL,
            service_type TEXT NOT NULL,
            mileage INTEGER,
            cost REAL,
            details TEXT
        )
    """
    )
    conn.commit()
    return conn


def get_existing_vehicles(conn):
    """
    Retrieves a list of unique vehicle names from the maintenance table.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT vehicle FROM maintenance")
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def add_record(conn, vehicle, service_date, service_type, mileage, cost, details):
    """
    Inserts a new maintenance record into the database.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO maintenance (vehicle, service_date, service_type, mileage, cost, details)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (vehicle, service_date, service_type, mileage, cost, details),
    )
    conn.commit()


def view_records(conn):
    """
    Retrieves all maintenance records sorted by service date.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maintenance ORDER BY service_date ASC")
    return cursor.fetchall()


def generate_report(conn, filename="maintenance_report.md"):
    """
    Generates a Markdown report documenting all maintenance records.
    """
    records = view_records(conn)
    if not records:
        print("No maintenance records to document.")
        return

    with open(filename, "w") as report_file:
        report_file.write("# Vehicle Maintenance Report\n\n")
        report_file.write(
            f"Report generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )
        report_file.write(
            "| ID | Vehicle | Service Date | Service Type | Mileage | Cost | Details |\n"
        )
        report_file.write(
            "|----|---------|--------------|--------------|---------|------|---------|\n"
        )
        for rec in records:
            r_id, vehicle, service_date, service_type, mileage, cost, details = rec
            mileage_str = str(mileage) if mileage is not None else "-"
            cost_str = f"${cost:.2f}" if cost is not None else "-"
            details_str = details if details else "-"
            report_file.write(
                f"| {r_id} | {vehicle} | {service_date} | {service_type} | {mileage_str} | {cost_str} | {details_str} |\n"
            )
    print(f"Maintenance report has been generated in {filename}")


def remove_record(conn):
    """
    Removes a maintenance record based on user-specified ID.
    """
    records = view_records(conn)
    if not records:
        print("No maintenance records found to remove.")
        return

    print("Maintenance Records:")
    print("-" * 80)
    # Display records in a table-like format.
    print(
        f"{'ID':<4} {'Vehicle':<15} {'Date':<12} {'Service Type':<20} {'Mileage':<8} {'Cost':<8} {'Details'}"
    )
    print("-" * 80)
    for rec in records:
        r_id, vehicle, service_date, service_type, mileage, cost, details = rec
        mileage_str = str(mileage) if mileage is not None else "-"
        cost_str = f"${cost:.2f}" if cost is not None else "-"
        details_str = details if details else "-"
        print(
            f"{r_id:<4} {vehicle:<15} {service_date:<12} {service_type:<20} {mileage_str:<8} {cost_str:<8} {details_str}"
        )
    print("-" * 80)

    try:
        rec_id = int(input("Enter the ID of the record to remove: ").strip())
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maintenance WHERE id = ?", (rec_id,))
    result = cursor.fetchone()
    if result is None:
        print("Record with the specified ID does not exist.")
        return

    confirmation = (
        input(
            f"Are you sure you want to delete the record for '{result[1]}' on {result[2]}? (Y/n): "
        )
        .strip()
        .lower()
    )
    if confirmation == "y" or confirmation == "":
        cursor.execute("DELETE FROM maintenance WHERE id = ?", (rec_id,))
        conn.commit()
        print("Record removed successfully.")
    else:
        print("Deletion cancelled.")


def admin():
    conn = create_database()
    print("1. Update maintenance record")
    print("2. Remove maintenance record")
    selection = input("Enter your choice (1-2): ").strip()

    if selection == "1":
        remove_record(conn)
    elif selection == "2":
        pass


def main():
    conn = create_database()
    while True:
        print("\n--- Vehicle Maintenance Manager ---")
        print("1. Add maintenance record")
        print("2. View maintenance records")
        print("3. Generate maintenance documentation report")
        # print("4. Remove maintenance record")
        print("4. Admin Page")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\nEnter maintenance record details:")
            # Look up previously entered vehicles.
            existing_vehicles = get_existing_vehicles(conn)
            if existing_vehicles:
                use_existing = (
                    input("Would you like to use an existing vehicle? (Y/n): ")
                    .strip()
                    .lower()
                )
                if use_existing == "y" or use_existing == "":
                    print("Select a vehicle from the list below:")
                    for i, v in enumerate(existing_vehicles, start=1):
                        print(f"  {i}. {v}")
                    try:
                        sel = int(
                            input("Enter the number corresponding to the vehicle: ")
                        )
                        if 1 <= sel <= len(existing_vehicles):
                            vehicle = existing_vehicles[sel - 1]
                        else:
                            print(
                                "Invalid selection. Please enter the vehicle name manually."
                            )
                            vehicle = input(
                                "Enter vehicle name (e.g., 'Toyota Camry'): "
                            ).strip()
                    except ValueError:
                        print("Invalid input. Please enter the vehicle name manually.")
                        vehicle = input(
                            "Enter vehicle name (e.g., 'Toyota Camry'): "
                        ).strip()
                else:
                    vehicle = input(
                        "Enter vehicle name (e.g., 'Toyota Camry'): "
                    ).strip()
            else:
                vehicle = input("Enter vehicle name (e.g., 'Toyota Camry'): ").strip()

            service_date = input("Service date (YYYY-MM-DD): ").strip()
            # Validate date format.
            try:
                datetime.datetime.strptime(service_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format, please use YYYY-MM-DD.")
                continue

            # Instead of freeform entry, provide a list of maintenance types.
            maintenance_options = [
                "Oil, Engine Change",
                "Oil, Rear Axle",
                "Oil, Front Axle",
                "Oil, TransmissionTires, Replacement",
                "Tires, Rotation",
                "Tires, Balance",
                "Battery, Replacement",
                "Battery, Aux Replacement",
                "Air Filter, Engine",
                "Air Filter, Cabin",
            ]
            print("Select maintenance type:")
            for i, option in enumerate(maintenance_options, start=1):
                print(f"  {i}. {option}")
            try:
                opt_choice = int(
                    input(
                        "Enter the number corresponding to the maintenance type: "
                    ).strip()
                )
                if 1 <= opt_choice <= len(maintenance_options):
                    service_type = maintenance_options[opt_choice - 1]
                else:
                    print("Invalid selection. Defaulting to Oil Change.")
                    service_type = maintenance_options[0]
            except ValueError:
                print("Invalid input. Defaulting to Oil Change.")
                service_type = maintenance_options[0]

            mileage_input = input("Current mileage (optional): ").strip()
            cost_input = input("Cost (optional): ").strip()
            details = input("Additional details (optional): ").strip()

            mileage = int(mileage_input) if mileage_input.isdigit() else None
            try:
                cost = float(cost_input) if cost_input else None
            except ValueError:
                cost = None

            add_record(
                conn, vehicle, service_date, service_type, mileage, cost, details
            )
            print("Maintenance record added successfully!")

        elif choice == "2":
            records = view_records(conn)
            if not records:
                print("No maintenance records found.")
            else:
                print("\nMaintenance Records:")
                print("-" * 80)
                for rec in records:
                    print(rec)
                print("-" * 80)

        elif choice == "3":
            generate_report(conn)

        elif choice == "4":
            admin(conn)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")

    conn.close()


if __name__ == "__main__":
    main()
