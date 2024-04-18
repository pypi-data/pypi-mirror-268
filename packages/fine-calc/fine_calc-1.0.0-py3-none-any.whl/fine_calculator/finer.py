from fine_calculator.calculator import calculate_fine

# Test cases
test_cases = [10, 20, 30, 15, 25]

# Iterate over test cases
for days_overdue in test_cases:
    fine_amount = calculate_fine(days_overdue)
    print(f"For {days_overdue} days overdue, the fine amount is: ${fine_amount}")
