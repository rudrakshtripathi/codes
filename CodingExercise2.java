import java.util.Arrays;
import java.util.Scanner;
public class CodingExercise2 {
   public static void main(String[] args) {
    
    // System.out.printf("%.1f%n", Math.PI);
    // System.out.printf("%.2f%n", Math.PI);
    // System.out.printf("%.3f%n", Math.PI);
    // System.out.printf("%.4f%n", Math.PI);
    // System.out.printf("%.5f%n", Math.PI);
    // System.out.println(Math.PI);

    for(int i=1;i<=5;i++){
        System.out.printf("%."+i+"f%n", Math.PI);
    }

        Scanner sc = new Scanner(System.in);
		System.out.print("Please, enter any text: ");
		String userInput = sc.nextLine();
		System.out.print("You entered these words: ");
        System.out.println(Arrays.toString(userInput.split("[\\p{P}\\s]+")));    

   }
}
