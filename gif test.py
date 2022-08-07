# gif test
import os
import numpy as np
import matplotlib.pyplot as plt
import imageio

teams = ['Preston North End', 'Aston Villa']
teams2 = ['Wolverhampton Wanderers', 'Blackburn Rovers']

season_list = [teams, teams2]
teams_count = len(teams)


filenames = []
for i,season in season_list:
    for teams in season:
        y = list(range(len(season),0,-1))
        x = i+1
        plt.scatter(y)

for i in y:
    # plot the line chart
    plt.plot(y[:i])
    plt.ylim(20,50)
    
    # create file name and append it to a list
    filename = f'{i}.png'
    filenames.append(filename)
    
    # save frame
    plt.savefig(filename)
    plt.close()
# build gif
with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        
# Remove files
for filename in set(filenames):
    os.remove(filename)