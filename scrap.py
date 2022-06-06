import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep 

URL = 'https://himalayas.app'
f = open("data.txt", "a")
  
for page in range(1, 102):
    print("Page: " + str(page))
    print("---------------------")
    allCompaniesReq = requests.get(URL + '/companies?page=' + str(page))
    soup = bs(allCompaniesReq.text, 'html.parser')
    
    companyBlock = soup.find("ul", {"id": "card-group"})
    companies = companyBlock.findChildren("div", recursive=False)
    for company in companies:        
        link = company.select_one("a[href*=tech-stack]")
        if link == None:
            continue
        print(URL + link['href'])
        companyPageReq = requests.get(URL + link['href'])
        x = randint(2,5)
        sleep(x)
        soupCompany = bs(companyPageReq.text, 'html.parser')
        stackElements = soupCompany.find_all("label", attrs={"data-category": "Libraries"})
        print("Number of stacks: " + str(len(stackElements)))        
        for stackElement in stackElements:
            print(stackElement.find('p').text)        
            f.write(stackElement.find('p').text + "\n")    