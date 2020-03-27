# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import pdb

# """
# q = []
# for [i]
#     for [j]
#         random [i][j] += 1;
#         if point[i][j] == 4
#             add +1 each neighbour
#             [i+1][j] +=1
#             [i-1][j] +=1
#             [i][j+1] +=1
#             [i][j-1] +=1
#             q[i] +=1
#         else
#             break
# plot (i,q)
# plot (q[i], freq(q[i]))
# """
def plotter(x, y, title):
	plt.title(title)
	plt.xlabel("Iterations")
	plt.ylabel("Count of Topples")
	plt.plot(x,y)
	plt.show()

def drop_grain():
	rand_pt = (int(np.random.random()*99),int(np.random.random()*99))
	grid[rand_pt[0]][rand_pt[1]] += 1

def get_topple_freq(topple_counts):
	freqs = {}
	for count in topple_counts:
		if freqs.get(count):
			freqs[count] += 1
		else:
			freqs[count] = 1
	return freqs

def topple(grid, i, j, sum_state, topple_count, iteration):
	if i < 99:
		if grid[i+1][j] < 4:
			grid[i+1][j] +=1
			grid[i][j] = grid[i][j] - 1
	if i > 0:
		if grid[i-1][j] < 4:
			grid[i-1][j] +=1
			grid[i][j] = grid[i][j] - 1
	if j < 99:
		if grid[i][j+1] < 4:
			grid[i][j+1] +=1
			grid[i][j] = grid[i][j] - 1
	if j > 0: 
		if grid[i][j-1] < 4: 
			grid[i][j-1] +=1
			grid[i][j] = grid[i][j] - 1

grid = np.zeros((100,100))
topple_counts = np.zeros(30000)
sum_state = np.zeros(30000)

for iteration in range(0,len(topple_counts)):
	drop_grain()
	for i in range(0,len(grid)):
		for j in range(0, len(grid[i])):
			if grid[i][j] >= 4:
				topple_counts[iteration] += 1
				topple(grid, i, j)

plotter(list(range(0, len(topple_counts))), list(topple_counts), 'Part A: Count of Topples vs. Iteration')
plotter(list(range(0, len(topple_counts))), list(sum_state), 'Part A: State Sum vs. Iteration')

#freqs

freqs = get_topple_freq(topple_counts)
freqs_x = sorted((freqs.keys()))
freqs_y = list(map(lambda count: freqs[count],freqs_x))
 
plt.xlabel('Event Size (Log_10)')
plt.ylabel('Event Frequency (Log_10)')
plt.plot(np.log10(freqs_x), np.log10(freqs_y))
plt.show()



