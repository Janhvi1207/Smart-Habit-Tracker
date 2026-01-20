import pandas as pd

# Load the habit dataset
df = pd.read_csv("data/habits.csv")

# Convert Completed column to boolean
df["Completed"] = df["Completed"].map({"Yes": True, "No": False})

# Calculate habit completion rate
completion_rate = df.groupby("Habit")["Completed"].mean() * 100

# Calculate average time spent per habit
average_time = df.groupby("Habit")["TimeSpentMinutes"].mean()

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
