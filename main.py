 # 1. This function should return the sum from 1 to num
def SumOfNumbers(num):
  sum = 0
  x = range(1, num)
  for n in x:
    sum += n

  return sum + num

print("SumOfNumbersOutput")
s = SumOfNumbers(3)
print(s) # should return 6
s = SumOfNumbers(9)
print(s) # should return 45

# 2. This function should return true if a number is even and false if a number is odd

  # your code
def IsEven(num):
    if num % 2 == 0:
      return True
    else:
      return False

print("")
print("Simple Even or Odd Output")
print(IsEven(2))   # should return True
print(IsEven(3))  # should return False

# 3. This function should print out each number from 1 to num and beside it state if it is even or odd. It should use your previous IsEven function.
def EvenOrOddForLoop(num):

  # your code

  
    x=range(1,num + 1)
    for n in x:
        if IsEven(n):
            print(n, "Even")
        else:
            print(n, "Odd")


print("")
print("Even or Odd Output For Loop")
EvenOrOddForLoop(9)
# 4. Same as the previous but implement with a while loop
def EvenOrOddWhileLoop(num):

  # your code

  return

print("")
print("Even or Odd Output While Loop")
EvenOrOddWhileLoop(12)

# 5. This function should take list of numbers and return the largest in the list. You are not allowed to use internal functions for maximum of lists. Only comparators >, < etc.
def Biggest(numbers):

  # your code
  outloop = 0

  for n in numbers:
    if n > outloop:
        outloop = n

    

  print(outloop)
  return 

print("")
print("Biggest Output")
print(Biggest([3,5,-2,8,1])) # should return 8

# . This function should ask a user for a 2 digit alpha-numeric password (eg. "e8" or "kA"). It should then, try to figure out how what that password is by creating other passwords and checking them. Your return should be how many passwords you had to check to find the user input password. This is essentially what is done in a Brute Force attack.
def PasswordCrack():

  return 

print("")
print("Password Crack")
print("It took {} attempts".format(PasswordCrack()))
