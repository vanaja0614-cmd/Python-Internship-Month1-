import pandas as pd
import matplotlib.pyplot as plt

students = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Kiran"],
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(students)

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("chart.png")
plt.show()