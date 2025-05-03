import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import os
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

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


def calculate_monthly_payment(principal, annual_rate, term_years):
    """Calculate the fixed monthly payment."""
    monthly_rate = annual_rate / 100 / 12
    total_months = term_years * 12
    monthly_payment = (
        principal
        * (monthly_rate * (1 + monthly_rate) ** total_months)
        / ((1 + monthly_rate) ** total_months - 1)
    )
    return monthly_payment


def calculate_amortization(
    principal, annual_rate, term_years, start_date=None, additional_payments=None
):
    """
    Compute the loan amortization schedule including additional payments.

    Returns a list of tuples in the format:
      (payment number, payment date, monthly_payment, scheduled_principal,
       additional_payment, interest_payment, new_balance)
    """
    monthly_rate = annual_rate / 100 / 12
    total_months = term_years * 12
    monthly_payment = calculate_monthly_payment(principal, annual_rate, term_years)

    if additional_payments is None:
        additional_payments = []
    # Sort additional payments by date (assumed to be in "YYYY-MM-DD" format)
    additional_payments = sorted(additional_payments, key=lambda x: x["date"])

    schedule = []
    balance = principal

    # If no start date provided, use the first day of next month
    if start_date is None:
        start_date = date.today().replace(day=1) + relativedelta(months=1)
    elif isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()

    for month in range(total_months):
        payment_date = start_date + relativedelta(months=month)
        date_str = payment_date.strftime("%Y-%m-%d")
        interest_payment = balance * monthly_rate
        scheduled_principal = monthly_payment - interest_payment

        # Sum all additional payments matching this payment date
        additional_payment = sum(
            p["amount"] for p in additional_payments if p["date"] == date_str
        )
        total_principal_payment = scheduled_principal + additional_payment

        # Avoid paying more than the remaining balance
        if total_principal_payment > balance:
            total_principal_payment = balance
            if scheduled_principal < balance:
                additional_payment = balance - scheduled_principal
            else:
                additional_payment = 0

        new_balance = balance - total_principal_payment

        schedule.append(
            (
                month + 1,  # Payment number
                date_str,  # Payment date
                monthly_payment,
                scheduled_principal,
                additional_payment,
                interest_payment,
                new_balance,
            )
        )

        balance = new_balance
        if balance <= 0:
            break
    return schedule


def plot_amortization(schedule, loan_name):
    """Graph the loan repayment schedule with a marker for the current date."""
    dates = [datetime.strptime(entry[1], "%Y-%m-%d") for entry in schedule]
    principal_payments = [entry[3] for entry in schedule]
    interest_payments = [entry[5] for entry in schedule]
    remaining_balances = [entry[6] for entry in schedule]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Plot scheduled principal and interest payments
    ax1.plot(dates, principal_payments, label="Scheduled Principal", color="green")
    ax1.plot(dates, interest_payments, label="Interest Payment", color="red")
    ax1.set_title(f"Monthly Payment Breakdown - {loan_name}")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Amount ($)")
    ax1.legend()
    ax1.grid(True)

    # Add vertical current date marker
    current_date = datetime.now()
    ax1.axvline(x=current_date, color="purple", linestyle="--", label="Current Date")

    # Plot remaining balance over time
    ax2.plot(dates, remaining_balances, label="Remaining Balance", color="blue")
    ax2.set_title(f"Remaining Loan Balance Over Time - {loan_name}")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Balance ($)")
    ax2.legend()
    ax2.grid(True)
    ax2.axvline(x=current_date, color="purple", linestyle="--", label="Current Date")

    # Rotate date labels
    for ax in [ax1, ax2]:
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

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
        start_date = input(
            "Enter loan start date (YYYY-MM-DD) or press Enter for next month: "
        ).strip()
        if not start_date:
            start_date = (
                date.today().replace(day=1) + relativedelta(months=1)
            ).strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid input. Loan not added.")
        return

    monthly_payment = calculate_monthly_payment(principal, annual_rate, term_years)

    loans[loan_name] = {
        "principal": principal,
        "annual_rate": annual_rate,
        "term_years": term_years,
        "start_date": start_date,
        "monthly_payment": monthly_payment,
        "date_added": datetime.now().strftime("%Y-%m-%d"),
        "additional_payments": [],  # Initialize an empty list for extra payments
    }

    save_loans(loans)
    print(f"\nLoan '{loan_name}' has been added successfully!")
    print(f"Monthly Payment: ${monthly_payment:.2f}")


def view_loans():
    """Display all stored loans."""
    loans = load_loans()
    if not loans:
        print("\nNo loans found in the system.")
        return

    print("\nCurrent Loans:")
    print("-" * 105)
    print(
        f"{'Loan Name':<15} {'Principal':<12} {'Rate':<8} {'Term':<8} {'Monthly':<12} {'Start Date':<12} {'Added':<12}"
    )
    print("-" * 105)
    for name, details in loans.items():
        print(
            f"{name:<15} ${details['principal']:<11,.2f} "
            f"{details['annual_rate']:<8}% {details['term_years']:<8} "
            f"${details['monthly_payment']:<11,.2f} {details['start_date']:<12} "
            f"{details['date_added']:<12}"
        )


def show_payment_details():
    """Show detailed payment information for a selected loan."""
    loans = load_loans()
    if not loans:
        print("\nNo loans found in the system.")
        return

    view_loans()
    loan_name = input("\nEnter the name of the loan to view payment details: ").strip()
    if loan_name not in loans:
        print("Loan not found!")
        return

    loan = loans[loan_name]
    schedule = calculate_amortization(
        loan["principal"],
        loan["annual_rate"],
        loan["term_years"],
        loan["start_date"],
        loan.get("additional_payments", []),
    )

    print(f"\nPayment Details for '{loan_name}'")
    print(f"Monthly Payment: ${loan['monthly_payment']:.2f}")
    print(f"Total Loan Amount: ${loan['principal']:.2f}")
    print(f"Annual Interest Rate: {loan['annual_rate']}%")
    print(f"Loan Term: {loan['term_years']} years")
    print(f"Start Date: {loan['start_date']}")

    total_interest = sum(payment[5] for payment in schedule)
    print(f"Total Interest Over Loan Term: ${total_interest:.2f}")

    print("\nPayment Schedule:")
    print("-" * 105)
    print(
        f"{'Pmt #':<6} {'Date':<12} {'Payment':<12} {'Sch. Prin.':<12} {'Add. Prin.':<12} {'Interest':<12} {'Balance':<12}"
    )
    print("-" * 105)
    for payment in schedule:
        print(
            f"{payment[0]:<6} {payment[1]:<12} ${payment[2]:<11,.2f} "
            f"${payment[3]:<11,.2f} ${payment[4]:<11,.2f} ${payment[5]:<11,.2f} ${payment[6]:<11,.2f}"
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
        start_date_input = input(
            f"Start date (current: {loans[loan_name]['start_date']}): "
        ).strip()

        if principal_input:
            loans[loan_name]["principal"] = float(principal_input)
        if rate_input:
            loans[loan_name]["annual_rate"] = float(rate_input)
        if term_input:
            loans[loan_name]["term_years"] = int(term_input)
        if start_date_input:
            try:
                datetime.strptime(start_date_input, "%Y-%m-%d")
                loans[loan_name]["start_date"] = start_date_input
            except ValueError:
                print("Invalid date format. Start date not updated.")

        # Recalculate monthly payment
        loans[loan_name]["monthly_payment"] = calculate_monthly_payment(
            loans[loan_name]["principal"],
            loans[loan_name]["annual_rate"],
            loans[loan_name]["term_years"],
        )

        save_loans(loans)
        print(f"Loan '{loan_name}' has been updated successfully!")
        print(f"New monthly payment: ${loans[loan_name]['monthly_payment']:.2f}")

    except ValueError:
        print("Invalid input. Loan not updated.")


def record_additional_payment():
    """Record an additional payment toward the principal for a specific loan."""
    loans = load_loans()
    if not loans:
        print("\nNo loans found in the system.")
        return

    view_loans()
    loan_name = input(
        "\nEnter the loan name to record an additional payment for: "
    ).strip()
    if loan_name not in loans:
        print("Loan not found!")
        return

    try:
        amount = float(input("Enter additional payment amount ($): "))
    except ValueError:
        print("Invalid amount.")
        return

    pay_date = input(
        "Enter payment date (YYYY-MM-DD) or press Enter for today's date: "
    ).strip()
    if not pay_date:
        pay_date = date.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(pay_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

    loan = loans[loan_name]
    if "additional_payments" not in loan:
        loan["additional_payments"] = []
    loan["additional_payments"].append({"date": pay_date, "amount": amount})
    save_loans(loans)
    print(
        f"Recorded additional payment of ${amount:.2f} on {pay_date} for loan '{loan_name}'."
    )


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
        loan["principal"],
        loan["annual_rate"],
        loan["term_years"],
        loan["start_date"],
        loan.get("additional_payments", []),
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
        print("5. Show Payment Details")
        print("6. Record Additional Payment")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()
        if choice == "1":
            add_loan()
        elif choice == "2":
            view_loans()
        elif choice == "3":
            update_loan()
        elif choice == "4":
            graph_loan()
        elif choice == "5":
            show_payment_details()
        elif choice == "6":
            record_additional_payment()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
