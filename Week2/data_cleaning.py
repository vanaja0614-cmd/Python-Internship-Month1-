# Week 2 - Data Cleaning Project

# Original data with duplicate values
data = [10, 20, 20, 30, 40, 40, 50]

print("Original Data:", data)

# Remove duplicates
unique_data = list(set(data))
print("Data after removing duplicates:", unique_data)

# Filter values greater than 25
filtered_data = [x for x in unique_data if x > 25]
print("Filtered Data (>25):", filtered_data)