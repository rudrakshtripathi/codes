import java.util.Scanner;
public class Reverseword {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        String rev =  reverse(s);
        System.out.println(rev);

    } 
    static void swap(String[] arr, int index1, int index2){
        String temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
    static String reverse(String s){
        String[] arr = s.trim().split("\\s+");       
         int start=0;
        int end = arr.length-1;
        while(start<end){
            swap(arr,start,end);
            start++;
            end--;
    }
    return String.join(" ",arr);
}
}