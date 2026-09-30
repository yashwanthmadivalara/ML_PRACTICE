import matplotlib.pyplot as plt

students = [40, 30, 20,10]
dept = ["cse","ece","ise","me"]
plt.pie(students, labels = dept)
plt.title("students by dept")
plt.show()