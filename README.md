# UAE Employee Salary & Gratuity Calculator

A Python command-line payroll utility built according to *UAE Labor Law* standards. It calculates monthly net salaries (including Basic, Housing, Transport, and 1.25x Overtime) alongside accurate *End-of-Service Gratuity* benefits, generating timestamped employee payslips.

#Key Features
 *UAE Labor Law Gratuity Logic:* Automatically calculates 21 days of basic pay per year for 1–5 years of service, and 30 days per year beyond 5 years (capped at 2 years' basic salary).
 *Monthly Payroll Breakdown:*Computes Basic Salary, Housing Allowance, Transport Allowance, and standard 1.25x hourly overtime pay.
 *Payslip Record Logging:*Saves formatted employee payslips to `employee_payslip_log.txt` for HR recordkeeping.

#Technologies Used
 Python 3 (Functions, Conditional Logic, Math Operations, File Handling, `datetime` module)

#Sample Output
```
==================================================
 UAE EMPLOYEE PAYSLIP & GRATUITY 
Generated Date : 2026-11-18 14:43:26
Employee Name : aysha (ID: DXB-107)
--------------------------------------------------
Basic Salary : 4,000.00 AED
Housing Allowance : 1,500.00 AED
Transport Allowance : 500.00 AED
Overtime Pay (1.25x): 208.33 AED
--------------------------------------------------
TOTAL MONTHLY PAY : 6,208.33 AED
--------------------------------------------------
Service Completed : 3.5 Years
End-of-Service Gratuity (UAE Law): 9,800.00 AED
==================================================
```

#How to Run
1. Download `salary_gratuity_calculator.py`.
2. Open your terminal in the project folder and run:
   ```bash
   python salary_gratuity_calculator.py
   ```

