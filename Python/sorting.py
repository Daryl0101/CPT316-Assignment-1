from Quick import QuickSort

def main():
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

if __name__ == "__main__":
    main()