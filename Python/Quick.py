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


# file = open("c:/Users/60134/Downloads/CPT316 Assignment 1/sgb-words.txt")
# data = file.read().split("\n")
# file.close()

# size = len(data)

# QuickSort(data, 0, size - 1)

# print('Sorted Array in Ascending Order:')
# file = open("python/sgb-words-sorted-py.txt", "w")
# for i in data:
# 	file.write(i)
# 	if i==data[size-1]:
# 		break
# 	file.write("\n")
# file.close()