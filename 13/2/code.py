import time
from functools import reduce
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

busid = lines[1].split(",")

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

for i in range(0, len(busid)):
    busid[i] = [busid[i], -i]
i = 0
while i < len(busid):
    if busid[i][0] == "x":
        busid.pop(i)
        i -= 1
    else:
        busid[i][0] = int(busid[i][0])
    i += 1
n = [0]*len(busid)
a = [0]*len(busid)
for i in range(0, len(busid)):
    n[i] = busid[i][0]
    a[i] = busid[i][1]

print(chinese_remainder(n, a))
print("--- %s seconds ---" % (time.time() - start_time))

