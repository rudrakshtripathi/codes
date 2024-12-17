
import java.util.Arrays;

public class Swaparray {
    public static void main(String[] args) {
        int[] arr = {1,4,6,9,2,77,30};
        swap(arr,3,5);
        System.out.println(Arrays.toString(arr));
    }
    static void swap(int[] arr, int index1,int index2){
        int temp=arr[index1];
        arr[index1]=arr[index2];
        arr[index2]=temp;
    }
}