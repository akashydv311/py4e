# PYTHON PRECIDANCE ORDER FOR SOLVING THE EXPRESSION

'''
Peranthesses
Exponentiation
Multiplication
Addition
Comparison
Logical NOT
Logical AND
Logical OR
Equality check (same level as >)



** (Exponentiation)
*, /, //, % (Multiplication, Division)
+, - (Addition, Subtraction)
Comparison (>, ==, etc.)
not and or

'''

result = 3 + 4 * 2 ** 2 - 1 > 20 and not False or 5 == 5
print(result)



# PYTHON DIVISION 

ans1 = 2 / 2
print("Division Result = ", type(ans1), ans1)

ans2 = 2 // 2
print("Floor Division = ", type(ans2), ans2)

# INPUT FUNCTION RETURN STRING

#Example 1

ans = '1' + '1'
print(ans)

#ans = 1 + '1'
#print(ans)

userinput = input("Enter any number: ")
ans = int(userinput) + 10
print("Added 10 in input: ", ans)




