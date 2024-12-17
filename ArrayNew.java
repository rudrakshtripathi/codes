public class ArrayNew {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int[] newArray = new int[array.length];
        System.arraycopy(array, 0, newArray, 0, array.length);
        for (int i = 0; i < array.length; i++) {
            System.out.println(newArray[i]);
                                
    }
}