import matplotlib.pyplot as plt

x = int(input('Give amount: '))

# fibonacci random number generator
def fib(n):
    a, b = 55, 24
    k = int(input("Enter k value: "))
    for _ in range(n):
        yield a
        a, b = b, (a - k + b - k) + 1


print(list(fib(x)))
arr1 = []
arr2 = []
count = 0

for i in fib(x):
    if count % 2 == 1:
        arr1.append(i)
    else:
        arr2.append(i)
    count += 1

plt.plot(arr1, arr2, marker='D', linestyle='None')
plt.title("Distribution on Plane")
plt.show()