import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

print(indeed_result)

print()
print()

# print(indeed_result.text)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# print(indeed_soup)

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')

span_list = []
for page in pages:
    span_list.append(page.find("span"))

print(span_list[0:-1])
