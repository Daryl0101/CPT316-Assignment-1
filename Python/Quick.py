import time

# Partition Algorithm
def Partition(word, left, right):
	pivot_word = word[right]

	i = left - 1

	for j in range(left, right):
		if word[j] <= pivot_word:
			i = i + 1

			(word[i], word[j]) = (word[j], word[i])

	(word[i + 1], word[right]) = (word[right], word[i + 1])

	return i + 1

# Quick Sort Algorithm
def QuickSort(word, left, right):
		
		if left < right:
			pivot = Partition(word, left, right)

			QuickSort(word, left, pivot - 1)

			QuickSort(word, pivot + 1, right)