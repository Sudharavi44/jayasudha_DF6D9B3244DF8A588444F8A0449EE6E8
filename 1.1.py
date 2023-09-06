# impliment a recursive function to calculate the factorial of given number
#factorial of 5 = 1 * 2 * 3 * 4 * 5
#farmula = n x (n-1)
def fact_rec(n):
 if n==0 or n==1:
  return 1
 else:
  return n*fact_rec(n-1)
print("calculate the factorial of given number")
print("---------------------------------------\n")

a = int(input("enter number:"))
b = fact_rec(a)

print("The factorial of {} is {}".format(a,b)) #format method