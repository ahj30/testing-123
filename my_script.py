# testing-123/my_script.py

def enlarge(i):
    return i * 100

 #n eed to remove from global scope in order to import order things from this script
#my_number = float(input("Please input a number"))
#n = enlarge(8)
#n = enlarge(my_number)
#print(n)

if __name__ == "__main__":
    # only run this if from the command line
    my_number = float(input("Please input a number"))
    n = enlarge(8)
    n = enlarge(my_number)
    print(n)
    