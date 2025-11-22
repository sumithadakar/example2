import sys

if len(sys.argv) != 2:
    print("Usage: <SALARY>")
    sys.exit(1)

salary = float(sys.argv[1])

print("Salary:", salary)

bonus = salary * 0.10

total_salary = salary + bonus

print("Bonus Amount:", bonus)
print("Total Salary After Adding Bonus:", total_salary)
