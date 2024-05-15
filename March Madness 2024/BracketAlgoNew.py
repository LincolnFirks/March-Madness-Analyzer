import csv
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
  for x in range(4):
    top.append("")



writer.writerow(top)

Header = [""]
section = ["KenPom %", "Peoples %","Adv","Adv+", "Adv+WP"]
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
      AdvList = []
      RunningAdvP = []
      for x in range(2, 8):
        currentTeam.append(KPlines[x])
        currentTeam.append(YahooLines[x-1])
        adv = round((float(KPlines[x]) - float(YahooLines[x-1])), 2)
        currentTeam.append(adv)
        if adv < 0:
          advP = round(((100 - float(KPlines[x])) * (float(KPlines[x]) - float(YahooLines[x-1]))), 2)
        else:
          advP = round((float(KPlines[x]) * (float(KPlines[x]) - float(YahooLines[x-1]))), 2)
        currentTeam.append(advP)
        AdvList.append(advP * (x-1))
        # AdvList.append(advP * (2**(x-2)))
        currentTeam.append(round(sum(AdvList), 2))
      
      writer.writerow(currentTeam)
      break


