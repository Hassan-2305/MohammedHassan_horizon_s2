import matplotlib.pyplot as plt
import math

x = []
y = []

points = int(input("Enter how many points to plot: "))

for i in range(points):
    x_coo = float(input(f"Enter the x-coordinate of point {i + 1}: "))
    y_coo = float(input(f"Enter the y-coordinate of point {i + 1}: "))
    x.append(x_coo)
    y.append(y_coo)

plt.scatter(x, y, marker='o', color='red')

# Connect each point to its closest neighbor
for i in range(len(x)):
    closest_distance = float('inf')  # Initialize a large number for comparison
    closest_point_index = -1
    
    for j in range(len(x)):
        if i != j:  # Don't compare a point to itself
            # Calculate the Euclidean distance using math.sqrt
            distance = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            
            # Check if this distance is the smallest so far
            if distance < closest_distance:
                closest_distance = distance
                closest_point_index = j
    
    # Draw a line from point i to its closest neighbor
    plt.plot([x[i], x[closest_point_index]], [y[i], y[closest_point_index]], 'r-', alpha=0.5)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plotting Points and Connecting to Nearest Neighbor')

plt.show()
