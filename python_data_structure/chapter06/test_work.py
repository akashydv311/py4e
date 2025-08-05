# string code

# String Example01
s1 = 'python'
s2 = 'machinelearning'
s3 = s1 + s2
#print(s3)

# String Example02
str_input = input('Enter age: ')
# convert the string
try:
    if int(str_input) == 18:
        print('Eligible')
    else:
        print('Not Eligible')
except ValueError as err:
    print("Value Error: ", err)
except Exception as err:
    print("Error Occoured: ", err)
    