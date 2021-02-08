def bubble_sort(array):
	n = len(array)

	for i in range(n):
	# Create a flag thatwill allow the function to
	# terminate early if there's nothing left to sort
	already_sorted = True

	# Start looking at each item of the list one by one,
	# comparing it with its adjacent value. With each
	# iteration, the portion of the array that you look at
	# shrinks because the remaining items have already been
	# sorted
	for j in range(n - i - 1):
		if array[j] > array[j + 1]:
			# 
