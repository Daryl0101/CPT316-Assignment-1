import time
from Quick import QuickSort

def main():
    # Import list of text to sort
    file = open("sgb-words.txt")
    data = file.read().split("\n")
    file.close()

    # Timestamp when sorting starts
    start = time.time()

    # Quick Sort
    QuickSort(data, 0, len(data)-1)
    
    # Timestamp when sorting ends
    end = time.time()

    # Output execution time
    print ("Time elapsed: " , int((end-start)*1000), "ms")
    
    # Record sorting result in text file called "sgb-words-sorted-py.txt"
    file = open("Python/sgb-words-sorted-py.txt", "w")
    for i in data:
        file.write(i)
        if i==data[len(data)-1]:
            break
        file.write("\n")
    file.close()

if __name__ == "__main__":
    main()