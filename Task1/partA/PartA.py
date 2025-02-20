import matplotlib.pyplot as plt

x = []
y = []

points = int(input("enter how many points to plot "))

for i in range(points):
    x_coo = float(input(f"Enter the x-coordinate of point x{i + 1}: "))
    y_coo = float(input(f"Enter the y-coordinate of point y{i + 1}: "))
    x.append(x_coo)
    y.append(y_coo)

    plt.scatter(x, y, marker ='o')

    plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plotting Points in Matplotlib')


plt.show()
