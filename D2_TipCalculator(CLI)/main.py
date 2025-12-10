print("Welcome to the Tip Calculator!")
def input_num_float(print_str):
    while True:
        try:
            num = float(input(print_str))
            if print_str.isdigit():
                return num
        except ValueError:
            print("Please enter a number")


bill = float(input_num_float("What was the total bill? "))
tip = float(input_num_float("What was the tip amount? "))
num_people = int(input_num_float("How many people to split the bill? "))

# Calculation
tip_amount = bill * (tip / 100)
total_bill= bill + tip_amount
price_per_person = round(total_bill / num_people, 2)

print(f"Each person should pay $ {price_per_person}" )
