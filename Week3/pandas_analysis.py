import pandas as pd

# Sample dataset
data = {
    "Name": ["Rahul", "Priya", None, "Kiran"],
    "Marks": [85, 90, None, 78]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Dataset")
print(df)

# Calculate average marks
average_marks = df["Marks"].mean()

print("\nAverage Marks:", average_marks)