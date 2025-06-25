import csv
import matplotlib.pyplot as plt


import csv

# Read data from a CSV file
data = []
with open('soccer_stats.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Perform data analysis
# Calculate the average goals scored
total_goals = 0
total_players = len(data) - 1  # Subtract 1 to exclude the header row

for row in data[1:]:
    total_goals += int(row[3])  # Assuming goals scored data is in the fourth column

average_goals = total_goals / total_players

# Display the average goals scored
print("Average Goals Scored: ", average_goals)

# Create a bar chart for goals scored
player_names = [row[0] for row in data[1:]]  # Assuming player names are in the first column
goals_scored = [int(row[3]) for row in data[1:]]  # Assuming goals scored data is in the fourth column

plt.bar(player_names, goals_scored)
plt.xlabel('Player')
plt.ylabel('Goals Scored')
plt.title('Goals Scored by Players')
plt.xticks(rotation=90)
plt.show()

# Create a scatter plot for goals scored vs assists
assists = [int(row[4]) for row in data[1:]]  # Assuming assists data is in the fifth column

plt.scatter(goals_scored, assists)
plt.xlabel('Goals Scored')
plt.ylabel('Assists')
plt.title('Goals Scored vs Assists')
plt.show()

# Create a table for all players
print("{:<20} {:<10} {:<10} {:<10}".format("Player", "Goals", "Assists", "Yellow Cards"))
print("-----------------------------------------------------------")
for row in data[1:]:
    print("{:<20} {:<10} {:<10} {:<10}".format(row[0], row[3], row[4], row[5]))  # Assuming player names, goals, assists, and yellow cards are in the first, fourth, fifth, and sixth columns respectively

# Sort players by goals scored and display top 10 goal scorers
sorted_goals = sorted(data[1:], key=lambda x: int(x[3]), reverse=True)
top_10_goals = sorted_goals[:10]

print("\nTop 10 Goal Scorers")
print("{:<20} {:<10}".format("Player", "Goals"))
print("----------------------------")
for row in top_10_goals:
    print("{:<20} {:<10}".format(row[0], row[3]))  # Assuming player names and goals scored are in the first and fourth columns respectively

# Sort players by assists and display top 10 assisters
sorted_assists = sorted(data[1:], key=lambda x: int(x[4]), reverse=True)
top_10_assists = sorted_assists[:10]

print("\nTop 10 Assisters")
print("{:<20} {:<10}".format("Player", "Assists"))
print("----------------------------")
for row in top_10_assists:
    print("{:<20} {:<10}".format(row[0], row[4]))  # Assuming player names and assists are in the first and fifth columns respectively

# Create scatter plots for goals scored and assists
top_goals_players = [row[0] for row in top_10_goals]
top_goals = [int(row[3]) for row in top_10_goals]

top_assists_players = [row[0] for row in top_10_assists]
top_assists = [int(row[4]) for row in top_10_assists]

plt.scatter(top_goals_players, top_goals, label='Top 10 Goal Scorers')
plt.scatter(top_assists_players, top_assists, label='Top 10 Assisters')

plt.xlabel('Player')
plt.ylabel('Count')
plt.title('Goals Scored vs Assists (Top 10 Players)')
plt.xticks(rotation=90)
plt.legend()
plt.show()
