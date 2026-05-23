from itertools import groupby

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('deliveries.csv')
# cleaning data deliveries.csv in dataframe of df
# df.dropna(inplace=True)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns.tolist())
print(df.isna().sum())
print(df.head())
df.drop_duplicates(inplace=True)
print(df.shape)

# Question 1 Which team batting first gave the highest target?
targets = df[df['inning'] == 1].groupby(['match_id', 'batting_team'])['total_runs'].sum()
max_target_value = targets.max()
max_target_team = targets.idxmax()[1]
max_match_id = targets.idxmax()[0]
print(f"The team batting first in match_id {max_match_id} that gave the highest target of {max_target_value} is: {max_target_team}")

# Question 2: Which team took the most wickets in the powerplay?
powerplay_wickets = df[df['over'] <=5 ].groupby('bowling_team')['is_wicket'].sum()
max_wickets = powerplay_wickets.max()
max_wickets_team = powerplay_wickets.idxmax() 
print(f"The team that took the most wickets in the powerplay is: {max_wickets_team}")


# Question 3: Which team lost more wickets in the power play?
powerplay_wickets_lost = df[df['over'] <6 ].groupby('batting_team')['is_wicket'].sum()
max_wickets_lost = powerplay_wickets_lost.max() 
max_wickets_lost_team = powerplay_wickets_lost.idxmax()
print(f"The team that lost more wickets in the power play is: {max_wickets_lost_team}")

# Question 4: Which team has set the 200 plus target more times?
targets = df[df['inning'] == 1].groupby(['match_id', 'batting_team'])['total_runs'].sum()
targets_200_plus = targets[targets >= 200]
target_counts = targets_200_plus.groupby(level=1).size()
max_target_counts = target_counts.max()
max_target_team = target_counts.idxmax()
print(f"The team that has set the 200 plus target more times is: {max_target_team} with {max_target_counts} times.")

# Question 5:How many times has z Khan dismissed SC Ganguly ?
dismissals = df[(df['bowler'] == 'Z Khan') & (df['player_dismissed'] == 'SC Ganguly')]
num_dismissals = dismissals.shape[0]
print(f"Z Khan has dismissed SC Ganguly {num_dismissals} times.")

# Question 6:Who is the highest wicket taker for RCB?
rcb_wickets = df[df['bowling_team'] == 'Royal Challengers Bangalore'].groupby('bowler')['is_wicket'].sum()
max_wickets = rcb_wickets.max()
max_wickets_bowler = rcb_wickets.idxmax()
print(f"The highest wicket taker for RCB is: {max_wickets_bowler} with {max_wickets} wickets.")

# Question 7: Which player has taken the most wickets in IPL so far?
wicket=df.groupby('bowler')['is_wicket'].sum()
highest_wicket=wicket.max()
ipl_highest_wicket_bowler=wicket.idxmax()
print(f"The Bowler name is IPL in Highest wicket {ipl_highest_wicket_bowler} with total wicket {highest_wicket}.")

# Question 8: Which team has given the highest Extra run in IPL so far?
Extra=df.groupby('bowling_team')['extra_runs'].sum()
Highest_Extra=Extra.max()
IPL_Highest_Extra_run_Team=Extra.idxmax()
print(f"Now IPL in Highest Extra  Give Run Team is {IPL_Highest_Extra_run_Team} with Extra Run {Highest_Extra}.")

# Suggest me question for chart through solve question matplotlib ya seaborn ?
# Question 9: Which Bowler is taken highest wickets for team ?
wickets_by_bowler_team = df.groupby(['bowling_team', 'bowler'])['is_wicket'].sum().reset_index()
top_bowlers = wickets_by_bowler_team.sort_values('is_wicket', ascending=False).groupby('bowling_team').head(1)
plt.figure(figsize=(10, 5))
plt.bar(top_bowlers['bowling_team'], top_bowlers['is_wicket'], color='skyblue')

# show bowler name on top of the bar
for index, row in top_bowlers.iterrows():
    plt.text(row['bowling_team'], row['is_wicket'], row['bowler'], ha='center', va='bottom', fontsize=5, color='blue') 
plt.xlabel('Bowling Team')
plt.ylabel('Wickets Taken')
plt.title('Highest Wicket Taker for Each Team in IPL')
plt.xticks(rotation=75,fontsize=8,color='Green')
plt.tight_layout()
plt.show()



