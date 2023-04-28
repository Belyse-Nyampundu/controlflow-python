# Write a function that uses while, if and continue 
# statements to print all the even numbers between 0 and 50

def all_numbers():
    x = 0
    while x < 50:
        x += 1
        if x % 2 != 0:
            continue
        print(x)

all_numbers()

# Write a function that takes an integer argument 
# and prints "Prime" if the number is prime,
#  and "Not prime" if the number is not prime.

def integer_number(num):
   
    if num % num and 1 ==0:
        print(f"{num}is prime")
    else:
        print(f"{num}is not a prime")
integer_number(3)

# Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.

def integers_number(num):
    
    sum = 0
    for i in num:
        if i % 2 ==0:
            sum += i
            print(sum)
integers_number([1,2,3,4,5,6,7,8,12])

# Write a function that takes any two integers as input, 
# and prints the sum of all the numbers 
# between the two integers (inclusive) that are divisible by 3.
def divisible_by_three(num1,num2):
    sum2 = 0
    for x in range(num1,num2):
        if x % 3 == 0:
            sum2 += x
            print(sum2)
divisible_by_three(1,10)


    

