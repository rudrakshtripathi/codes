import java.util.Scanner;
public class Pallndrome_2 {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the String- ");
        String str = in.next();
        String reverse = rev(str);

        if (str.equals(reverse)){
            System.out.println("Pallindrome!!");
        }
        else {
            System.out.println("Not a Pallindrome!!!");
        }

        
    }

    static String Swap(char[] str, int index1, int index2 ){
        char temp = str[index1];
        str[index1]=str[index2];
        str[index2]=temp;
        return String.valueOf(str);
    }
    static String rev(String str){
        char[] arr = str.toCharArray();
        int start=0;
        int end = arr.length-1;
        while(start<end){
            Swap(arr, start,end);
            start++;
            end--;
        }
        return String.valueOf(arr);
    }









}
