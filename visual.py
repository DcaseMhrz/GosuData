# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import getdata as gd
 
team1=gd.finalteamnames[0]
team2=gd.finalteamnames[1]

worldrank2=(float(gd.finalteamdata[1])/(float(gd.finalteamdata[5])+float(gd.finalteamdata[1]))*100)
worldrank1=(float(gd.finalteamdata[5])/(float(gd.finalteamdata[5])+float(gd.finalteamdata[1]))*100)

rating1=(float(gd.finalteamdata[0])/(float(gd.finalteamdata[0])+float(gd.finalteamdata[4]))*100)
rating2=(float(gd.finalteamdata[4])/(float(gd.finalteamdata[0])+float(gd.finalteamdata[4]))*100)

teamearnings1=gd.finalteamdata[2]
teamearnings2=gd.finalteamdata[6]
teamearnings1=teamearnings1.replace("$","")
teamearnings2=teamearnings2.replace("$","")

earnings1=(float(teamearnings1)/(float(teamearnings2)+float(teamearnings1))*100)
earnings2=(float(teamearnings2)/(float(teamearnings2)+float(teamearnings1))*100)

winrate1=gd.finalteamdata[3]
winrate2=gd.finalteamdata[7]

winrate1=winrate1.replace("%","")
winrate2=winrate2.replace("%","")


winrate1=(float(winrate1)/(float(winrate1)+float(winrate2))*100)


winrate2=(float(winrate2)/(float(winrate1)+float(winrate2))*100)

averageEarnings1=(gd.sum1/(gd.sum1+gd.sum2)*100)
averageEarnings2=(gd.sum2/(gd.sum1+gd.sum2)*100)

print(worldrank1,worldrank2,rating1,rating2,winrate1,winrate2,earnings1,earnings2,gd.sum1,gd.sum2)
# Set data
df = pd.DataFrame({
'group': ['A','B'],
'WorldRank': [worldrank1, worldrank2],
'Rating': [rating1, rating2],
'Earnings': [earnings1, earnings2],
'Winrate': [winrate1, winrate2],
'Average Earnings': [averageEarnings1, averageEarnings2]
})
 
 
 
# ------- PART 1: Create background
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([20,50,70], ["10","20","30"], color="grey", size=7)
plt.ylim(0,100)
 
 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label=gd.finalteamnames[0])
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label=gd.finalteamnames[1])
ax.fill(angles, values, 'r', alpha=0.1)


# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title(team1+" VS "+team2)
plt.show()