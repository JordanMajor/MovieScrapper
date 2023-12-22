from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


class getFilms:   

    def __init__(self,ratings,times,directors):
        self.ratings = ratings
        self.times = times
        self.directors = directors

    def setRatings(self):
        return self.ratings

    def setYear(self):
        return self.times
    
    def setDirector(self):
        return self.directors
    
class regression(getFilms):

    def __init__(self):
        self.ratings = ratings
        self.times = times
        self.directors = directors

    def train(self):
        pass


#Driver
ratings = []
times = []
directors = []

url = "https://editorial.rottentomatoes.com/guide/best-horror-movies-of-all-time/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
article = soup.find_all('h2')

#adding the scores into an array
for scores in article:
    scores = soup.find_all('span', class_={'tMeterScore'})
            
for score in scores:
    scr = score.text
    score_num = int(scr.rstrip('%'))
    ratings.append(score_num)
              
#adding the years into an array
for years in article:
    year_element = soup.find_all('span',class_={'subtle start-year'})

for year in year_element:
    yr = year.text
    year_num = int(yr.strip('()'))
    times.append(year_num)

#opening the directors csv file
directors = pd.read_csv('C:\\Users\\jorda\\OneDrive\\Documents\\Exel\\HorrorDirectors.csv')


gf = getFilms(ratings,times,directors)
r = regression()

arr1 = gf.setRatings
arr2 = gf.setYear

#r.train()
