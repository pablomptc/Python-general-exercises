CALCULATION OF NUMBER OF POINTS WITHIN A TRIANGLE

"""The objective of this exercise is to find the number of points of each type that are inside a triangle.
Each point is actually a bus stop in a city in Europe. The "X" coordinate is "demand average score" and the 
"y" coordinate is "offer average score". This two dimensions were calculated previously for each stop from 
different indicators. Values range from 1 to 5. Each stop can be of 3 types: rural, city and town. And this
does not depend on the two variables X and Y. And for a question of the project, it was asked to calculate 
all the points of city, rural and town that had an offer average score less than 3, and that at the same time 
were in the upper part of the line y = x."""

# Libraries
import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn.linear_model import LinearRegression


file = pd.read_csv("Final.csv")


# Urban points
urban_points = file[file.Scale == "Urban"]
urban_points_under_3 = urban_points[urban_points["_OFFER_ AVERAGE SCORE"] < 3]
urban_D = urban_points_under_3["_DEMAND_ AVERAGE SCORE"].tolist ()
urban_O = urban_points_under_3["_OFFER_ AVERAGE SCORE"].tolist ()
urban_S = urban_points_under_3["Scale"].tolist ()
urban = list (zip (urban_D, urban_O, urban_S))

above_u = []
under_u = []

for i in urban:
    if i[1] > i[0]:
        above_u.append (i)
    else:
        under_u.append (i)
        

# Town points
town_points = file[file.Scale == "Town"]
town_points_under_3 = town_points[town_points["_OFFER_ AVERAGE SCORE"] < 3]
town_D = town_points_under_3["_DEMAND_ AVERAGE SCORE"].tolist ()
town_O = town_points_under_3["_OFFER_ AVERAGE SCORE"].tolist ()
town_S = town_points_under_3["Scale"].tolist ()
town = list (zip (town_D, town_O, town_S))

above_t = []
under_t = []

for i in town:
    if i[1] > i[0]:
        above_t.append(i)
    else:
        under_t.append(i)
under_t


# Rural points
rural_points = file[file.Scale == "Rural"]
rural_points_under_3 = rural_points[rural_points["_OFFER_ AVERAGE SCORE"] < 3]
rural_D = rural_points_under_3["_DEMAND_ AVERAGE SCORE"].tolist ()
rural_O = rural_points_under_3["_OFFER_ AVERAGE SCORE"].tolist ()
rural_S = rural_points_under_3["Scale"].tolist ()
rural = list (zip (rural_D, rural_O, rural_S))

above_r = []
under_r = []

for i in rural:
    if i[1] > i[0]:
        above_r.append(i)
    else:
        under_r.append(i)



# NUMBER OF URBAN POINTS
u = str (len(above_u))
print ("The number of rural points is: " + u)

# NUMBER OF TOWN POINTS
t = str (len(above_t))
print ("The number of rural points is: " + t)

# NUMBER OF RURAL POINTS
r = str (len(above_r))
print ("The number of rural points is: " + r)
