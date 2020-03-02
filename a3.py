import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
forward euler is:
y_next = y_curr + step*f_y_dot(x_curr, y_curr)
x_next = x_curr + step*f_x_dot(x_curr, y_curr)
where step = 0.1
"""

def plotter(sets, title):
	plt.title(title)
	plt.xlabel("x")
	plt.ylabel("y")
	for i in range(0, len(sets)):
		plt.plot([pt[0] for pt in sets[i]],[pt[1] for pt in sets[i]], color='blue')
	plt.show()

step = 0.1

points_a = [(3*np.random.random_sample(), 2*np.random.random_sample()) for i in range(0,100)]
sets_a = [[pt] + 99*[None] for pt in points_a]

for i in range(0, len(sets_a)):
	for j in range(0, len(sets_a[i])):
		x_curr = sets_a[i][j][0]
		y_curr = sets_a[i][j][1]

		x_next = x_curr + step*(3-x_curr-2*y_curr)*x_curr
		y_next = y_curr + step*(2-y_curr-x_curr)*y_curr

		if (j+1 < len(sets_a[i])):
			sets_a[i][j+1] = (x_next,y_next)

plotter(sets_a, 'part a')

points_b = [(1*np.random.random_sample(), 1*np.random.random_sample()) for i in range(0,100)]
sets_b = [[pt] + 99*[None] for pt in points_b]
theta_b = 2

for i in range(0, len(sets_b)):
	for j in range(0, len(sets_b[i])):
		x_curr = sets_b[i][j][0]
		y_curr = sets_b[i][j][1]

		x_next = x_curr + step*(1-y_curr)*x_curr
		y_next = y_curr + step*(theta_b*x_curr-1)*y_curr

		if (j+1 < len(sets_b[i])):
			sets_b[i][j+1] = (x_next,y_next)

plotter(sets_b, 'part b')


















