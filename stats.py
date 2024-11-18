import pandas as pd
import numpy as np
from itertools import combinations

def best_champions_per_team():

    matchhistory_df = pd.read_csv("data/match_history.csv")

    teams = {}
    #for each team, find the champions that that team has played and the win rate for each champion has
    # {team: {champion : [wins, losses, win_rate]}}
    for _, row in matchhistory_df.iterrows():
        winner = row['Winner']
        blue_win = winner == row['Blue'] 
        loser = row['Blue'] if winner != row['Blue'] else row['Red']
        
        if winner not in teams:
            teams[winner] = {}
        if loser not in teams:
            teams[loser] = {}


        blue_picks = row['B_Picks'].strip().split(",")

        for champ in blue_picks:
            if blue_win:
                if champ not in teams[winner]:
                    teams[winner][champ] = [1, 0, 1.0]
                else:
                    wins, losses = teams[winner][champ][0] + 1, teams[winner][champ][1] 
                    teams[winner][champ] = [wins, losses, wins/(wins+losses)]
            else:
                if champ not in teams[loser]:
                    teams[loser][champ] = [0, 1, 0.0]
                else:
                    wins, losses = teams[loser][champ][0], teams[loser][champ][1] + 1
                    teams[loser][champ] = [wins, losses, wins/(wins+losses)]
        
        red_picks = row['R_Picks'].strip().split(",")
        for champ in red_picks:
            if not blue_win:
                if champ not in teams[winner]:
                    teams[winner][champ] = [1, 0, 1.0]
                else:
                    wins, losses = teams[winner][champ][0] + 1, teams[winner][champ][1]
                    teams[winner][champ] = [wins, losses, wins/(wins+losses)]
            else:
                if champ not in teams[loser]:
                    teams[loser][champ] = [0, 1, 0.0]
                else:
                    wins, losses = teams[loser][champ][0], teams[loser][champ][1] + 1
                    teams[loser][champ] = [wins, losses, wins/(wins+losses)]
    
    sorted_teams = {}
    for team, champions in teams.items():
        sorted_champions = dict(sorted(champions.items(), key=lambda item: (item[1][2], item[1][0]), reverse=True))
        sorted_teams[team] = sorted_champions

    return sorted_teams

def best_champions_pairs_per_team():

    matchhistory_df = pd.read_csv("data/match_history.csv")

    teams = {}
    #for each team, find the champions that that team has played and the win rate for each champion has
    # {team: {champion : [wins, losses, win_rate]}}
    for _, row in matchhistory_df.iterrows():
        winner = row['Winner']
        blue_win = winner == row['Blue'] 
        loser = row['Blue'] if winner != row['Blue'] else row['Red']
        
        if winner not in teams:
            teams[winner] = {}
        if loser not in teams:
            teams[loser] = {}


        blue_picks = row['B_Picks'].strip().split(",")
        champ_pairs = list(combinations(blue_picks, 2))
        for champ_pair in champ_pairs:
            if blue_win:
                if champ_pair not in teams[winner]:
                    teams[winner][champ_pair] = [1, 0, 1.0]
                else:
                    wins, losses = teams[winner][champ_pair][0] + 1, teams[winner][champ_pair][1] 
                    teams[winner][champ_pair] = [wins, losses, wins/(wins+losses)]
            else:
                if champ_pair not in teams[loser]:
                    teams[loser][champ_pair] = [0, 1, 0.0]
                else:
                    wins, losses = teams[loser][champ_pair][0], teams[loser][champ_pair][1] + 1
                    teams[loser][champ_pair] = [wins, losses, wins/(wins+losses)]
        
        red_picks = row['R_Picks'].strip().split(",")
        champ_pairs = list(combinations(red_picks, 2))
        for champ_pair in champ_pairs:
            if not blue_win:
                if champ_pair not in teams[winner]:
                    teams[winner][champ_pair] = [1, 0, 1.0]
                else:
                    wins, losses = teams[winner][champ_pair][0] + 1, teams[winner][champ_pair][1]
                    teams[winner][champ_pair] = [wins, losses, wins/(wins+losses)]
            else:
                if champ_pair not in teams[loser]:
                    teams[loser][champ_pair] = [0, 1, 0.0]
                else:
                    wins, losses = teams[loser][champ_pair][0], teams[loser][champ_pair][1] + 1
                    teams[loser][champ_pair] = [wins, losses, wins/(wins+losses)]
    
    sorted_teams = {}
    for team, champions in teams.items():
        sorted_champions = dict(sorted(champions.items(), key=lambda item: (item[1][2], item[1][0]), reverse=True))
        sorted_teams[team] = sorted_champions

    return sorted_teams


best_champ_team = best_champions_per_team()
best_champ_pairs_team = best_champions_pairs_per_team()

print(best_champ_team["T1"])
print(best_champ_pairs_team["T1"])
