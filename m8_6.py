import matplotlib.pyplot as plt

# marks = [45,48,52,55,57,61,63,65,67,68,71,72,74,76,78,81,83,85,88,92]
salary = [20,22,24,25,27,28,30,32,35,200]

plt.boxplot(salary)
plt.ylabel("Marks")
plt.title("Mark distrbution")
plt.show()