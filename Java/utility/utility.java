package Java.utility;

import java.io.File;
import java.io.IOException;
import java.util.*;
import java.io.FileWriter;

public class utility {
    // Utility function for importing file into array
    public static String[] ImportFile(String path) throws IOException{
        File file = new File(path);
        ArrayList<String> data_list = new ArrayList<>();
        Scanner fileReader = new Scanner(file);
        while (fileReader.hasNextLine())
            data_list.add(fileReader.nextLine());
        fileReader.close();
        String[] data = new String[data_list.size()];
        data = data_list.toArray(data);
        return data;
    }

    // Utility function for exporting array into file
    public static void ExportFile(String path, String[] data){
        try {
            FileWriter fileWriter = new FileWriter(path);
            int i;
            for(i=0; i<data.length; i++){
                fileWriter.write(data[i]);
                if(i == data.length-1){
                    fileWriter.close();
                    break;
                }
                fileWriter.write("\n");
            }
        }catch(IOException e){
            e.printStackTrace();
        }
    }

    // Utility function for swapping
    public static void swap(String[] data, int i, int j){
        String tmp = data[i];
        data[i] = data[j];
        data[j] = tmp;
    }
}