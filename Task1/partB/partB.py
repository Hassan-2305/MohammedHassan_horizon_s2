import matplotlib.pyplot as plt
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

x = []
y = []

points = int(input("Enter how many points to plot: "))

for i in range(points):
    x_coo = float(input(f"Enter the x-coordinate of point x{i + 1}: "))
    y_coo = float(input(f"Enter the y-coordinate of point y{i + 1}: "))
    x.append(x_coo)
    y.append(y_coo)

plt.scatter(x, y, marker='o', color='blue')

for i in range(len(x)):
    short_dist = float('inf')  
    near_neighbor = -1  

    for j in range(len(x)):
        if i != j: 
            dist = distance((x[i], y[i]), (x[j], y[j])) 
            if dist < short_dist:  
                short_dist = dist
                near_neighbor = j

    plt.plot([x[i], x[near_neighbor]], [y[i], y[near_neighbor]], color='r')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plotting Points and Connecting to Nearest Neighbor')

plt.show()
