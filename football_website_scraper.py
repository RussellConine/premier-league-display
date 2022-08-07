import re
from numpy import zeros
import requests
import matplotlib.pyplot as plt

# define website, leagues
#https://www.worldfootball.net/history/eng-premier-league/

first_year = 1888
last_year = 2021
base_url = "https://www.worldfootball.net/schedule/eng-premier-league-"

def create_years(first_year,last_year):
    years = []
    for year in range(first_year, last_year):
        year_string = str(year) + "-" + str(year+1)
        years.append(year_string)
    return years


def scrape_year(year_string):
    
    URL = base_url + year_string
    page = requests.get(URL).text
    split_pattern_1 = 'Pt\.'
    split_pattern_2 = "</table>"
    found = re.split(split_pattern_1, page)[1]
    found = re.split(split_pattern_2, found)[0]
    pattern = 'a href.+title="[^"]+"'
    teams = list()
    
    teams_string = re.findall(pattern, found)
    for long_string in teams_string:
        untrimmed_team = re.split("title", long_string)
        team = re.sub('[^A-Za-z0-9 ]+', '', untrimmed_team[1])
        teams.append(team)

    return(teams)   
    

def plot_year(results):
    for count,season in enumerate(results):
        ys = list(range(len(season),0,-1))
        xs = count+1+zeros(len(season))
        place = 0
        for x,y in zip(xs,ys):
            label = season[place]
            plt.annotate(label, # this is the text
                (x,y), # these are the coordinates to position the label
                textcoords="offset points", # how to position the text
                xytext=(0,10), # distance from text to points (x,y)
                ha='right') # horizontal alignment can be left, right or center
            place+=1
            plt.scatter(x,y)
    plt.show()


def main():
    first_year = 1888
    last_year = 1890
    years = create_years(first_year, last_year)
    results = []
    for season in years:
        results.append(scrape_year(season))
    plot_year(results)
    # plot_year(results)



if __name__ == "__main__":
    main()
