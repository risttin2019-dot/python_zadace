import pandas as pd
R = '/Volumes/bootcamp/northern_star/raw_2025_26/'
matches = pd.read_parquet(R + 'matches_2025_26.parquet')

# 1. zadatak

both_teams_scored = (matches['home_goals'] > 0) & (matches['away_goals'] > 0)
tight_home_victory = (matches['home_goals'] - matches['away_goals'] == 1)
zero_zero = (matches['home_goals'] == 0) & (matches['away_goals'] == 0)
matches['high_total_goals'] = matches['home_goals'] + matches['away_goals']

matches[both_teams_scored]
matches[tight_home_victory]
matches[zero_zero]
matches.sort_values('high_total_goals', ascending=False).head(10)


# 2. zadatak

# 2.1

ravenscar_albion = (matches['home_team'] == 'RVA') | (matches['away_team'] == 'RVA')

rva_matches = matches[ravenscar_albion].copy()

# 2.2

rva_matches['result'] = 'tie'
rva_matches.loc[rva_matches['home_goals'] > rva_matches['away_goals'], 'result'] = 'home win'
rva_matches.loc[rva_matches['home_goals'] < rva_matches['away_goals'], 'result'] = 'away win'

len(rva_matches.loc[(rva_matches['home_team'] == 'RVA') & (rva_matches['result'] == 'home win')
                |
                (rva_matches['away_team'] == 'RVA') & (rva_matches['result'] == 'away win')])

len(rva_matches.loc[(rva_matches['home_team'] == 'RVA') & (rva_matches['result'] == 'away win')
                |
                (rva_matches['away_team'] == 'RVA') & (rva_matches['result'] == 'home win')])

len(rva_matches[rva_matches['result'] == 'tie'])

# 2.3

rva_matches.loc[rva_matches['home_team'] == 'RVA', 'home_goals'].sum()
rva_matches.loc[rva_matches['away_team'] == 'RVA', 'away_goals'].sum()

# 22 gola na domacem terenu
# 11 golova na gostujucem terenu

# 2.4

rva_matches['rva_goals'] = 0
rva_matches.loc[rva_matches['home_team'] == 'RVA', 'rva_goals'] = rva_matches['home_goals']
rva_matches.loc[rva_matches['away_team'] == 'RVA', 'rva_goals'] = rva_matches['away_goals']

rva_matches.sort_values('rva_goals', ascending=False)


# 3. zadatak

# 3.1

matches['stadium'].unique()

# 3.2

matches['stadium'].value_counts()

# 3.3

for stadium in matches['stadium'].unique():
  avg_att = matches.loc[matches['stadium'] == stadium, 'attendance'].mean()
  #print(stadium, round(avg_att, 2))

# 3.4

stadium_avg_att = {}

for stadium in matches['stadium'].unique():
  avg_att = matches.loc[matches['stadium'] == stadium, 'attendance'].mean()
  stadium_avg_att[stadium] = round(float(avg_att), 2)

df_avg = pd.DataFrame(list(stadium_avg_att.items()), columns=['stadium', 'avg_attendance'])

df_avg.sort_values('avg_attendance', ascending=False).head(5)