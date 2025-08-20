
# open a file [ we can ]

"""
try:
    fhandle = open("myfile.txt")
except Exception as err:
    print("Error while reading the file: ", err)
    
print(fhandle)
file_data = fhandle.read()

#print(len(fhandle))
for character in fhandle.read():
    print(character)

print(len(file_data))

print(file_data[:10])

"""

# ------------------------------------------


'''
try:
    fy = open('myfile.txt')
    print(fy)
    
    for sen in fy:
        print(sen)

except Exception as err:
    print("Error: ", err)
        

'''

#text = '    Hi my name is akash yadav    '
#clean_text = text.strip()
#print(clean_text)

#
#try:
#    fy = open('myfile.txt')
#    
#    for line in fy:
#        line = line.rstrip()
#        print(line)
#
#except Exception as err:
#    print("Error: ", err)
#        



lines = [
    "Item: Laptop Price: 55000",
    "Item: Phone Price: 30000",
    "Item: Tablet Price: 25000"
]

for line in lines:
    parts = line.split("Price:")
    if len(parts) > 1:
        price = parts[1].strip()
        print(price)
    print(parts)










