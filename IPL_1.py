import numpy as np
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

#Years of Seasons
Seasons = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

#Seasons with numbers
Sdict = {2001:1,2002:2,2003:3,2004:4,2005:5,2006:6,2007:7,2008:8,2009:9,2010:10}

#Players
Players = ["Dhoni","Virat","Archer","Sachin","Jadeja","Bumrah","Hardik","Gill","Starc","Bhuvaneshwar","Sudharshan"]

#Players with Index
Pdict = {"Dhoni":1,"Virat":2,"Archer":3,"Sachin":4,"Jadeja":5,"Bumrah":6,"Hardik":7,"Gill":8,"Starc":9,"Bhuvaneshwar":10,"Sudharshan":11}

#Salaries
Dhoni_s = [10045069, 12221319, 14298396, 16346983, 18502576, 20563209, 23308691, 26227243, 28791763, 31577297]
Virat_s = [9741819, 11424863, 13118776, 15270236, 17325691, 19636776, 22102423, 24850290, 27575262, 30445139]
Archer_s = [6621289, 7595477, 8691996, 9858810, 11230002, 12702302, 14241299, 15965667, 17809865, 19687522]
Sachin_s = [8162719, 9731341, 11173657, 12734541, 14540001, 16248908, 18145909, 20241709, 22584878, 24973593]
Jadeja_s = [9834735, 11509436, 13121768, 14814601, 16617297, 18649020, 20637245, 22932653, 25180313, 27744063]
Bumrah_s = [6973312, 8039946, 9219442, 10560611, 12128761, 13772717, 15494831, 17383160, 19395031, 21572797]
Hardik_s = [9489457, 11108489, 12999115, 14735062, 16736108, 18938838, 21072016, 23386647, 25747763, 28411857]
Gill_s = [6119021, 7140755, 8393570, 9658480, 11014579, 12423679, 13931279, 15568392, 17210395, 18944295]
Starc_s = [7202302, 8346423, 9730427, 11024444, 12636338, 14386582, 16105528, 18049793, 20032859, 22058838]
Bhuvaneshwar_s = [6437551, 7449820, 8682219, 9940575, 11309608, 12666015, 14181265, 15783178, 17474236, 19290544]
Sudharsan_s = [7975480, 9334823, 10743222, 12438773, 14177414, 15898757, 17852476, 19790686, 21773001, 23917744]

#Matrix
Salary = np.array([Dhoni_s,Virat_s,Archer_s,Sachin_s,Jadeja_s,Bumrah_s,Hardik_s,Gill_s,Starc_s,Bhuvaneshwar_s,Sudharsan_s])

#Games
Dhoni_g = [80,77,82,82,73,82,58,78,6,35]
Virat_g = [82,57,82,79,76,72,60,72,79,80]
Archer_g = [79,78,75,81,76,79,62,76,77,69]
Sachin_g = [80,65,77,66,69,77,55,67,77,40]
Jadeja_g = [82,82,82,79,82,78,54,76,71,41]
Bumrah_g = [70,69,67,77,70,77,57,74,79,44]
Hardik_g = [78,64,80,78,45,80,60,70,62,82]
Gill_g = [35,35,80,74,82,78,66,81,81,27]
Starc_g = [40,40,40,81,78,81,39,0,10,32]
Bhuvaneshwar_g = [75,51,51,79,77,76,49,69,54,62]
Sudharsan_g = [78,56,50,43,34,53,34,43,34,43]

#Games_matrix
Games = np.array([Dhoni_g,Virat_g,Archer_g,Sachin_g,Jadeja_g,Bumrah_g,Hardik_g,Gill_g,Starc_g,Bhuvaneshwar_g,Sudharsan_g])

#Points
Dhoni_p = [1830, 2629, 1976, 1642, 1447, 1468, 1746, 1626, 2333, 1205]
Virat_p = [2592, 1946, 1124, 2784, 1703, 2396, 2207, 2786, 1352, 1285]
Archer_p = [1712, 2024, 1118, 1231, 1125, 1864, 1957, 1431, 1422, 2124]
Sachin_p = [2607, 2771, 2531, 2614, 2717, 2639, 2425, 2654, 2224, 1219]
Jadeja_p = [1324, 2113, 2144, 1041, 2073, 2097, 2712, 2502, 2240, 1844]
Bumrah_p = [2107, 1701, 1482, 2784, 1580, 1857, 1880, 1919, 2159, 1411]
Hardik_p = [1813, 1771, 2724, 2617, 1622, 1434, 2010, 2573, 2614, 2443]
Gill_p = [1255, 1230, 1751, 2086, 2193, 2347, 1275, 2379, 2295, 2584]
Starc_p = [1825, 1342, 1978, 2408, 2029, 2312, 2432, 2362, 1704, 2500]
Bhuvaneshwar_p = [2115, 1154, 2360, 1480, 2125, 2742, 1809, 1942, 2364,2487]
Sudharsan_p = [1266, 2756, 2346, 2181, 1880, 2391, 1034, 2403, 1019, 2595]

#Points_matrix
Points = np.array([Dhoni_p,Virat_p,Archer_p,Sachin_p,Jadeja_p,Bumrah_p,Hardik_p,Gill_p,Starc_p,Bhuvaneshwar_p,Sudharsan_p])

print(Salary)
print(Points)
print(Games)
print(Salary[0])
print(Salary[0,4])
print(Games[0:5])
print(Salary/Games)
print(np.round(Salary/Games))
print(plt.plot(Salary[0]))
print(plt.xticks(list(range(0,10)),Seasons))
print(plt.show())
print(plt.plot(Salary[0],ls=':'))#line style will add style to the marked line in the graph
print(plt.xticks(list(range(0,10)),Seasons,rotation='vertical'))
print(plt.show())
print(plt.plot(Salary[0],ls=':',color='red'))#color will add the color to the line
print(plt.show())
print(plt.plot(Salary[0],ls=':',color='red',marker='s'))#marker will add the type of the mark
print(plt.show())
print(plt.plot(Salary[0],ls=':',color='red',marker='s',ms=8,label="Dhoni"))#ms is marker size means tickness of the line
print(plt.plot(Salary[1],ls=':',color='blue',marker='o',ms=8,label="Virat"))
print(plt.plot(Salary[2],ls=':',color='purple',marker='^',ms=8,label="Archer"))
print(plt.plot(Salary[3],ls=':',color='yellow',marker='*',ms=8,label="Sachin"))
print(plt.xticks(list(range(0,10)),Seasons,rotation='vertical'))
print(plt.legend(loc='best'))
print(plt.show())