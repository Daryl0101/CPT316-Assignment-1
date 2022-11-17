# Partition Algorithm
def Partition(word, left, right):
	# Set the rightmost word as the pivot word
	pivot_word = word[right]

	# Initialize the index to place the words smaller than pivot word
	i = left-1

	# Continuously compare if the word currently pointed by j is smaller or equal to the pivot word is found
	# Place the word to position i if it is smaller than the pivot word
	# Thus all words smaller than the pivot word is placed on the left of pivot word
	for j in range(left,right):
		if word[j]<pivot_word:
			i = i+1
			(word[i],word[j]) = (word[j],word[i])

	# Place the pivot word to the right of the last word smaller than the pivot word
	# Thus all words greater than the pivot word is placed on the right of the pivot word
	(word[i+1],word[right]) = (word[right],word[i+1])

	# Return the index of the new pivot
	return i+1

# Quick Sort Algorithm
def QuickSort(word, left, right):
		# If the left index is smaller than the right index
		# Choose a new pivot using Partition Algorithm
		# Partition the list to the left and the right of the pivot word using Partition Algorithm
		# Recursively sort the left partition and the right partition using Quick Sort
		if left<right:
			pivot = Partition(word,left,right)
			QuickSort(word,left,pivot-1)
			QuickSort(word,pivot+1,right)