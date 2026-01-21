import pandas as pd

# Load the habit dataset
df = pd.read_csv("data/habits.csv")

# Convert Completed column to boolean
df["Completed"] = df["Completed"].map({"Yes": True, "No": False})

# Calculate habit completion rate
completion_rate = df.groupby("Habit")["Completed"].mean() * 100

# Calculate average time spent per habit
average_time = df.groupby("Habit")["TimeSpentMinutes"].mean()
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/habits.csv")

# Convert Completed column to boolean
df["Completed"] = df["Completed"].map({"Yes": True, "No": False})

# Calculate completion rate per habit
completion_rate = df.groupby("Habit")["Completed"].mean() * 100

# Calculate average time spent per habit
average_time = df.groupby("Habit")["TimeSpent"].mean()

# --------- Visualization 1: Completion Rate ---------
plt.figure()
completion_rate.plot(kind="bar")
plt.title("Habit Completion Rate (%)")
plt.xlabel("Habit")
plt.ylabel("Completion Rate")
plt.tight_layout()
plt.show()

# --------- Visualization 2: Average Time Spent ---------
plt.figure()
average_time.plot(kind="bar")
plt.title("Average Time Spent Per Habit (minutes)")
plt.xlabel("Habit")
plt.ylabel("Minutes")
plt.tight_layout()
plt.show()

# Save insights to text file
with open("insights.txt", "w") as f:
    f.write("Habit Completion Rate (%)\n")
    f.write(completion_rate.to_string())
    f.write("\n\nAverage Time Spent Per Habit (minutes)\n")
    f.write(average_time.to_string())

print("Analysis completed successfully!")

print("Habit Completion Rate (%):")
print(completion_rate)

print("\nAverage Time Spent (minutes):")
print(average_time)

# Save insights to a text file
with open("insights.txt", "w") as f:
    f.write("Habit Completion Rate (%)\n")
    f.write(completion_rate.to_string())
    f.write("\n\nAverage Time Spent (minutes)\n")
    f.write(average_time.to_string())
