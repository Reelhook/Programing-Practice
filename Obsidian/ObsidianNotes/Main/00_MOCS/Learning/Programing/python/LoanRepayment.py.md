---
tags:
  - programming/python
  - project/program/py
---



This code implements a complete loan management system in Python with the following features:

1. **Data Persistence:** Loans are stored in a JSON file (`loans.json`). The functions `load_loans()` and `save_loans()` handle reading from and writing to this file, respectively.
    
2. **Loan Calculations:**
    
    - **Monthly Payment Calculation:** The function `calculate_monthly_payment()` computes the fixed monthly payment for a loan based on its principal, annual interest rate, and term (in years).
        
    - **Amortization Schedule:** The function `calculate_amortization()` generates the full payment schedule for a loan. This schedule includes, for each payment:
        
        - Payment number and date.
            
        - The fixed monthly payment.
            
        - The portion of the payment that is scheduled to reduce the principal.
            
        - Any additional payment made that month.
            
        - The interest paid.
            
        - The new remaining balance after the payment. It takes into account any extra principal payments, and stops once the balance reaches zero.
            
3. **Remaining Balance Update:**
    
    - The function `update_remaining_balance_for_loan()` calculates the remaining balance as of today (by iterating through the amortization schedule up to the current date) and stores it in the loan’s meta data under `"remaining_balance"`.
        
    - `update_all_remaining_balances()` goes through all stored loans and updates their remaining balance, saving the modifications.
        
4. **Visualization:**
    
    - `plot_amortization()` uses Matplotlib to graph the loan’s amortization schedule. It displays two plots:
        
        - A breakdown of the scheduled principal and interest portions of each payment, with a vertical line marking the current date.
            
        - A graph showing the remaining balance over time, also with a current date marker.
            
5. **User Interaction & Management:** A text menu (implemented in `main_menu()`) offers several commands:
    
    - **Add New Loan:** `add_loan()` prompts the user for details (principal, interest rate, term, start date) and creates a new loan entry with calculated monthly payment and initial remaining balance.
        
    - **View All Loans:** `view_loans()` displays a formatted list of all loans, including key details such as principal, rate, term, monthly payment, start date, and the updated remaining balance.
        
    - **Update Existing Loan:** `update_loan()` allows modifying an existing loan’s details. The monthly payment is recalculated after any change.
        
    - **Record Additional Payment:** `record_additional_payment()` lets the user record extra principal payments for a loan on specified dates. These payments are then factored into the amortization schedule.
        
    - **Show Payment Details:** `show_payment_details()` prints out detailed information for a selected loan, including its complete amortization schedule.
        
    - **Graph Loan Repayment:** `graph_loan()` graphs the repayment schedule for the selected loan using the plotting function.
        
    - **Exit:** This option terminates the program.
        

When the script is run (via the main menu in the `if __name__ == "__main__": main_menu()` block), the user is presented with these options to manage, update, and visualize their loans interactively.

In summary, the code provides a full-fledged CLI-based loan management tool that integrates loan calculations, extra payment tracking, real-time balance updates, and comprehensive visualization of the repayment schedule.