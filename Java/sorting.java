package Java;
import static Java.algo.Quick.*;
import static Java.utility.utility.*;
import java.io.IOException;

public class sorting {
    public static void main(String[] args) throws IOException{
        // Import list of text to sort
        String[] data = ImportFile("sgb-words.txt");

        // Timestamp when sorting starts
        long start = System.nanoTime();
        
        // Quick Sort
        QuickSort(data, 0, data.length-1);

        // Timestamp when sorting ends
        long end = System.nanoTime();

        // Output execution time
        System.out.println("Time executed: " + (end - start)/1000000 + " ms");

        // Record sorting result in text file called "sgb-words-sorted-java.txt"
        ExportFile("Java/sgb-words-sorted-java.txt", data);
    }
}
