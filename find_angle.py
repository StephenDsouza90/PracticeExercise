# https://www.hackerrank.com/challenges/find-angle/problem
# https://www.mathsisfun.com/algebra/trig-finding-angle-right-triangle.html
 
import math


def find_angle(ab, bc):
    arctan = math.atan2(ab, bc)
    degree_angle = math.degrees(arctan) 
    print(str(int(round(degree_angle))) + '°')
    

# Opposite
ab = float(input())
# Adjacent
bc = float(input())
find_angle(ab, bc)