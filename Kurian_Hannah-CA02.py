# Kurian_Hannah, 201765922, October2023 CA-02.py
# Inputs angle and time
# Outputs include overall travelled, horizontal movement, vertical movement, battery usage , battery remaining, echo_inputs, state whether destination can be reached by rover
# States whether destination can be reached given angle and time

import math

#Constant variables stated below
battery_start= 100.0 #%
battery_usage= 2.7 #% per second
speed= 1.5 #m/s


angle_in_radians= float(input("enter angle in degrees between 0 and 90: "))
angle_in_degrees= (angle_in_radians *(math.pi/180))
time= float(input("enter time of travel in seconds: ")) #time must be a positive number 
print()

#Calculations
overall_distance_travelled= (speed *time)
horizontal_distance= (overall_distance_travelled *math.sin(angle_in_degrees))
vertical_distance= (overall_distance_travelled *math.cos(angle_in_degrees))
battery_used= (time * battery_usage)
battery_remaining= (battery_start- battery_used)
print()

#Output
print ("angle given in degrees: ", angle_in_degrees)
print ("time given in seconds: ", time)
print ("overall distance travelled: ", overall_distance_travelled)
print ("horizontal distance travelled: ", horizontal_distance)
print ("vertical distance travelled ", vertical_distance)
print ("battery used over travel: ", battery_used)
print ("battery left after travel: ", battery_remaining)

# checking if robot can achieve its destination

if battery_remaining <0:
    print ("robot cannot reach destination due to inadequate battery ")
else:
    print ("robot can reach destination due to enough battery")


    if horizontal_distance==0:
        print ("robot will not be able to return along the same path")
    else:
        print ("robot will be able to return along the same path")
    

#Test   Angle in radians, Time in seconds     Expected Battery Remaining, Horizontal Distance     Actual Battery Remaining, Horizontal Distance      Destination Reached?      Comment

#1      10,20                                     46.0, 5.21                                          46.0, 5.21                                        Yes               Test successful 
#2      30,100                                   -170.0, 75.0                                        -170.0, 75.0                                       No                Test successful                                                            No               Test successful
#3      45,80                                    -116.0, 84.9                                        -116.0, 84.9                                       No                Test successful
#4      65,15                                     59.5, 20.4                                          59.5, 20.4                                        Yes               Test successful                                                                                              
#5      50,75                                    -102.5, 86.2                                        -102.5, 86.2                                       No                Test successful



 
