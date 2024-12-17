import java.util.Scanner;

public class CodindExercise1 {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Please, enter A side of a triangle: ");
        int A = sc.nextInt();
		System.out.print("Please, enter B side of a triangle: ");
        int B = sc.nextInt();
		System.out.print("Please, enter C side of a triangle: ");
        int C = sc.nextInt();
		
		int s = (A+B+C)/2;
		double triangleArea= Math.sqrt(s*(s-A)*(s-B)*(s-C));
        
		System.out.println("Triangle area is: " + triangleArea);

        System.out.print("Please, enter circle radius: ");
		int r= sc.nextInt();
		
		double circleCircumference = 2 * (Math.PI) * r;
		System.out.println("Circle circumference is: " + circleCircumference);
		
	}

}
