import matplotlib.pyplot as plt

x=[1, 2, 3, 4]
y = [20, 30, 15, 25]

plt.bar(x,y)
plt.title("temperature over days")
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()