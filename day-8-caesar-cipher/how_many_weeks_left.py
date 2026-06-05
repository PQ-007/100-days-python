age = input("What is your current age? ")
age_as_int = int(age)
years_left = 90 - age_as_int
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")