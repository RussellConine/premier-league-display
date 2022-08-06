import re
import requests

# define website, leagues
#https://www.worldfootball.net/history/eng-premier-league/

first_year = 1888
last_year = 2021
base_url = "https://www.worldfootball.net/schedule/eng-premier-league-"

def create_years():
    years = []
    for year in range(first_year, last_year):
        year_string = str(year) + "-" + str(year+1)
        years.append(year_string)
    return years


def scrape_year(year_string):
    URL = base_url + year_string
    page = requests.get(URL).text
    pattern = 'preston-north-end'
    found = re.search(page, pattern)
    return page


def main():
    year_string1 = '1888-1889'
    years = create_years()
    page = scrape_year(year_string1)



if __name__ == "__main__":
    main()
