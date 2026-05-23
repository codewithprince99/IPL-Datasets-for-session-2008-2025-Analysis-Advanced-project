import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df=pd.read_csv('matches.csv')

# Data Cleaning process... 
# print(df.columns.tolist())
df.columns=df.columns.str.strip().str.lower().str.replace(' ','_')
# print(df['city'].isna().sum())
df['city']=df['city'].fillna('Unknown',inplace=False)# throw error because of inplace=True 
df['target_runs']=df['target_runs'].fillna(0).astype(int)
df['result_margin']=df['result_margin'].fillna(0).astype(int)
# print(df.info())
# print(df.head())
df.drop_duplicates(inplace=True)

# Quesrion 1:Which team has won by the highest run margin in IPL so far?
max_run_margin=df['result_margin'].max()
Team=df[df['result_margin']==max_run_margin]['winner'].values[0] # why use this line value[0] 
print(f"IPL in History of Highest Run_Margin Winner Team {Team} with Run_Margin {max_run_margin}.")

# Question 2:Who is the most Player of the Match for Royal Challengers Bangalore?
rcb_pom=df[df['winner']=='Royal Challengers Bangalore']['player_of_match']
most_pom=rcb_pom.value_counts().idxmax() # why use this line value_counts and idxmax bea
print(f"Most Player of the Match for Royal Challengers Bangalore is {most_pom}.")

# Question 3:Which team has won the most matches in RCB vs KKR?
rcb_kkr=df[(df['team1']=='Royal Challengers Bangalore') & (df['team2']=='Kolkata Knight Riders') | (df['team1']=='Kolkata Knight Riders') & (df['team2']=='Royal Challengers Bangalore')].groupby('winner').size()
most_wins=rcb_kkr.idxmax()
print(f"Most wins in RCB vs KKR is {most_wins}.")

# Question 4:Which player has been the most Player of the Match for each team in the IPL?
Each_team_pom=df.groupby('winner')['player_of_match'].agg(lambda x: x.value_counts().idxmax())
# sactter plot
plt.figure(figsize=(10,4))
plt.scatter(Each_team_pom.index, Each_team_pom.values)
plt.xticks(rotation=60) 
plt.xlabel('Teams')
plt.ylabel('Most Player of the Match')
plt.title('Most Player of the Match for Each Team in IPL')
# plt.show()

# Question 5:Which city has hosted the most IPL matches?
most_hosted_city=df['city'].value_counts().idxmax() # why use 
venue_name=df[df['city']==most_hosted_city]['venue'].value_counts().idxmax() 
print(f"The city that has hosted the most IPL matches is {most_hosted_city} and the venue is {venue_name}.")

# Question 6: which team has won final match in season 2007/2008 ?
final_match=df[df['season']=='2007/08' ].groupby('match_type').get_group('Final')
final_winner=final_match['winner'].iloc[0] # why use this line iloc[0]
print(f"The team that won the final match in season 2007/2008 is {final_winner}.")

# Question 7: Which umpire has officiated in the most matches so far?
Umpire_matches1=df['umpire1'].value_counts().idxmax()
Umpire_matches2=df['umpire2'].value_counts().idxmax()
print(f"IPL in Most umpire1  officiated name is  {Umpire_matches1}")
print(f"IPL in Most umpire2  officiated name is  {Umpire_matches2}")



#Question 8: Which Team is Highest IPL in Arrive to Final Match  ?

final_matches=df[df['match_type']=='Final']
final_teams=pd.concat([final_matches['team1'], final_matches['team2']])
most_arrivals=final_teams.value_counts().idxmax()
print(f"The team that has arrived the most in the final match is: {most_arrivals}.")

# Question 9: Which team has reached the finals and won the most number of times?
final_matches=df[df['match_type']=='Final']['winner']
most_arrivals=final_matches.value_counts().idxmax()
print(f"The team that has arrived the most in the final match And won  is: {most_arrivals}.")

# Question 10:Which team reaches Qualifier 1 more times?
Qualifier_1=df[df['match_type']=='Qualifier 1']
Qualifier=pd.concat([Qualifier_1['team1'],Qualifier_1['team2']])
Highest_Qualifier_1=Qualifier.value_counts().idxmax()
print(f"Highest IPL in Arrive Qualifier_1 Team name is {Highest_Qualifier_1}.")