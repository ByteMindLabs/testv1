# add function here
def add(a, b):
    return a + b    

#add function for multiplication
def multiply(a, b):
    return a * b    

# add main function to test the add function
if __name__ == "__main__":
    print(add(2, 3))  # should print 5
    print(add(-1, 1))  # should print 0
    print(add(0, 0))  # should print 0
    print(multiply(2, 3))  # should print 6
    print(multiply(-1, 1))  # should print -1
    print(multiply(0, 0))  # should print 0
