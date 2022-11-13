import time
from Quick import QuickSort

def main():
    file = open("C:/Users/admin/Desktop/USM/CPT316-Assignment-1-master/sgb-words.txt")
    data = file.read().split("\n")
    file.close()

    size = len(data)
    start = time.time()
    print('Sorted Array in Ascending Order:')
    QuickSort(data, 0, size - 1)
    end = time.time()
    for i in data:
            print (i)
    print ("Time elapsed: " , int((end-start)*1000), "ms")
    
    file = open("Python/sgb-words-sorted-py.txt", "w")
    for i in data:
        file.write(i)
        if i==data[size-1]:
            break
        file.write("\n")
    file.close()

if __name__ == "__main__":
    main()