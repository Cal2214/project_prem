import predict
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Create GUI Window 
window = tk.Tk()
window.geometry("600x600")
window.title("AI Prem Predictor")

# Create Prem Label 
title_label = tk.Label(window,text="Pick Two Teams", font=("Arial",40))
title_label.pack()
title_label.place(x=100, y=0)

# Create Vs Label 
vs_label = tk.Label(window,text="Vs", font=("Arial",20))
vs_label.pack()
vs_label.place(x=279, y=200)

# Create Dropdowns

# Store Teams 
teams = ["Arsenal", "AstonVilla", "Bournemouth", "Brentford", "Brighton", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich", "Leicester", "Liverpool", "ManCity", "ManUtd", "Newcastle", "NottmForest", "Southampton", "Tottenham", "WestHam", "Wolves"]

# Home Label
home_label = tk.Label(window, text="Home Team", font=("Arial",20))
home_label.pack()
home_label.place(x=120, y=200)

# Home DropDown
home_dropdown = ttk.Combobox(window, values=teams)
home_dropdown.pack()
home_dropdown.place(x=120, y=250)

# Away Label
away_label = tk.Label(window, text="Away Team", font=("Arial",20))
away_label.pack()
away_label.place(x=320, y=200)

# Away DropDown
away_dropdown = ttk.Combobox(window, values=teams)
away_dropdown.pack()
away_dropdown.place(x=320, y=250)

# Final Prediction Label
prediction_label = tk.Label(window, text="Predicted Result:", font=("Arial",20))
prediction_label.pack()
prediction_label.place(x=200, y=360)

# Home win / Away win / draw Label
prediction_Win_label = tk.Label(window, text="", font=("Arial",14))
prediction_Win_label.pack()
prediction_Win_label.place(x=270, y=400)

# Home Win Chance Label
home_win_label = tk.Label(window, text="Home Win Chance:", font=("Arial",12))
home_win_label.pack()
home_win_label.place(x=50, y=500)

# Home Win Chance Label
home_win_percent_label = tk.Label(window, text="", font=("Arial",9))
home_win_percent_label.pack()
home_win_percent_label.place(x=100, y=520)

# Draw Chance Label
draw_label = tk.Label(window, text="Draw Chance:", font=("Arial",12))
draw_label.pack()
draw_label.place(x=270, y=500)

# Draw Chance Label
draw_percent_label = tk.Label(window, text="", font=("Arial",9))
draw_percent_label.pack()
draw_percent_label.place(x=300, y=520)

# Away Win Chance Label
away_win_label = tk.Label(window, text="Away Win Chance:", font=("Arial",12))
away_win_label.pack()
away_win_label.place(x=450, y=500)

# Away Win Chance Label
away_win_percent_label = tk.Label(window, text="", font=("Arial",9))
away_win_percent_label.pack()
away_win_percent_label.place(x=500, y=520)

# Get Dropdown Teams 
def getDropdownResults():
    home_team = home_dropdown.get()
    away_team = away_dropdown.get()

    # --- Input validation ---
    if not home_team or not away_team:
        messagebox.showwarning("Input Error", "Please select both a Home and Away team.")
        return

    if home_team == away_team:
        messagebox.showwarning("Input Error", "Home and Away teams cannot be the same.")
        return

    result, probabilities = predict.getTeams(home_team, away_team)
    predicted_label, result_probs = getResults(result, probabilities)
    displayResults(predicted_label, result_probs)


def getResults(result, probabilities):
    # Display Predicted Result 
    label_to_result = {-1: "Away Win", 0: "Draw", 1: "Home Win"}
    predicted_label = label_to_result[result]

    # Display Predicted Prob
    result_probs = {
        label_to_result[label]: prob for label, prob in zip(predict.logreg.classes_, probabilities)
    }

    return predicted_label, result_probs

def displayResults(predicted_label, result_probs):
    prediction_Win_label.config(text=predicted_label)
    home_win_percent_label.config(text=f"{result_probs.get('Home Win', 0)*100:.2f}%")
    draw_percent_label.config(text=f"{result_probs.get('Draw', 0)*100:.2f}%")
    away_win_percent_label.config(text=f"{result_probs.get('Away Win', 0)*100:.2f}%")

# Create Prediction Button 
predict_button = tk.Button(window, text="Predict")
predict_button.config(command=getDropdownResults)
predict_button.pack()
predict_button.place(x=270, y=300)


window.mainloop()
