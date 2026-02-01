import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print(data)
import pandas as pd

data = pd.read_csv("students.csv")

print(data)
# Calculate average marks for each student
data["Average"] = data[["Maths", "Science", "English"]].mean(axis=1)

print("\nAverage Marks:")
print(data[["Name", "Average"]])
import pandas as pd

data = pd.read_csv("students.csv")

print(data)

# Calculate average marks for each student
data["Average"] = data[["Maths", "Science", "English"]].mean(axis=1)

print("\nAverage Marks:")
print(data[["Name", "Average"]])
# Find top and lowest performer
top_student = data.loc[data["Average"].idxmax()]
low_student = data.loc[data["Average"].idxmin()]

print("\nTop Performer:")
print(top_student["Name"], "-", top_student["Average"])

print("\nLowest Performer:")
print(low_student["Name"], "-", low_student["Average"])

# Plot average marks
plt.bar(data["Name"], data["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")
plt.show()
