import datetime


def calculate_monthly_salary(basic, housing, transport, overtime_hours):
    # Standard UAE hourly overtime rate is Basic Salary / 30 days / 8 hours * 1.25
    hourly_rate = (basic / 30) / 8
    overtime_pay = overtime_hours * hourly_rate * 1.25
    total_salary = basic + housing + transport + overtime_pay
    return overtime_pay, total_salary


def calculate_uae_gratuity(basic_salary, years_of_service):
    # UAE Labor Law End-of-Service Gratuity Rules:
    # - Less than 1 year: 0 AED
    # - 1 to 5 years: 21 days of basic salary per year
    # - More than 5 years: 21 days/year for first 5 years + 30 days/year after 5 years
    daily_basic = basic_salary / 30

    if years_of_service < 1:
        gratuity = 0.0
    elif years_of_service <= 5:
        gratuity = 21 * daily_basic * years_of_service
    else:
        first_five_years = 21 * daily_basic * 5
        remaining_years = 30 * daily_basic * (years_of_service - 5)
        gratuity = first_five_years + remaining_years

    # Gratuity cannot exceed 2 years' total basic salary under UAE law
    max_gratuity = basic_salary * 24
    return min(gratuity, max_gratuity)


def save_payslip(emp_name, emp_id, basic, housing, transport, overtime_pay, total_salary, years, gratuity):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    slip = [
        "\n==================================================",
        " UAE EMPLOYEE PAYSLIP & GRATUITY ",
        f"Generated Date : {now}",
        f"Employee Name : {emp_name} (ID: {emp_id})",
        "--------------------------------------------------",
        f"Basic Salary : {basic:,.2f} AED",
        f"Housing Allowance : {housing:,.2f} AED",
        f"Transport Allowance : {transport:,.2f} AED",
        f"Overtime Pay (1.25x): {overtime_pay:,.2f} AED",
        "--------------------------------------------------",
        f"TOTAL MONTHLY PAY : {total_salary:,.2f} AED",
        "--------------------------------------------------",
        f"Service Completed : {years} Years",
        f"End-of-Service Gratuity (UAE Law): {gratuity:,.2f} AED",
        "==================================================\n"
    ]
    slip_text = "\n".join(slip)
    print(slip_text)

    with open("employee_payslip_log.txt", "a") as file:
        file.write(slip_text)
    print("Payslip saved to 'employee_payslip_log.txt'.")


def main():
    print("==================================================")
    print(" UAE SALARY & END-OF-SERVICE GRATUITY TOOL ")
    print("==================================================")

    try:
        emp_name = input("Enter Employee Name: ").strip() or "Employee"
        emp_id = input("Enter Employee ID (e.g., DXB-101): ").strip() or "DXB-001"
        basic = float(input("Enter Monthly Basic Salary (AED): "))
        housing = float(input("Enter Monthly Housing Allowance (AED): "))
        transport = float(input("Enter Monthly Transport Allowance (AED): "))
        overtime_hours = float(input("Enter Overtime Hours this month (0 if none): "))
        years = float(input("Enter Total Years of Service (e.g., 3.5): "))

        if basic <= 0 or years < 0:
            print("Basic salary must be greater than 0 and years cannot be negative.")
            return

        overtime_pay, total_salary = calculate_monthly_salary(basic, housing, transport, overtime_hours)
        gratuity = calculate_uae_gratuity(basic, years)

        save_payslip(emp_name, emp_id, basic, housing, transport, overtime_pay, total_salary, years, gratuity)

    except ValueError:
        print("Invalid input. Please enter valid numbers for salary, hours, and years.")


if __name__ == "__main__":
    main()
