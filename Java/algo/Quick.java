package Java.algo;
import static Java.utility.utility.swap;

public class Quick {
    // Partition Algorithm
    private static int Partition(String[] word, int left, int right){
        // Set the rightmost word as the pivot word
        String pivot_word = word[right];
        
        // Initialize the index to place the words smaller than pivot word
        int i = left-1;

        // Continuously compare if the word currently pointed by j is smaller or equal to the pivot word is found
	    // Place the word to position i if it is smaller than the pivot word
	    // Thus all words smaller than the pivot word is placed on the left of pivot word
        for(int j=left;j<right;j++){
            if(word[j].compareTo(pivot_word)<0){
                i++;
                swap(word,i,j);
            }
        }

        // Place the pivot word to the right of the last word smaller than the pivot word
	    // Thus all words greater than the pivot word is placed on the right of the pivot word
        swap(word,i+1,right);

        // Return the index of the new pivot
        return i+1;
    }

    // Quick Sort Algorithm
    public static void QuickSort(String[] word, int left, int right){
        // If the left index is smaller than the right index
		// Choose a new pivot using Partition Algorithm
		// Partition the list to the left and the right of the pivot word using Partition Algorithm
        // Recursively sort the left partition and the right partition using Quick Sort
        if(left<right){
            int pivot = Partition(word,left,right);
            QuickSort(word,left,pivot-1);
            QuickSort(word,pivot+1,right);
        }
    }
}