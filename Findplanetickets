# Importing libraries
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime

# Defining a function to scrape flight data from Expedia
def scrape_flights(origin, destination, date):
  # Constructing the url
  url = f"https://www.expedia.com/Flights-Search?flight-type=on&starDate={date}&endDate={date}&mode=search&trip=oneway&leg1=from:{origin},to:{destination},departure:{date}TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&options=cabinclass:economy,nopenalty:N,sortby:price&origref=www.expedia.com"
  # Sending a request and parsing the response
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  # Finding the flight elements
  flights = soup.find_all("li", class_="flight-module segment offer-listing")
  # Creating empty lists to store the data
  airlines = []
  durations = []
  prices = []
  # Looping through the flights and extracting the data
  for flight in flights:
    # Getting the airline name
    airline = flight.find("div", class_="secondary-content no-wrap").text.strip()
    airlines.append(airline)
    # Getting the flight duration
    duration = flight.find("span", class_="duration-emphasis").text.strip()
    durations.append(duration)
    # Getting the flight price
    price = flight.find("span", class_="full-bold no-wrap").text.strip()
    prices.append(price)
  # Returning a dataframe with the scraped data
  return pd.DataFrame({"airline": airlines, "duration": durations, "price": prices})

# Defining a function to preprocess the flight data
def preprocess_flights(df):
  # Converting the duration to minutes
  df["duration"] = df["duration"].apply(lambda x: int(x.split()[0][:-1]) * 60 + int(x.split()[1][:-1]))
  # Converting the price to numeric
  df["price"] = df["price"].apply(lambda x: float(x[1:].replace(",", "")))
  # Encoding the airline names as dummy variables
  df = pd.get_dummies(df, columns=["airline"], drop_first=True)
  # Returning the preprocessed dataframe
  return df

# Defining a function to train a linear regression model on the flight data
def train_model(df):
  # Splitting the data into features and target
  X = df.drop("price", axis=1)
  y = df["price"]
  # Splitting the data into train and test sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  # Creating and fitting a linear regression model
  model = LinearRegression()
  model.fit(X_train, y_train)
  # Printing the model score on the test set
  print(f"Model score: {model.score(X_test, y_test)}")
  # Returning the model
  return model

# Defining a function to predict the flight price for a given input
def predict_price(model, origin, destination, date, duration, airline):
  # Creating a dataframe with the input data
  input_df = pd.DataFrame({"duration": [duration]})
  # Encoding the airline name as a dummy variable
  input_df = pd.get_dummies(input_df, columns=["airline"], drop_first=True)
  # Adding the missing columns if any
  missing_cols = set(model.coef_.index) - set(input_df.columns)
  for col in missing_cols:
    input_df[col] = 0
  # Reordering the columns to match the model
  input_df = input_df[model.coef_.index]
  # Predict
