import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
forward euler is:
y_next = y_curr + step*f_y_dot(x_curr, y_curr)
x_next = x_curr + step*f_x_dot(x_curr, y_curr)
where step = 0.1
"""

def plotter(figure, sets, title):
	plt.title(title)
	plt.xlabel("X")
	plt.ylabel("Y")
	for i in range(0, len(sets)):
		plt.plot([pt[0] for pt in sets[i]],[pt[1] for pt in sets[i]], color='blue')
	plt.show()

def plotter_c_2(figure, sets, title):
	plt.title(title)
	plt.xlabel("Delta")
	plt.ylabel("Tao")
	plt.plot([pt[0] for pt in sets],[pt[1] for pt in sets], 'o')
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

plotter(1, sets_a, 'Part A: Competing Dynamics Model')

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

plotter(2, sets_b, 'Part B: Predator–Prey Model')

thetas_c_2 = [round(x,1) for x in list(np.arange(0,1.1,0.1))]
fixed_points_c_2 = [(theta, theta/(0.1+theta**2)) for theta in thetas_c_2]
sets_c_2 = []

for pt in fixed_points_c_2:
	tao = (2*pt[0]*pt[1] - 1) + (-0.1-pt[0]**2)
	delta = (2*pt[0]*pt[1] - 1)*(-0.1-pt[0]**2) - (0.1+pt[0]**2)*(-2*pt[0]*pt[1])
	sets_c_2.append([delta, tao])

plotter_c_2(3, sets_c_2, 'Part C-2: Tao-Delta Plot')

points_c_4 = [(1*np.random.random_sample(), 1*np.random.random_sample()) for i in range(0,5)]
thetas_c_4 = [0.1, 0.5, 1]
sets_c_4 = [[pt] + 99*[None] for pt in points_c_4]

for theta in thetas_c_4:
	for i in range(0, len(sets_c_4)):
		for j in range(0, len(sets_c_4[i])):
			x_curr = sets_c_4[i][j][0]
			y_curr = sets_c_4[i][j][1]

			x_next = x_curr + step*(-x_curr + 0.1*y_curr + x_curr**2*y_curr)
			y_next = y_curr + step*(theta - 0.1*y_curr - x_curr**2*y_curr)

			if (j+1 < len(sets_c_4[i])):
				sets_c_4[i][j+1] = (x_next,y_next)

	plotter(4, sets_c_4, 'Part C: Selkov Model')




















