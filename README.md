# Rover-Movement-Simulation-with-Battery-Usage-Tracking
This Python program calculates the movement of a rover based on user-input angle and time. It computes the total distance traveled, horizontal and vertical displacements, battery usage, and remaining battery. It checks if the rover can reach its destination and return based on battery levels and movement distance.

### Code Explanation:

```python
import math

# Constant variables stated below
battery_start = 100.0  # %
battery_usage = 2.7     # % per second
speed = 1.5             # m/s
```

### Constants Initialisation:
battery_start: The initial battery level, starting at 100%.
battery_usage: The rate of battery consumption in percentage per second (2.7% per second).
speed: The speed of the rover is set to 1.5 meters per second.

```python
angle_in_radians = float(input("Enter angle in degrees between 0 and 90: "))
angle_in_degrees = (angle_in_radians * (math.pi / 180))
time = float(input("Enter time of travel in seconds: "))  # time must be a positive number
```

### Input & Conversion:
The user is asked to input an angle in degrees between 0 and 90, which is converted from degrees to radians for trigonometric calculations.
The user is prompted to input the time the rover travels, measured in seconds.

```python
# Calculations
overall_distance_travelled = (speed * time)
horizontal_distance = (overall_distance_travelled * math.sin(angle_in_degrees))
vertical_distance = (overall_distance_travelled * math.cos(angle_in_degrees))
battery_used = (time * battery_usage)
battery_remaining = (battery_start - battery_used)
```

### Calculations:
overall_distance_travelled: The total distance moved in meters.
horizontal_distance: The horizontal displacement (x-axis) using the sine of the angle.
vertical_distance: The vertical displacement (y-axis) using the cosine of the angle.
battery_used: The battery consumption over the travel time.
battery_remaining: The remaining battery percentage after travel.

```python
# Output
print("Angle given in degrees:", angle_in_degrees)
print("Time given in seconds:", time)
print("Overall distance travelled:", overall_distance_travelled)
print("Horizontal distance travelled:", horizontal_distance)
print("Vertical distance travelled:", vertical_distance)
print("Battery used over travel:", battery_used)
print("Battery left after travel:", battery_remaining)
```

### Output:
Prints calculated values including angle, time, distance traveled, horizontal and vertical distances, battery used, and remaining battery.

```python
# Checking if the robot can achieve its destination
if battery_remaining < 0:
    print("Robot cannot reach destination due to inadequate battery.")
else:
    print("Robot can reach destination due to enough battery.")
```

### Battery Status Check:
Checks if the remaining battery is below 0%. If so, the rover cannot reach its destination.

```python
if horizontal_distance == 0:
    print("Robot will not be able to return along the same path.")
else:
    print("Robot will be able to return along the same path.")
```
    

### Return Path Check:
Checks if the horizontal distance is zero. If so, the rover cannot return along the same path; otherwise, it can return.

