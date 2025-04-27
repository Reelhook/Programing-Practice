import matplotlib

matplotlib.use("TkAgg")  # or 'Qt5Agg' if you prefer
import matplotlib.pyplot as plt


def calculate_amortization(principal, annual_rate, term_years):
    """
    Compute the loan amortization schedule.

    Arguments:
    - principal: The total loan amount.
    - annual_rate: The annual interest rate (in percentage).
    - term_years: The term of the loan in years.

    Returns:
    - schedule: A list of tuples in the format:
      (month number, monthly payment, principal portion, interest portion, remaining balance)
    """
    monthly_rate = annual_rate / 100 / 12
    total_months = term_years * 12

    # Calculate the fixed monthly payment using the amortization formula.
    monthly_payment = (
        principal
        * (monthly_rate * (1 + monthly_rate) ** total_months)
        / ((1 + monthly_rate) ** total_months - 1)
    )

    schedule = []
    balance = principal

    for month in range(1, total_months + 1):
        # Interest for the current month:
        interest_payment = balance * monthly_rate
        # Principal is the remaining part of the fixed monthly payment:
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment

        # Ensure the balance doesn't go negative:
        if balance < 0:
            balance = 0

        schedule.append(
            (month, monthly_payment, principal_payment, interest_payment, balance)
        )

    return schedule


def plot_amortization(schedule):
    """
    Graph the loan repayment schedule.

    Creates two subplots:
      1. Monthly Payment Breakdown (Principal vs. Interest)
      2. Remaining Loan Balance over Time
    """
    months = [entry[0] for entry in schedule]
    principal_payments = [entry[2] for entry in schedule]
    interest_payments = [entry[3] for entry in schedule]
    remaining_balances = [entry[4] for entry in schedule]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Plot the breakdown of each payment:
    ax1.plot(months, principal_payments, label="Principal Payment", color="green")
    ax1.plot(months, interest_payments, label="Interest Payment", color="red")
    ax1.set_title("Monthly Payment Breakdown")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Amount ($)")
    ax1.legend()
    ax1.grid(True)

    # Plot the remaining balance over time:
    ax2.plot(months, remaining_balances, label="Remaining Balance", color="blue")
    ax2.set_title("Remaining Loan Balance Over Time")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Balance ($)")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


def main():
    """
    Main function prompting for loan details, calculating the schedule,
    and graphing the repayment data.
    """
    print("Loan Repayment Graph Generator")
    principal = float(input("Enter the principal loan amount ($): "))
    annual_rate = float(input("Enter the annual interest rate (%): "))
    term_years = int(input("Enter the term of the loan in years: "))

    schedule = calculate_amortization(principal, annual_rate, term_years)
    plot_amortization(schedule)


if __name__ == "__main__":
    main()
