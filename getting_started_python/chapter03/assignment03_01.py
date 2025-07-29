#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.


def compute_pay(r, h):
    total_pay=0.0
    
    if h<=40:
        total_pay=h*r
    else:
        normal_pay = 40 * r
        extra_hour = h - 40
        extra_pay_rate = r * 1.5
        e_p = extra_hour*extra_pay_rate
        total_pay = normal_pay + e_p
    
    return total_pay
        


hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate per hour:")
r = float(rph)

pay = compute_pay(r, h)
print(pay)