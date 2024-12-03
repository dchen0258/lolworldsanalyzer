import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def predict_winner_on_draft():
    # Load Data
    champions_df = pd.read_csv("data/champions.csv")
    matchhistory_df = pd.read_csv("data/match_history.csv")

    # Get list of champions
    champions = champions_df['Champion'].unique()

    # Initialize columns for each champion by team side
    for champion in champions:
        matchhistory_df[f'Blue_{champion}'] = 0
        matchhistory_df[f'Red_{champion}'] = 0

    # Populate champion columns based on picks
    for idx, row in matchhistory_df.iterrows():
        blue_picks = row['B_Picks'].split(",") # Picks array for Blue team
        red_picks = row['R_Picks'].split(",")# Picks array for Red team
        for champion in blue_picks:
            matchhistory_df.loc[idx, f'Blue_{champion}'] = 1
        for champion in red_picks:
            matchhistory_df.loc[idx, f'Red_{champion}'] = 1

    # Encode target label: 1 if Blue wins, 0 if Red wins
    matchhistory_df['Winner_Label'] = matchhistory_df['Winner'] == matchhistory_df['Blue']

    # Prepare feature matrix X and target vector y
    X = matchhistory_df[[col for col in matchhistory_df.columns if 'Blue_' in col or 'Red_' in col]]
    y = matchhistory_df['Winner_Label']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

    # Model training
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Prediction and Evaluation
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model Accuracy: {accuracy:.2f}")

    return model

def run_model(filename, model):
    champions_df = pd.read_csv("data/champions.csv")
    matchhistory_df = pd.read_csv(filename)

    # Get list of champions
    champions = champions_df['Champion'].unique()

    # Initialize columns for each champion by team side
    for champion in champions:
        matchhistory_df[f'Blue_{champion}'] = 0
        matchhistory_df[f'Red_{champion}'] = 0

    # Populate champion columns based on picks
    for idx, row in matchhistory_df.iterrows():
        blue_picks = row['B_Picks'].split(",") # Picks array for Blue team
        red_picks = row['R_Picks'].split(",")# Picks array for Red team
        for champion in blue_picks:
            matchhistory_df.loc[idx, f'Blue_{champion}'] = 1
        for champion in red_picks:
            matchhistory_df.loc[idx, f'Red_{champion}'] = 1

    # Encode target label: 1 if Blue wins, 0 if Red wins
    matchhistory_df['Winner_Label'] = matchhistory_df['Winner'] == matchhistory_df['Blue']

    # Prepare feature matrix X and target vector y
    X = matchhistory_df[[col for col in matchhistory_df.columns if 'Blue_' in col or 'Red_' in col]]
    y = matchhistory_df['Winner_Label']

    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")


trained_model = predict_winner_on_draft()
run_model("data/match_test.csv", trained_model)
