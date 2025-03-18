from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from collections import defaultdict

driver = webdriver.Chrome()  
driver.get('https://tournament.fantasysports.yahoo.com/mens-basketball-bracket/pickdistribution') 
# Yahoo probabilities page

allData = defaultdict(list) 
# This will hold all data as we scrape each page

playIn = set(["ALST/SFPA","AMER/MSM","SDSU/UNC","TEX/XAV"])

def collect():
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[2]/span"))
    ) # Wait for elements to appear

    # Now safely get all elements
    names = driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/span[1]") # team names
    percents = driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]/span[1]") # percentage

    # add percentage to team
    for n,p in zip(names, percents):
        if n.text not in playIn:
            allData[n.text].append(p.text)




collect()
for x in range(2,7):
  driver.find_element(By.XPATH, "//div[@class='Fz(16px) Px(15px) Py(8px)']/button[" + str(x) + "]").click()
  collect()
# Scrape each page systematically


file = open("yahoo-picks-2025.csv", "w", newline='')
writer = csv.writer(file)

writer.writerow(["Team", "Rd64", "Rd32", "Rd16", "Rd8", "Rd4", "Final"]) # header
data = [[n] + p for n, p in allData.items()] 
# we need to filter the names to matching with Kenpom 
rename = {
    # "ALST/SFPA": "Alabama St.",
    # "AMER/MSM": "American",
    "N.C. Wilmington": "UNC Wilmington",
    # "SDSU/UNC": "San Diego St.",
    "SIU Edwardsville": "SIUE",
    "St. Mary's": "Saint Mary's",
    # "TEX/XAV": "Texas"
}
for d in data:
    if d[0] in rename:
        d[0] = rename[d[0]]

data.sort()
writer.writerows(data)


