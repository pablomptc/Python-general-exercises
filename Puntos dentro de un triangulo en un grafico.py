import pandas as pd
import matplotlib as plt
import numpy as np

a = pd.read_csv("rankings.csv")
e = pd.read_csv("Scale2.csv")
k = pd.read_csv("Final.csv")

#Regresion lineal python (FIND M AND  N)
X = a[["_DEMAND_ AVERAGE SCORE"]].values
y = a[["_OFFER_ AVERAGE SCORE"]].values


from sklearn.linear_model import LinearRegression
slr = LinearRegression()
slr.fit(X,y)
print("Slope: %.3f" % slr.coef_[0])

print("Intercept: %.3f" % slr.intercept_)

#Select the points above the line and below offer
#Seleccionar los puntos que estén por encima de la linea y debajo de offer= 3

#Slope: 0.507
#Intercept: 1.487

f = list(zip(b,c,d))


#Urban points
Urban_points = k[k.Scale == "Urban"]
Urban_points1 = Urban_points[Urban_points["_OFFER_ AVERAGE SCORE"] < 3]
Ux = Urban_points1["_DEMAND_ AVERAGE SCORE"].tolist()
Uy = Urban_points1["_OFFER_ AVERAGE SCORE"].tolist()
Uz = Urban_points1["Scale"].tolist()
Urban = list(zip(Ux,Uy,Uz))

above_U = []
under_U = []

for i in Urban:
    if i[1] > (0.507*(i[0])+1.487):
        above_U.append(i)
    else:
        under_U.append(i)
above_U




#Town points
Town_points = k[k.Scale == "Town"]
Town_points1 = Town_points[Town_points["_OFFER_ AVERAGE SCORE"] < 3]
Tx = Town_points1["_DEMAND_ AVERAGE SCORE"].tolist()
Ty = Town_points1["_OFFER_ AVERAGE SCORE"].tolist()
Tz = Town_points1["Scale"].tolist()
Town = list(zip(Tx,Ty,Tz))

above_T = []
under_T = []

for i in Town:
    if i[1] > (0.507*(i[0])+1.487):
        above_T.append(i)
    else:
        under_T.append(i)
under_T

#Rural points
Rural_points = k[k.Scale == "Rural"]
Rural_points1 = Rural_points[Rural_points["_OFFER_ AVERAGE SCORE"] < 3]
Rx = Rural_points1["_DEMAND_ AVERAGE SCORE"].tolist()
Ry = Rural_points1["_OFFER_ AVERAGE SCORE"].tolist()
Rz = Rural_points1["Scale"].tolist()
Rural = list(zip(Rx,Ry,Rz))

above_R = []
under_R = []

for i in Rural:
    if i[1] > (0.507*(i[0])+1.487):
        above_R.append(i)
    else:
        under_R.append(i)




 len(above_U)
len(above_T)
len(above_R)
