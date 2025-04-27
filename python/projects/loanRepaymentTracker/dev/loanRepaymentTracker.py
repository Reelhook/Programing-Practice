import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

LOANS_FILE = "loans.json"


def load_loans():
    """Load existing loans from JSON file."""
    if os.path.exists(LOANS_FILE):
        with open(LOANS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def save_loans(loans):
    """Save loans to JSON file."""
    with open(LOANS_FILE, "w") as f:
        json.dump(loans, f, indent=4)


def calculate_amortization(principal, annual_rate, term_years):
    """
    Compute the loan amortization schedule.
    Returns a list of tuples containing monthly payment details.
    """
    monthly_rate = annual_rate / 100 / 12
    total_months = term_years * 12

    monthly_payment = (
        principal
        * (monthly_rate * (1 + monthly_rate) ** total_months)
        / ((1 + monthly_rate) ** total_months - 1)
    )

    schedule = []
    balance = principal

    for month in range(1, total_months + 1):
        interest_payment = balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment

        if balance < 0:
            balance = 0

        schedule.append(
            (month, monthly_payment, principal_payment, interest_payment, balance)
        )

    return schedule


def plot_amortization(schedule, loan_name):
    """Graph the loan repayment schedule with loan name in the title."""
    months = [entry[0] for entry in schedule]
    principal_payments = [entry[2] for entry in schedule]
    interest_payments = [entry[3] for entry in schedule]
    remaining_balances = [entry[4] for entry in schedule]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Plot the breakdown of each payment
    ax1.plot(months, principal_payments, label="Principal Payment", color="green")
    ax1.plot(months, interest_payments, label="Interest Payment", color="red")
    ax1.set_title(f"Monthly Payment Breakdown - {loan_name}")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Amount ($)")
    ax1.legend()
    ax1.grid(True)

    # Plot the remaining balance over time
    ax2.plot(months, remaining_balances, label="Remaining Balance", color="blue")
    ax2.set_title(f"Remaining Loan Balance Over Time - {loan_name}")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Balance ($)")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


def add_loan():
    """Add a new loan to the system."""
    loans = load_loans()

    print("\nAdding New Loan")
    loan_name = input("Enter a name for this loan: ").strip()

    if loan_name in loans:
        print("A loan with that name already exists!")
        return

    try:
        principal = float(input("Enter the principal loan amount ($): "))
        annual_rate = float(input("Enter the annual interest rate (%): "))
        term_years = int(input("Enter the term of the loan in years: "))
    except ValueError:
        print("Invalid input. Loan not added.")
        return

    loans[loan_name] = {
        "principal": principal,
        "annual_rate": annual_rate,
        "term_years": term_years,
        "date_added": datetime.now().strftime("%Y-%m-%d"),
    }

    save_loans(loans)
    print(f"Loan '{loan_name}' has been added successfully!")


def view_loans():
    """Display all stored loans."""
    loans = load_loans()

    if not loans:
        print("\nNo loans found in the system.")
        return

    print("\nCurrent Loans:")
    print("-" * 70)
    print(
        f"{'Loan Name':<20} {'Principal':<15} {'Rate':<10} {'Term':<10} {'Date Added':<15}"
    )
    print("-" * 70)

    for name, details in loans.items():
        print(
            f"{name:<20} ${details['principal']:<14,.2f} {details['annual_rate']:<10}% "
            f"{details['term_years']:<10} {details['date_added']:<15}"
        )


def update_loan():
    """Update an existing loan's details."""
    loans = load_loans()

    if not loans:
        print("\nNo loans found in the system.")
        return

    view_loans()
    loan_name = input("\nEnter the name of the loan to update: ").strip()

    if loan_name not in loans:
        print("Loan not found!")
        return

    print("\nEnter new values (or press Enter to keep current values):")

    try:
        principal_input = input(
            f"Principal (current: ${loans[loan_name]['principal']}): "
        ).strip()
        rate_input = input(
            f"Annual rate (current: {loans[loan_name]['annual_rate']}%): "
        ).strip()
        term_input = input(
            f"Term in years (current: {loans[loan_name]['term_years']}): "
        ).strip()

        if principal_input:
            loans[loan_name]["principal"] = float(principal_input)
        if rate_input:
            loans[loan_name]["annual_rate"] = float(rate_input)
        if term_input:
            loans[loan_name]["term_years"] = int(term_input)

        save_loans(loans)
        print(f"Loan '{loan_name}' has been updated successfully!")

    except ValueError:
        print("Invalid input. Loan not updated.")


def graph_loan():
    """Select and graph a loan's amortization schedule."""
    loans = load_loans()

    if not loans:
        print("\nNo loans found in the system.")
        return

    view_loans()
    loan_name = input("\nEnter the name of the loan to graph: ").strip()

    if loan_name not in loans:
        print("Loan not found!")
        return

    loan = loans[loan_name]
    schedule = calculate_amortization(
        loan["principal"], loan["annual_rate"], loan["term_years"]
    )
    plot_amortization(schedule, loan_name)


def main_menu():
    """Display and handle the main menu options."""
    while True:
        print("\n=== Loan Management System ===")
        print("1. Add New Loan")
        print("2. View All Loans")
        print("3. Update Existing Loan")
        print("4. Graph Loan Repayment")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_loan()
        elif choice == "2":
            view_loans()
        elif choice == "3":
            update_loan()
        elif choice == "4":
            graph_loan()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
