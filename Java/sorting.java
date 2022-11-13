package Java;
import static Java.algo.Quick.*;
import static Java.utility.utility.*;
import java.io.IOException;

public class sorting {
    public static void main(String[] args) throws IOException{
        String[] data = ImportFile("sgb-words.txt");
        QuickSort(data, 0, data.length-1);
        ExportFile("Java/sgb-words-sorted-java.txt", data);
        Display(data);
    }
}
