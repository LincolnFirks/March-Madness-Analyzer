import csv
from operator import itemgetter

file = open("download.csv", "r")
reader = csv.reader(file)


def GetStats(row):
  file.seek(0)
  teams = []
  teamsWins = []
  total = 0
  index = 0
  for lines in reader:
    winner = lines[row]
    if index < 2:
      index += 1
      continue
    if winner in teams:
      for team in teamsWins:
        if team[0] == winner:
          team[1] += 1
    else:
      teams.append(winner)
      teamsWins.append([winner, 1])
    total += 1
    index += 1
  
  teamsWins = sorted(teamsWins, key=lambda x: x[1])
  teamsWins.reverse()
  print("Total: " + str(total))
  for team in teamsWins:
    percentage = round((100 * (team[1] / total)), 2)
    print(team[0] + " " + str(team[1])  + " " + str(percentage) + "%")

print("To Win Championship:")
GetStats(63)

regions = ["East", "West", "South", "MidWest"]
for x in range(4):
  print("\n")
  print("To Make Make Final Four: " + regions[x] +  " Region\n")
  GetStats(x + 57)
  



