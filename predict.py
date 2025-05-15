import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# Load the dataset
# df = pd.read_csv('prem_result_final.csv')
df = pd.read_csv('prem_result_increase.csv')


# Feature columns
X = df[['HomeGoals','AwayGoals','HomeWinRate','AwayWinRate','HomeH2HWinRate','AwayH2HWinRate','HomeRecentForm','AwayRecentForm','HomeTeam_Arsenal','HomeTeam_AstonVilla','HomeTeam_Bournemouth','HomeTeam_Brentford','HomeTeam_Brighton','HomeTeam_Chelsea','HomeTeam_Crystal Palace','HomeTeam_Everton','HomeTeam_Fulham','HomeTeam_Ipswich','HomeTeam_Leicester','HomeTeam_Liverpool','HomeTeam_ManCity','HomeTeam_ManUtd','HomeTeam_Newcastle','HomeTeam_NottmForest','HomeTeam_Southampton','HomeTeam_Tottenham','HomeTeam_WestHam','HomeTeam_Wolves','AwayTeam_Arsenal','AwayTeam_AstonVilla','AwayTeam_Bournemouth','AwayTeam_Brentford','AwayTeam_Brighton','AwayTeam_Chelsea','AwayTeam_Crystal Palace','AwayTeam_Everton','AwayTeam_Fulham','AwayTeam_Ipswich','AwayTeam_Leicester','AwayTeam_Liverpool','AwayTeam_ManCity','AwayTeam_ManUtd','AwayTeam_Newcastle','AwayTeam_NottmForest','AwayTeam_Southampton','AwayTeam_Tottenham','AwayTeam_WestHam','AwayTeam_Wolves']]
y = df['Result'] 
# print(df.columns) 
# print(X.isnull().sum()) 

# Split Data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Init Model 
logreg = LogisticRegression(random_state=16)

# Train Model 
logreg.fit(x_train, y_train)

# Predict 
prediction = logreg.predict(x_test)

# Check the Accurecy 
modelResults = accuracy_score(y_test, prediction)

# print(modelResults)
# print(confusion_matrix(y_test, prediction))
# print(classification_report(y_test, prediction))

def getTeams(homeTeamName, awayTeamName):
    home_column = f"HomeTeam_{homeTeamName}"
    away_column = f"AwayTeam_{awayTeamName}"

    # Find rows where either team was involved in a match
    home_matches = df[(df[home_column] == 1)]
    #print(home_matches)
    away_matches = df[(df[away_column] == 1)]
    #print(away_matches)

    # Get the last home team and away team matches 
    last_home = home_matches.tail(1)
    last_away = away_matches.tail(1)

    # Get the game column features
    features = {
        'HomeGoals' : last_home['HomeGoals'].values[0],
        'AwayGoals' : last_away['AwayGoals'].values[0],
        'HomeWinRate' : last_home['HomeWinRate'].values[0],
        'AwayWinRate' : last_away['AwayWinRate'].values[0],
        'HomeH2HWinRate' : last_home['HomeH2HWinRate'].values[0],
        'AwayH2HWinRate' : last_away['AwayH2HWinRate'].values[0],
        'HomeRecentForm' : last_home['HomeRecentForm'].values[0],
        'AwayRecentForm' : last_away['AwayRecentForm'].values[0]
    }

    # Create new row 
    create_row = pd.DataFrame([dict.fromkeys(X.columns, 0.0)])
    create_row.columns = X.columns

    # Fill in new row 
    for key in features: 
        create_row.at[0, key] = features[key]

    # Set columns 
    create_row.at[0, f"HomeTeam_{homeTeamName}"] = 1
    create_row.at[0, f"AwayTeam_{awayTeamName}"] = 1


    # Get prediction probabilities
    probabilities = logreg.predict_proba(create_row)[0]

    # Get the prediction
    predicted_result = logreg.predict(create_row)[0]

    return predicted_result, probabilities

