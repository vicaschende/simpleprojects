 = int(input("Enter an integer value: "))
i = abs(i)
n = 0
# g_r stands for "the golden ratio"
g_r = 1.618034
x = 1 - g_r
# using the golden ratio to calculate the fibonacci sequence;
while n <= i:
     term = (pow(g_r, n) - pow(x, n))/(2.236068)

     term = round(term, 0)

     print(term)

     n += 1

print ("Sequence finished")
