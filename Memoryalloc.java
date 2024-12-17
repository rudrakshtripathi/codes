public class Memoryalloc {
    public static void main(String[] args) {
        int a0=5;        // Primitive type memory allocation  
        int b0=5;        // these variable equals to the value in stack memory itself
        System.out.println(a0==b0);

        Integer a=128;    // Wrapper type (False.. dikha raha hain kyonki int ka range hi -128 se 127 hai)
        Integer b=128;    // its the reference variable both reference varialbe is pointing to different objects in heap memory.          
        System.out.println(a==b); 

         // we can use .equals() method for Integer(wrapper) variable as well
         System.out.println(a.equals(b)); // Now it will give True..

        Integer a1=66;
        Integer b1=66;                  // it show true because its inside the domain of int size(intger pool)
        System.out.println(a1==b1);


        int[] arr1= {1,2,3,4,5};
        int[] arr2= {1,2,3};            // comparing two arrays when its different guud 
        System.out.println(arr1==arr2);   // False 

        int[] arr3= {1,2,3};
        int[] arr4= {1,2,3};            // comparing two arrays if its same.but ouput is False.
        System.out.println(arr3==arr4); // because its arr1 and arr2 are reference to the different objects in heap memory.

          // now to compare properly we uses .equals() method for arrays 
          // Syntax of using .equals() method in Arrays is different from int..
          System.out.println(java.util.Arrays.equals(arr3, arr4));  // now its showing True...

         arr3 = arr4;  // after writing this both variable are pointing to the same object..
        System.out.println(arr3==arr4);// so it will show True.. because both variable are pointing to same object in heap memory.

    }
}
