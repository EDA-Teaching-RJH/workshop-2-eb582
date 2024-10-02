import math  

def main():
    A = int(input("what's the length of A? "))
    B = int(input("what's the length of B? "))
    C = pythag(A,B)
    print("The Length of C is = " , C)

def pythag(A,B):
    return math.sqrt(A ** 2 + B ** 2)
    
main()