
import java.util.Scanner;     //import Scanner package

public class Inputinjava {
    public static void main(String[] args) {
        Scanner in  = new Scanner(System.in);  // Syantax to intialise Scanner
        // System.out.print("Write my name-");
        // String name = in.next();            // Syntax to take input of Strings
        // System.out.println("my name is " + name);
        // System.out.print("What is my age - ");
        // int age = in.nextInt();             // Syntax to take input of Age
        // System.out.println("My age is " + age);

        String a =in.next();
        String b = in.next();
        int sum = Integer.parseInt(a)+Integer.parseInt(b);
        System.out.println(sum);
    }
}
