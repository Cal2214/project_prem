# 🏆 Premier League Match Predictor 

This project uses machine learning to predict the outcome of English Premier League (EPL) football matches. Given two teams, it estimates the chances of a home win, away win, or draw based on recent form, goals, and more.

## 🔧 Features

- ✅ User-friendly GUI built with `Tkinter`
- ✅ Team selection via dropdown menus
- ✅ Displays win/draw probabilities as percentages
- ✅ Trained on real Premier League match data
- ✅ Predicts results using logistic regression

## 🧠 How It Works

1. Collects data on goals, recent form, win rates, and head-to-head performance.
2. Trains a logistic regression model (`sklearn`) to predict match outcomes.
3. GUI allows user to select any two teams and receive a prediction instantly.

## 🗃️ Data Sources

- Match results from [BBC Sport](https://www.bbc.co.uk/sport/football/premier-league/scores-fixtures/2024-08)
- Features match outcomes, team forms, and win rates
