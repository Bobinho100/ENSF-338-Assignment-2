import timeit
import matplotlib.pyplot as plt



def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)




n_values = range(35)
time_taken = []


for i in n_values:
    timeTaken = timeit.timeit(lambda : func(i),number=1)
    time_taken.append(timeTaken)


plt.plot(n_values, time_taken)
plt.xlabel('n')
plt.ylabel('Time taken (seconds)')
plt.title('Time taken to compute the n-th Fibonacci number')


plt.show()