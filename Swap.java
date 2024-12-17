import java.util.Scanner;
public class Swap {
   public static void main(String[] args) {
     Scanner in = new Scanner(System.in);
    System.out.println("Enter the first number:");
    int a = in.nextInt();
    System.out.println("Enter the second number:");
    int b= in.nextInt();
    System.out.println("Before swapping:"+a +" "+ b);
    swap(b,a);
    System.out.println("After swapping:"+a +" "+ b);
   }

  public static void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;

   }
}
