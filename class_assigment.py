#1.1
a=int(input())   
b=int(input())
sum=a+b
print("Sum of a and b is", sum)

#1.2
a=int(input())
b=int(input())
sub=a-b
print("The difference when b is subtracted from a is", sub)

#1.3
a=int(input())
b=int(input())
product=a*b
print("The product of a and b is", product)

#1.4
a=int(input())
b=int(input())
quot=a/b
print("The quotient when a is divided by b is", quot)

#1.5
a=int(input())
b=int(input())
rem=a%b
print("The remainder when a is divided by b is", rem)
#1.6
import math
a=int(input())
print(math.log10(a))

a=int(input())
b=int(input())
square=a**b
print("The squere is", square)

#2.1
mpg=float(input())
liters_per_hund_km= 235.21/mpg
print(mpg, "miles-per-gallon are equivalent", liters_per_hund_km, "L/100km")




#3.1
import math                  #degrees = radian * (180° / pi)
                            #a float value, representing the value in degrees
lat1=float(input())         
long1=float(input())
lat2=float(input())
long2=float(input())

  #converting into radians because distance f-cion (with sin, cos etc) uses radians as inputs
lat1_r= math.degrees(lat1) 
long1_r=math.degrees(long1)
lat2_r=math.degrees(lat2)
long2_r=math.radians(long2)
distance=6371.01*math.acos((math.sin(lat1_r)*math.sin(lat2_r)+math.cos(lat1_r)*math.cos(lat2_r)*math.cos(long1_r-long2_r)))
print(distance)

#4.1
distance_feet = int(input("distance in feet: "))
distance_inches = distance_feet * 12
distance_yards = distance_feet / 3.0
distance_miles = distance_feet / 5280.0
 
print("The distance in inches is %i inches." % distance_inches)
print("The distance in yards is %.2f yards." % distance_yards)
print("The distance in miles is %.2f miles." % distance_miles)





#5.1
import math

n=int(input("the number of sides: "))
s=float(input("the length of a side: "))
area= n*(s**2)/4*math.tan(math.pi/n)
print("Area of a regular polygon is", area)

#6.1
from datetime import datetime

current_datatime= datetime.now()
print(current_datatime)



#7.1
Ta=float(input("temperature in degrees C is "))
V=float(input("wind speed in km/h id "))

WCI= round(13.12+0.6215*Ta-11.37* V**0.16 +0.3965* Ta* V**0.16, 2)

print("The wind chill index is ", WCI)

