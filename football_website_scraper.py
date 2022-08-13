import re
from numpy import zeros
import requests
import matplotlib.pyplot as plt
import pandas as pd

# define website, leagues
#https://www.worldfootball.net/history/eng-premier-league/

first_year = 1888
last_year = 2021
base_url = "https://www.worldfootball.net/schedule/eng-premier-league-"

def CreateYears(first_year,last_year):
    years = []
    for year in range(first_year, last_year):
        year_string = str(year) + "-" + str(year+1)
        years.append(year_string)
    return years


def ScrapeYear(year_string):
    
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
    

def PlotYear(results):
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

def ConvertToDataFrame(results, years):
    results_dict = {}
    for season in results.values(): # build dictionary w/ team as key, empty list as value
        for team in season:         # will fill empty values with list of results in next loop
            if team not in results_dict.keys():
                results_dict[team] = []
    for season in results.values():
        for team in results_dict:
            if team in season:
                results_dict[team].append(season.index(team) + 1)    # if team has result in this season, record place
            else:                                                    # place is team's season index + 1
                results_dict[team].append(0)    # if team wasn't in that season, record place as zero
    df = pd.DataFrame(data = results_dict)
    df.index = years # name index with years
    print(df)

def main():
    first_year = 1888
    last_year = 1893
    years = CreateYears(first_year, last_year)
    print(years)
    results = {}
    max_len = 0
    for season in years:
        results[season] = ScrapeYear(season)
    # print(results)
    results_df = ConvertToDataFrame(results, years)
    # PlotYear(results)



if __name__ == "__main__":
    main()
