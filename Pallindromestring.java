import java.util.Scanner;
public class Pallindromestring {
   public static void main(String[] args) {
    // String str = "ababa";
    Scanner in = new Scanner(System.in);
    System.out.print("Enter a string:");
    String str = in.next();
    System.out.println(str);
    // String strnew = swap(str, 2,3);
    // System.out.println(strnew);
    String revnew = rev(str);
    System.out.println(revnew);

    if (str.equals(revnew)){
        System.out.println("Pallindrome");
    }
    else{
        System.out.println("Not Pallindrome");
    }


   }
   static String swap (char[] str, int index1, int index2){
    // char[] chars = str.toCharArray();
    char temp  = str[index1];
    str[index1] = str[index2];
    str[index2] = temp;
    return String.valueOf(str);
   }
    
   static String rev (String str){
    char[] arr= str.toCharArray();
    int start=0;
    int end= arr.length-1;
    while(start<end){
    // swap(str, start, end);
    swap(arr,start, end);
    start++;
    end--; 
   }
   return String.valueOf(arr);
    
   
   }
}