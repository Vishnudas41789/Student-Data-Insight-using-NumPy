
import numpy as np


data = np.genfromtxt('StudentsPerformance.csv', delimiter=',', dtype=str, skip_header=1)


print("📊 Sample Data:\n", data[:3])
print("🧮 Shape of Data:", data.shape)


unique_genders = np.unique(data[:, 0])
print("\n👥 Unique Genders:", unique_genders)


unique_groups = np.unique(data[:, 1])
print("🏫 Unique Groups:", unique_groups)
math_scores = data[:, 5].astype(float)
unique_math_scores = np.unique(math_scores)
print("🧮 Unique Math Scores:", unique_math_scores[:10])  # Show first 10 only


unique_rows = np.unique(data, axis=0)
print("🎓 Total Unique Students:", len(unique_rows))
