
import sys

def fizzBuzz(n):
    for i in range(1, n+1):  # This will loop from 1 to 5 (6 is not included)
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print ("FIzz")
        elif i % 3 != 0 and i % 5 == 0:
            print ("Buzz")
        else:
            print (i)

def main():
   
   user_input = input("Enter a number: ")
   num = int(user_input)
   fizzBuzz(num)

if __name__ == '__main__':
    sys.exit(main())
