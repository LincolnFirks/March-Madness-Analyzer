import csv
import math

OptimalFile = open("MM_stats_2025.csv", "w", newline='')
writer = csv.writer(OptimalFile)
# output file


KPFile = open("scraped_kenpom_2025.csv", "r")
kp = list(csv.reader(KPFile))
# scraped kenpom

YahooFile = open("yahoo-picks-2025.csv", "r")
yahoo = list(csv.reader(YahooFile))
# scraped yahoo


rounds = ["Rd64", "Rd32", "Swt16", "Elite8", "Final4", "Champ"]
top = ["Team"]

for item in rounds:
  top.append(item)
  for x in range(4):
    top.append("")

writer.writerow(top)

header = [""] + ["KenPom %", "Peoples %","Adv","Adv+", "Adv+WP"] * 6
writer.writerow(header)

# Sample row for both: [Akron, 10.2, 2.4, 0.1, 0.01,0.001, 0.001]
for k,y in zip(kp[1:],yahoo[1:]):
    row = [k[0]] # team name
    wp = 0 # Weighted path for Adv+WP
    # This is sum of all Adv+ up up until and including this round
    for i in range(1,7): # all rounds
        row.append(k[i]) # KP%
        row.append(y[i]) # P%
        k_val, y_val = float(k[i]), float(y[i])
        adv = k_val - y_val
        row.append(round(adv,2)) #Adv
        row.append(round(adv * k_val,2)) #Adv+
        # adv weighted by win probability
        wp += adv * i
        row.append(round(wp,2))

    writer.writerow(row)
    






