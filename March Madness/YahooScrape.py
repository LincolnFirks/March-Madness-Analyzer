from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import itertools

driver = webdriver.Chrome()  
driver.get('https://tournament.fantasysports.yahoo.com/mens-basketball-bracket/pickdistribution') 
# Kenpom probabilities page

teamdata = []


for x in range(1,65):
    data = driver.find_element(By.XPATH, "//table/tbody/tr[" + str(x) + "]/td[2]/span").text
    teamdata.append(data)
#Add team names

def scrapePercents():
  for x in range(1,65):
    data = driver.find_element(By.XPATH, "//table/tbody/tr[" + str(x) + "]/td[3]/span").text
    teamdata.append(data)

scrapePercents()
for x in range(2,7):
  driver.find_element(By.XPATH, "//div[@class='Fz(16px) Px(15px) Py(8px)']/button[" + str(x) + "]").click()
  scrapePercents()



file = open("yahoo-picks-2024.csv", "w", newline='')
writer = csv.writer(file)

writer.writerow(["Team", "Rd64", "Rd32", "Rd16", "Rd8", "Rd4", "Final"])

block = 64

TeamsToRename = ["N. Carolina", "SDSU", "St. Mary's", "McNeese", "W. Kentucky", "St. Peter's"]
RenameTo = ["North Carolina", "San Diego St.", "Saint Mary's", "McNeese St.", "Western Kentucky", "Saint Peter's"]

index = 0
RenameIndex = 0
for item in teamdata:
  if item in TeamsToRename:
    teamdata[index] = RenameTo[TeamsToRename.index(item)]
  index+=1



for x in range(block):
  currentTeam = []
  for y in range(7):
    currentTeam.append(teamdata[x+(block*y)])
  writer.writerow(currentTeam)


