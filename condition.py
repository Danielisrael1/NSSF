lecturers_name=input("Enter lecturer name: ")
school=input("Enter school/faulty:  ")
hours=float(input("Enter hours worked this month: "))

h_pay=50000



def gross_pay(hours,h_pay):
    
    return hours*h_pay

NSSF=15/100*gross_pay(hours,h_pay)
SACCO=5/100*gross_pay(hours,h_pay)
print(f"NSSF: {NSSF}")
print(f"SACCO: {SACCO}")
def t_tax(NSSF,SACCO):
    return NSSF+SACCO

def net_pay(gross_pay,t_tax):
    return gross_pay-t_tax


print(f"Name: {lecturers_name}")
print(f"School: {school}")
print(f"Hours worked: {hours}")
print("--------PAYROLL SUMMARY----------")

total_pay=gross_pay(hours,h_pay)
print(f"Gross pay:  {total_pay}")


print("Deductions: ")
print(f"  -NSSF: {NSSF}")
print(f"  -SACCO: {SACCO}")
print(f"Total deductions:{t_tax(NSSF,SACCO)}")
print(f"Net pay:{net_pay(gross_pay(hours,h_pay),t_tax(NSSF,SACCO))}")
print("=================================")