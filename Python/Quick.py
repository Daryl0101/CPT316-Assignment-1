# Partition Algorithm
def Partition(word, left, right):

	# choose the rightmost element as pivot
	pivot_word = word[right]

	# pointer for greater element
	i = left - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(left, right):
		if word[j] <= pivot_word:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(word[i], word[j]) = (word[j], word[i])

	# Swap the pivot element with the greater element specified by i
	(word[i + 1], word[right]) = (word[right], word[i + 1])

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort


def QuickSort(word, left, right):
	if left < right:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pivot = Partition(word, left, right)

		# Recursive call on the left of pivot
		QuickSort(word, left, pivot - 1)

		# Recursive call on the right of pivot
		QuickSort(word, pivot + 1, right)


file = open("c:/Users/60134/Downloads/CPT316 Assignment 1/sgb-words.txt")
data = file.read().split("\n")
file.close()

size = len(data)

QuickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
file = open("python/sgb-words-sorted-py.txt", "w")
for i in data:
	file.write(i)
	if i==data[size-1]:
		break
	file.write("\n")
file.close()