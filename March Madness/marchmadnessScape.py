"""
The purpose of this program is to scrape kenpom for probabilities and
write them to a csv file in proper format. Should be reusable every year
with slight tweaks (if kenpom changes format).
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()  
driver.get('https://kenpom.com/blog/2023-tourney-forecast/') 
# Kenpom probabilities page

data = driver.find_element(By.CLASS_NAME, "entry-content").text
#Find HTML element with data
data = data.split()
# Split data into list


file = open("kenpom-forecast-2024.csv", "w", newline='')
writer = csv.writer(file)
# intialize csv file and writer

roundTitles = data[0:6]
roundTitles.insert(0,"Team")
roundTitles.insert(0,"Seed")
#separate titles of rounds and team, seed titles into own list
data = data[6:]
# remove from titles from data


writer.writerow(roundTitles)
#write titles in csv file


index = 0
lastItem = ' '
cleanData = []

for item in data:
  if item == "Swt16": # Break off after first set of data
    break
  if item[0].isalpha() and lastItem[0].isalpha():
    cleanData[index-1] += (" " + item)
    # if two in a row start with letters (multi word team), combine
    continue 
  cleanData.append(item)
  index += 1
  lastItem = item

print(cleanData)
 
currentTeam = []
index = 0
for item in cleanData:
  if item == "Rd2": #Rd2 left in to be stop indicator
    writer.writerow(currentTeam)
    break
  if (index % 8 == 0) and (index != 0):
    #When done with team, write to a row and reset list
    writer.writerow(currentTeam)
    currentTeam = [item]
    index += 1
  else:
    currentTeam.append(item)
    index += 1

