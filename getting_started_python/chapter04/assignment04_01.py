
# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function.

def computepay(h, r):
    pay = 0.0
    extra_pay = 0.0
    total_pay = 0.0
    # pay for upto 40 hours | normal
    if h <= 40 and h > 0:
        pay = h * r
    elif h >= 41:
        pay = h * r
        extra_hour_worked = h - 40
        extra_pay_rate = r/2
        extra_pay = extra_hour_worked * extra_pay_rate
    else:
        total_pay = -1
    # total pay
    total_pay = pay + extra_pay
    
    return total_pay

hrs = input("Enter Hours:")
rph = input("Enter Rate Per Hours:")

hrs = float(hrs)
rph = float(rph)

gross_pay = computepay(hrs, rph)

print("Pay", gross_pay)

