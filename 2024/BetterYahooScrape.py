from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import itertools
import time
driver = webdriver.Chrome()  
driver.get('https://tournament.fantasysports.yahoo.com/mens-basketball-bracket/pickdistribution') 
# Kenpom probabilities page

teamdata = []


for x in range(1,69):
    data = driver.find_element(By.XPATH, "//table/tbody/tr[" + str(x) + "]/td[2]/span").text
    team = [data]
    teamdata.append(team)
    data = driver.find_element(By.XPATH, "//table/tbody/tr[" + str(x) + "]/td[3]/span").text
    teamdata[x-1].append(data)

# Get team name and first percentage
teamdata.sort()


def scrapePercents():
  newdata = []
  for x in range(1,69):
    data = driver.find_element(By.XPATH, "//table/tbody/tr[" + str(x) + "]/td[2]/span").text
    team = [data]
    newdata.append(team)
    data = driver.find_element(By.XPATH, "//table/tbody/tr[" + str(x) + "]/td[3]/span").text
    newdata[x-1].append(data)
    #Loop through every team and add team name and percent
  newdata.sort()
  for team, newteam in zip(teamdata, newdata):
    team.append(newteam[1])

    
for x in range(2,7):
  driver.find_element(By.XPATH, "//div[@class='Fz(16px) Px(15px) Py(8px)']/button[" + str(x) + "]").click()
  scrapePercents()
#Scrape each page automatically

TeamsToRename = ['McNeese', 'N. Carolina', 'S. Dakota St.', 'SDSU', "St. Mary's", "St. Peter's", 'W. Kentucky']
RenameTo = ["McNeese St.", "North Carolina", "South Dakota St.", "San Diego St.", "Saint Mary's", "Saint Peter's",  "Western Kentucky"]
renameIndex = 0

for team in teamdata:
  if team[0] in TeamsToRename:
    team[0] = RenameTo[renameIndex]
    renameIndex += 1



file = open("yahoo-picks-2024.csv", "w", newline='')
writer = csv.writer(file)

writer.writerow(["Team", "Rd64", "Rd32", "Rd16", "Rd8", "Rd4", "Final"])
writer.writerows(teamdata)


