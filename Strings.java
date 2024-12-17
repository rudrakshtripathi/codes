public class Strings {
   public static void main(String[] args) {
    String str1 = "Hello";  
    // String str1 = "Hell";  // you cant change the object of string in pool becuase Strings are immutable..
    System.out.println(str1);
    str1="fuck yuhh";    // here what happened that the object is not chjanged but a new object in the pool is created..
    System.out.println(str1);   // the ref var 'str1' is now shifted and is now pointing to newly created object i.e."fuck yuhh"

    String[] arr = str1.split(" ");
    System.out.println(java.util.Arrays.toString(arr));
















   }
} 