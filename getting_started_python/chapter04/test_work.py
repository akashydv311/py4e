
def print_msg():
    print("hello world")

def itration(num):
    i=0
    while i is not num:
        print_msg()
        i+=1

def test_return(word):
    for i in word:
        if i == 'o':
            return i

def return_st():
    for i in range(10):
        pass
    return
    print("byy")

# main
#num = input("How maney time's do you want to print:")
#itration(int(num))

#char = test_return('python')
#print(char)

ans = return_st()
print(ans)



