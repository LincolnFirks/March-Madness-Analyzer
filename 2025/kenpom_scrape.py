"""
The purpose of this program is to scrape kenpom for probabilities and
write them to a csv file in proper format. Should be reusable every year
with slight tweaks (if kenpom changes format).
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome()  
driver.get('https://kenpom.substack.com/p/2025-ncaa-tournament-probabilities') 
# Kenpom probabilities page

data = driver.find_element(By.TAG_NAME, "code").text
# Find HTML element with data
data = data.split()
# Split data into list

file = open("./scraped_kenpom_2025.csv", "w", newline='')
writer = csv.writer(file)
# intialize csv file and writer

roundTitles = ["Team"]
roundTitles += data[0:6]
#separate titles of rounds and team, seed titles into own list
# remove from titles from data
writer.writerow(roundTitles)
#write titles in csv file


index = 0
lastItem = ' '
cleanData = []

playIn = set(["Alabama St.","Saint Francis","American","Mount St. Mary's","San Diego St.","North Carolina","Texas","Xavier"])

for item in data[6:]:
  if item[0].isalpha() and lastItem[0].isalpha():
    cleanData[index-1] += (" " + item)
    # if two in a row start with letters (multi word team), combine
    continue 
  if item == "<.001":
    item = ".001"
    # clean up data
  cleanData.append(item)
  index += 1
  lastItem = item


 
currentTeam = []
index = 0
finalData = []
for item in cleanData:
  if (index % 8 == 0):
    #When done with team, write to a row and reset list
    if currentTeam and currentTeam[0] not in playIn:
        finalData.append(currentTeam)
    currentTeam = []
    index += 1
  else:
    currentTeam.append(item)
    index += 1
if currentTeam[0] not in playIn:    
    finalData.append(currentTeam)

finalData.sort()
writer.writerows(finalData)