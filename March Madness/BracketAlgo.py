import csv
import pandas as pd
import math

OptimalFile = open("OptimalValues.csv", "w", newline='')
writer = csv.writer(OptimalFile)


KPFile = open("kenpom-forecast-2024.csv", "r")
KPReader = csv.reader(KPFile)

YahooFile = open("yahoo-picks-2024.csv", "r")
YahooReader = csv.reader(YahooFile)

rounds = ["Rd64", "Rd32", "Swt16", "Elite8", "Final4", "Champ"]
top = ["Team"]

for item in rounds:
  top.append(item)
  for x in range(3):
    top.append("")


writer.writerow(top)

Header = [""]
section = ["KenPom %", "Peoples %","Adv","Adv+"]
for x in range(6):
  Header += section

writer.writerow(Header)


for KPlines in KPReader:
  YahooFile.seek(0)
  if KPlines[0] == "Seed": 
    continue
  for YahooLines in YahooReader:
    if KPlines[1] == YahooLines[0]:
      currentTeam = [KPlines[1]]
      for x in range(2, 8):
        currentTeam.append(KPlines[x])
        currentTeam.append(YahooLines[x-1])
        currentTeam.append(round((float(KPlines[x]) - float(YahooLines[x-1])), 2))
        currentTeam.append(round((float(KPlines[x]) * (float(KPlines[x]) - float(YahooLines[x-1]))), 2))
      writer.writerow(currentTeam)
      break


