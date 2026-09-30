import matplotlib.pyplot as plt

marks = [65, 65, 90, 65, 60, 55]

plt.hist(marks)
plt.title("marks of student")
plt.xlabel("marks")
plt.ylabel("no. of students")
plt.show()