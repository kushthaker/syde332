import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
forward euler is:
y_next = y_curr + step*f_y_dot(x_curr, y_curr)
x_next = x_curr + step*f_x_dot(x_curr, y_curr)
where step = 0.1
"""

def plotConfig(sets, title):

	for i in range(0, len(sets)):
		plt.plot([pt[0] for pt in sets[i]],[pt[1] for pt in sets[i]], color='blue')

  plt.title(title)
  plt.xlabel("x")
  plt.ylabel("y")
  plt.show()

step = 0.1

points = [(3*np.random.random_sample(), 2*np.random.random_sample()) for i in range(0,100)]
sets = [[pt] + 99*[None] for pt in points]

for i in range(0, len(sets)):
	for j in range(0, len(sets[i])):
		x_curr = sets[i][j][0]
		y_curr = sets[i][j][1]

		x_next = x_curr + step*(3-x_curr-2*y_curr)*x_curr
		y_next = y_curr + step*(2-y_curr-x_curr)*y_curr

		if (j+1 < len(sets[i])):
			sets[i][j+1] = (x_next,y_next)

plotConfig(sets, 'part a')














