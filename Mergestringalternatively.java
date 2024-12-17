import java.util.Scanner;
public class Mergestringalternatively {
   public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String str1 = in.nextLine();
    String str2 = in.nextLine();
    String res = mergealt(str1, str2);
    System.out.println(res);

   } 

   static String mergealt(String str1, String str2){
    StringBuilder s = new StringBuilder();
    int len = Math.min(str1.length(), str2.length());
    for (int i = 0; i < len; i++) {
        s.append(str1.charAt(i));
        s.append(str2.charAt(i));  
    }
    if(str1.length() > len){
        s.append(str1.substring(len));
   }
   if (str2.length()> len){
    s.append(str2.substring(len));
}
    return s.toString();
}
}